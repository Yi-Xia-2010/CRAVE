import re
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import argparse
import torch
from pathlib import Path
from collections import defaultdict
from scipy.stats import ttest_ind, shapiro, kruskal, mannwhitneyu, sem, t

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None

from transformers import AutoTokenizer, AutoModelForTokenClassification


# Configuration 

DEFAULT_MODEL_PATH    = "chrlukas/stories-emotion-c8"
CONTEXT_WINDOW_RADIUS = 4
HIGH_THRESHOLD        = 0.65
LOW_THRESHOLD         = 0.35

METHODS = ["RAF_NoCritic", "RAF_Critic", "AVL_NoCritic", "AVL_Critic"]

# Map actual folder names → canonical method names
FOLDER_TO_METHOD = {
    "Rise_and_Fall":        "RAF_NoCritic",
    "Rise_and_Fall_Critic": "RAF_Critic",
    "V_and_A_levels":       "AVL_NoCritic",
    "V_and_A_levels_Critic":"AVL_Critic",
    # Also accept canonical names directly
    "RAF_NoCritic":         "RAF_NoCritic",
    "RAF_Critic":           "RAF_Critic",
    "AVL_NoCritic":         "AVL_NoCritic",
    "AVL_Critic":           "AVL_Critic",
}

# 4 pre-planned comparisons (no correction applied)
PLANNED_PAIRS = [
    ("RAF_NoCritic", "RAF_Critic"),    # Critic effect within RAF
    ("AVL_NoCritic", "AVL_Critic"),    # Critic effect within AVL
    ("RAF_NoCritic", "AVL_NoCritic"),  # Curve effect without Critic
    ("RAF_Critic",   "AVL_Critic"),    # Curve effect with Critic
]

METHOD_COLORS = {
    "RAF_NoCritic": "#4C72B0",
    "RAF_Critic":   "#1A4A8A",
    "AVL_NoCritic": "#C44E52",
    "AVL_Critic":   "#8A1A1E",
}

METRICS = [
    ("Valence Affective Salience (AS)",        "v_as",  False),
    ("Arousal Affective Salience (AS)",         "a_as",  False),
    ("Valence High-Salience Proportion (%)",    "v_hsp", True),
    ("Arousal High-Salience Proportion (%)",    "a_hsp", True),
]

STATS_CSV_HEADER = [
    "Metric",
    "Global_Kruskal_P", "Global_Significant",
    "Group_A", "Group_B", "N_A", "N_B",
    "Mean_A", "CI95_A_Lower", "CI95_A_Upper",
    "Mean_B", "CI95_B_Lower", "CI95_B_Upper",
    "Mean_Diff", "Diff_CI95_Lower", "Diff_CI95_Upper", "Cohen_d",
    "Normal_A (Shapiro_p)", "Normal_B (Shapiro_p)",
    "Welch_t_p", "MannWhitney_p",
    "Test_Used", "Final_p", "Significance", "Conclusion",
]


# Helpers 

def sig_stars(p):
    if p is None or np.isnan(p): return "N/A"
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    return "ns"

def fmt(v, decimals=4):
    if v is None or (isinstance(v, float) and np.isnan(v)): return "N/A"
    return f"{v:.{decimals}f}"

def compute_mean_ci(data, confidence=0.95):
    n = len(data)
    if n < 2: return np.nan, np.nan
    m   = np.mean(data)
    se  = sem(data)
    if se == 0: return m, m
    h   = se * t.ppf((1 + confidence) / 2., n - 1)
    return m - h, m + h

def compute_diff_ci(a, b, confidence=0.95):
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2: return np.nan, np.nan, np.nan, np.nan
    m1, m2 = np.mean(a), np.mean(b)
    v1, v2 = np.var(a, ddof=1), np.var(b, ddof=1)
    diff   = m1 - m2
    se     = np.sqrt(v1/n1 + v2/n2)
    if se == 0: return diff, diff, diff, 0.0
    df     = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))
    margin = t.ppf((1 + confidence) / 2., df) * se
    s_pool = np.sqrt(((n1-1)*v1 + (n2-1)*v2) / (n1+n2-2))
    d      = (diff / s_pool) if s_pool != 0 else 0.0
    return diff, diff - margin, diff + margin, d

def check_normality(arr):
    if len(arr) < 3: return np.nan
    if np.max(arr) == np.min(arr): return np.nan
    _, p = shapiro(arr)
    return p


# Emotion Model 

def load_model(model_path):
    print(f"[Loading emotion model: {model_path}]")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model     = AutoModelForTokenClassification.from_pretrained(model_path)
        model.eval()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if torch.backends.mps.is_available(): device = torch.device("mps")
        model.to(device)
        return tokenizer, model, device
    except Exception as e:
        print(f"  ERROR loading model: {e}")
        return None, None, None

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def predict_sentence_with_context(target, history, future, tokenizer, model, device):
    prev   = history[-CONTEXT_WINDOW_RADIUS:] if history else []
    nxt    = future[:CONTEXT_WINDOW_RADIUS]   if future  else []
    cls_id = tokenizer.cls_token_id
    sep_id = tokenizer.sep_token_id
    ids    = [cls_id]
    for blk in prev:
        ids.extend(tokenizer.encode(blk, add_special_tokens=False))
        ids.append(sep_id)
    target_sep_rank = len(prev)
    ids.extend(tokenizer.encode(target, add_special_tokens=False))
    ids.append(sep_id)
    for blk in nxt:
        ids.extend(tokenizer.encode(blk, add_special_tokens=False))
        ids.append(sep_id)
    if len(ids) > 512: ids = ids[:512]
    sep_positions = [i for i, x in enumerate(ids) if x == sep_id]
    target_sep = sep_positions[target_sep_rank] if target_sep_rank < len(sep_positions) else -1
    if target_sep == -1: return 0.5, 0.5
    with torch.no_grad():
        out = model(input_ids=torch.tensor([ids], device=device))
    logits = out.logits[0, target_sep].cpu().numpy()
    return float(sigmoid(logits[0])), float(sigmoid(logits[1]))

def extract_sentences(filepath):
    sentences = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(("#", "=", ">", "--", "[NEXT", "[Choice:")):
                continue
            line = re.sub(r"\[.*?\]", "", line)
            line = re.sub(r"^.*?:\s*", "", line)
            line = line.replace('"', "")
            if line.strip():
                parts = re.split(r"(?<=[.!?])\s+", line)
                sentences.extend(s.strip() for s in parts if s.strip())
    return sentences

def predict_file(filepath, tokenizer, model, device):
    sentences = extract_sentences(filepath)
    if not sentences: return [], []
    valences, arousals = [], []
    for i, text in enumerate(sentences):
        v, a = predict_sentence_with_context(
            text, sentences[:i], sentences[i+1:], tokenizer, model, device)
        valences.append(v)
        arousals.append(a)
    return valences, arousals


# Route-Level Aggregation

def collect_case_data(case_dir, tokenizer, model, device, base_path, out_root=None):
    try:
        rel = case_dir.relative_to(base_path)
    except ValueError:
        rel = Path(case_dir.name)

    parts = rel.parts
    folder_name = parts[0]
    method_name = FOLDER_TO_METHOD.get(folder_name, folder_name)
    # Path layout: method / Theme / genre / World_Curve_X_Story_Y
    theme_name = parts[1] if len(parts) > 1 else "unknown"
    genre_name = parts[2] if len(parts) > 2 else "unknown"
    novel_name = parts[3] if len(parts) > 3 else "unknown"

    # Extract curve type from "World_Curve_X_Story_Y" → "Curve_X"
    m = re.search(r"Curve_(\d+)", novel_name, re.IGNORECASE)
    curve_name = f"Curve_{m.group(1)}" if m else "unknown"

    routes_dir  = case_dir / "Story_Routes"
    route_metrics = []

    if not routes_dir.exists():
        return route_metrics

    # Output dir for raw sentence sequences (mirrors source structure)
    if out_root is not None:
        seq_dir = out_root / "Raw_Sequences" / method_name / theme_name / genre_name / novel_name
        seq_dir.mkdir(parents=True, exist_ok=True)
    else:
        seq_dir = None

    for fp in routes_dir.glob("*.txt"):
        vs, as_ = predict_file(fp, tokenizer, model, device)
        if len(vs) < 2: continue
        v_arr = np.array(vs)
        a_arr = np.array(as_)

        # Save per-route sentence sequence CSV 
        if seq_dir is not None:
            sentences = extract_sentences(fp)
            seq_rows  = [["Sentence_Index", "Sentence", "Valence", "Arousal"]]
            for idx, (sent, v, a) in enumerate(zip(sentences, vs, as_)):
                seq_rows.append([idx + 1, sent, round(v, 6), round(a, 6)])
            with open(seq_dir / f"{fp.stem}_sequence.csv", "w",
                      newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(seq_rows)

        route_metrics.append({
            "method":     method_name,
            "theme":      theme_name,
            "genre":      genre_name,
            "novel":      novel_name,
            "curve":      curve_name,
            "route":      fp.stem,
            "v_as":       float(np.mean(np.abs(v_arr - 0.5))),
            "a_as":       float(np.mean(np.abs(a_arr - 0.5))),
            "v_hsp":      float(np.mean((v_arr > HIGH_THRESHOLD) | (v_arr < LOW_THRESHOLD)) * 100),
            "a_hsp":      float(np.mean((a_arr > HIGH_THRESHOLD) | (a_arr < LOW_THRESHOLD)) * 100),
        })

    return route_metrics


# Statistics 
def compute_group_stats(route_metrics):
    data = defaultdict(lambda: {"v_as": [], "a_as": [], "v_hsp": [], "a_hsp": []})
    for rm in route_metrics:
        m = rm["method"]
        for k in ("v_as", "a_as", "v_hsp", "a_hsp"):
            data[m][k].append(rm[k])
    return data


def run_rigorous_tests(data_grouped):
    rows = []
    avail = [m for m in METHODS if m in data_grouped and len(data_grouped[m]["v_as"]) >= 3]

    for metric_label, dict_key, _ in METRICS:
        # Omnibus Kruskal-Wallis 
        global_p = np.nan
        if len(avail) >= 2:
            arrays   = [np.array(data_grouped[m][dict_key]) for m in avail]
            all_vals = np.concatenate(arrays)
            if np.max(all_vals) == np.min(all_vals):
                global_p = 1.0
            else:
                try:
                    _, global_p = kruskal(*arrays)
                except ValueError:
                    pass
        global_sig = "Yes" if (not np.isnan(global_p) and global_p < 0.05) else "No"

        # 4 planned pairwise comparisons
        for m1, m2 in PLANNED_PAIRS:
            if m1 not in avail or m2 not in avail:
                continue
            arr1 = np.array(data_grouped[m1][dict_key])
            arr2 = np.array(data_grouped[m2][dict_key])

            mean1, mean2   = np.mean(arr1), np.mean(arr2)
            ci_l1, ci_u1   = compute_mean_ci(arr1)
            ci_l2, ci_u2   = compute_mean_ci(arr2)
            diff, d_lo, d_hi, cohen_d = compute_diff_ci(arr1, arr2)

            all_pair = np.concatenate((arr1, arr2))
            if np.max(all_pair) == np.min(all_pair):
                p_welch = p_mw = 1.0
                p_norm1 = p_norm2 = np.nan
                is_normal = True
            else:
                p_norm1   = check_normality(arr1)
                p_norm2   = check_normality(arr2)
                is_normal = (not np.isnan(p_norm1) and p_norm1 > 0.05 and
                             not np.isnan(p_norm2) and p_norm2 > 0.05)
                _, p_welch = ttest_ind(arr1, arr2, equal_var=False)
                _, p_mw    = mannwhitneyu(arr1, arr2, alternative="two-sided")

            test_used = "Welch's t" if is_normal else "Mann-Whitney U"
            final_p   = p_welch if is_normal else p_mw
            stars     = sig_stars(final_p)

            if final_p < 0.05:
                conclusion = (f"{m1} > {m2} ({stars})" if mean1 > mean2
                              else f"{m2} > {m1} ({stars})")
            else:
                conclusion = f"{m1} ≈ {m2} (ns)"

            rows.append([
                metric_label,
                fmt(global_p), global_sig,
                m1, m2, len(arr1), len(arr2),
                fmt(mean1), fmt(ci_l1), fmt(ci_u1),
                fmt(mean2), fmt(ci_l2), fmt(ci_u2),
                fmt(diff), fmt(d_lo), fmt(d_hi), fmt(cohen_d),
                fmt(p_norm1, 4) if not np.isnan(p_norm1) else "N/A",
                fmt(p_norm2, 4) if not np.isnan(p_norm2) else "N/A",
                fmt(p_welch, 6), fmt(p_mw, 6),
                test_used, fmt(final_p, 6), stars, conclusion,
            ])

    return rows


def save_summary_csv(data_grouped, out_dir):
    header = [
        "Method", "N_Routes",
        "Valence_AS_Mean", "Valence_AS_SD", "Valence_AS_CI_Low", "Valence_AS_CI_High",
        "Arousal_AS_Mean",  "Arousal_AS_SD",  "Arousal_AS_CI_Low",  "Arousal_AS_CI_High",
        "Valence_HSP_Mean", "Valence_HSP_CI_Low", "Valence_HSP_CI_High",
        "Arousal_HSP_Mean", "Arousal_HSP_CI_Low", "Arousal_HSP_CI_High",
    ]
    rows = [header]
    for m in METHODS:
        if m not in data_grouped: continue
        d = data_grouped[m]
        v_as_lo,  v_as_hi  = compute_mean_ci(d["v_as"])
        a_as_lo,  a_as_hi  = compute_mean_ci(d["a_as"])
        v_hsp_lo, v_hsp_hi = compute_mean_ci(d["v_hsp"])
        a_hsp_lo, a_hsp_hi = compute_mean_ci(d["a_hsp"])
        rows.append([
            m, len(d["v_as"]),
            fmt(np.mean(d["v_as"])), fmt(np.std(d["v_as"], ddof=1)),
            fmt(v_as_lo), fmt(v_as_hi),
            fmt(np.mean(d["a_as"])), fmt(np.std(d["a_as"], ddof=1)),
            fmt(a_as_lo), fmt(a_as_hi),
            f"{np.mean(d['v_hsp']):.1f}%", f"{v_hsp_lo:.1f}%", f"{v_hsp_hi:.1f}%",
            f"{np.mean(d['a_hsp']):.1f}%", f"{a_hsp_lo:.1f}%", f"{a_hsp_hi:.1f}%",
        ])
    with open(out_dir / "Statistics_Summary_CI95.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


# Plotting

def plot_bar(data_grouped, field, ylabel, title, filename, out_dir, is_pct=False):
    methods = [m for m in METHODS if m in data_grouped]
    if not methods: return

    values = [np.mean(data_grouped[m][field]) for m in methods]
    errors = []
    for m in methods:
        d = data_grouped[m][field]
        if len(d) < 2:
            errors.append(0)
        else:
            _, ci_hi = compute_mean_ci(d)
            errors.append(max(0, ci_hi - np.mean(d)))

    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots(figsize=(9, 5))
    colors  = [METHOD_COLORS[m] for m in methods]
    bars    = ax.bar(methods, values, yerr=errors, color=colors,
                     width=0.5, capsize=5, edgecolor="white")

    fmt_str = "{:.1f}%" if is_pct else "{:.4f}"
    for bar, val, err in zip(bars, values, errors):
        ax.text(bar.get_x() + bar.get_width() / 2,
                val + err + max(values) * 0.02,
                fmt_str.format(val),
                ha="center", va="bottom", fontweight="bold", fontsize=9)

    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontweight="bold", fontsize=11)
    ax.set_xticklabels(methods, rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / filename, dpi=300)
    plt.close()



# Curve ablation: line plot per method across Curve_1~6

CURVE_ORDER = [f"Curve_{i}" for i in range(1, 7)]

def run_curve_lineplot(route_metrics, out_dir):
    """
    For each of the 4 metrics, produce one line plot:
      x-axis  : Curve_1 … Curve_6
      y-axis  : mean AS or HSP
      4 lines : one per method (RAF_NoCritic, RAF_Critic, AVL_NoCritic, AVL_Critic)
    No statistical tests — purely descriptive.
    Also saves a summary CSV with mean ± SD per method × curve.
    """
    if not route_metrics: return
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build nested dict: data[method][curve] = {field: [values]}
    from collections import defaultdict as _dd
    data = _dd(lambda: _dd(lambda: {"v_as": [], "a_as": [], "v_hsp": [], "a_hsp": []}))
    for rm in route_metrics:
        for k in ("v_as", "a_as", "v_hsp", "a_hsp"):
            data[rm["method"]][rm["curve"]][k].append(rm[k])

    # Determine curve order present in data
    all_curves = sorted({rm["curve"] for rm in route_metrics},
                        key=lambda c: int(c.split("_")[1]) if c.split("_")[1].isdigit() else 99)

    # Summary CSV 
    header = ["Method", "Curve",
              "Valence_AS_Mean", "Valence_AS_SD",
              "Arousal_AS_Mean", "Arousal_AS_SD",
              "Valence_HSP_Mean", "Valence_HSP_SD",
              "Arousal_HSP_Mean", "Arousal_HSP_SD",
              "N_Routes"]
    rows = [header]
    for method in METHODS:
        for curve in all_curves:
            d = data[method][curve]
            if not d["v_as"]: continue
            rows.append([
                method, curve,
                fmt(np.mean(d["v_as"])),  fmt(np.std(d["v_as"],  ddof=1) if len(d["v_as"])  > 1 else 0),
                fmt(np.mean(d["a_as"])),  fmt(np.std(d["a_as"],  ddof=1) if len(d["a_as"])  > 1 else 0),
                fmt(np.mean(d["v_hsp"])), fmt(np.std(d["v_hsp"], ddof=1) if len(d["v_hsp"]) > 1 else 0),
                fmt(np.mean(d["a_hsp"])), fmt(np.std(d["a_hsp"], ddof=1) if len(d["a_hsp"]) > 1 else 0),
                len(d["v_as"]),
            ])
    with open(out_dir / "Curve_Ablation_Summary.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

    # Line plots
    plot_specs = [
        ("v_as",  "Valence Affective Salience (AS)",       "Line_Valence_AS.png",  False),
        ("a_as",  "Arousal Affective Salience (AS)",        "Line_Arousal_AS.png",  False),
        ("v_hsp", "Valence High-Salience Proportion (%)",   "Line_Valence_HSP.png", True),
        ("a_hsp", "Arousal High-Salience Proportion (%)",   "Line_Arousal_HSP.png", True),
    ]
    plt.style.use("seaborn-v0_8-darkgrid")
    for field, ylabel, fname, is_pct in plot_specs:
        fig, ax = plt.subplots(figsize=(10, 5))
        for method in METHODS:
            means, errs, xs = [], [], []
            for i, curve in enumerate(all_curves):
                vals = data[method][curve][field]
                if not vals: continue
                m = np.mean(vals)
                xs.append(i)
                means.append(m)
                ci_lo, ci_hi = compute_mean_ci(vals)
                errs.append(ci_hi - m if not np.isnan(ci_hi) else 0)
            if not xs: continue
            ax.errorbar(xs, means, yerr=errs,
                        label=method, color=METHOD_COLORS[method],
                        marker="o", linewidth=2, capsize=4)

        ax.set_xticks(range(len(all_curves)))
        ax.set_xticklabels(all_curves, rotation=15)
        ax.set_ylabel(ylabel + (" (%)" if is_pct else ""), fontsize=11)
        ax.set_title(f"{ylabel} across Curve Types", fontweight="bold", fontsize=11)
        ax.legend(loc="best", fontsize=9)
        plt.tight_layout()
        plt.savefig(out_dir / fname, dpi=300)
        plt.close()
        print(f"   [OK] {fname}")

    print(f"   [OK] Curve_Ablation_Summary.csv  ({len(rows)-1} rows)")


# Report per level

def run_level(route_metrics, out_dir, title_suffix=""):
    if not route_metrics: return
    out_dir.mkdir(parents=True, exist_ok=True)

    data_grouped = compute_group_stats(route_metrics)
    test_results = run_rigorous_tests(data_grouped)

    with open(out_dir / "Rigorous_Statistical_Tests_CI95.csv", "w",
              newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(STATS_CSV_HEADER)
        w.writerows(test_results)

    save_summary_csv(data_grouped, out_dir)

    plot_bar(data_grouped, "v_as",  "Valence Affective Salience (AS) [95% CI]",        f"Valence Affective Salience{title_suffix}",        "Bar_Valence_AS.png",   out_dir)
    plot_bar(data_grouped, "v_hsp", "Valence High-Salience Proportion (%) [95% CI]",   f"Valence High-Salience Proportion{title_suffix}",  "Bar_Valence_HSP.png",  out_dir, True)
    plot_bar(data_grouped, "a_as",  "Arousal Affective Salience (AS) [95% CI]",        f"Arousal Affective Salience{title_suffix}",        "Bar_Arousal_AS.png",   out_dir)
    plot_bar(data_grouped, "a_hsp", "Arousal High-Salience Proportion (%) [95% CI]",   f"Arousal High-Salience Proportion{title_suffix}",  "Bar_Arousal_HSP.png",  out_dir, True)


# Main

def main():
    parser = argparse.ArgumentParser(
        description="eval_as.py — 2x2 Factorial Emotion Analysis (AS / HSP)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Directory layout expected under --results_dir:
  <method>/results/<Theme>/<Genre>/World_Curve_X_Story_Y/Story_Routes/Route_*.txt

Methods recognised: RAF_NoCritic, RAF_Critic, AVL_NoCritic, AVL_Critic

Examples:
  python eval_as.py -r story_outputs -o eval_as
        """)
    parser.add_argument("--results_dir", "-r", required=True,
                        help="Root folder containing method sub-directories")
    parser.add_argument("--output_dir",  "-o", required=True,
                        help="Where to write all reports and figures")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL_PATH,
                        help="HuggingFace model path for emotion classification")
    args = parser.parse_args()

    base_path = Path(args.results_dir).resolve()
    out_root  = Path(args.output_dir).resolve()

    tokenizer, model, device = load_model(args.model)
    if not model:
        return

    store = defaultdict(list)

    out_root.mkdir(parents=True, exist_ok=True)

    route_dirs = list(base_path.rglob("Story_Routes"))
    print(f"[Debug] base_path = {base_path}")
    print(f"[Debug] Found {len(route_dirs)} Story_Routes directories")
    if route_dirs:
        print("[Debug] First 3 examples:")
        for rd in route_dirs[:3]:
            print(f"         {rd}")
    it = tqdm(route_dirs, desc="Processing case dirs") if tqdm else route_dirs

    for rd in it:
        rm = collect_case_data(rd.parent, tokenizer, model, device, base_path, out_root)
        if not rm:
            print(f"   [Debug] No routes collected from: {rd.parent}")
            continue

        method = rm[0]["method"]
        theme  = rm[0]["theme"]
        genre  = rm[0]["genre"]

        if method not in METHODS:
            print(f"   [Skip] Unrecognised method folder: {rd.parent.name} (mapped: {method})")
            continue

        store["all"].extend(rm)


    if not any(store.values()):
        print("\n[Warning] No data collected — check --results_dir path and method folder names.")
        return

    print("\nGenerating reports...")

    for key, metrics in store.items():
        if not metrics:
            continue
        if key == "all":
            run_level(metrics, out_root / "All_Methods", " (All Methods)")

    # Master route metrics CSV
    all_metrics = store.get("all", [])
    if all_metrics:
        master = out_root / "MASTER_ROUTE_METRICS.csv"
        with open(master, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["method", "theme", "genre", "novel", "curve", "route",
                          "v_as", "a_as", "v_hsp", "a_hsp"]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(all_metrics)
        print(f"   [OK] MASTER_ROUTE_METRICS.csv  ({len(all_metrics)} routes)")

        # Novel-level summary: mean of all routes within each method × novel
        from collections import defaultdict as _dd
        novel_data = _dd(lambda: {"v_as": [], "a_as": [], "v_hsp": [], "a_hsp": []})
        for rm in all_metrics:
            key = (rm["method"], rm["theme"], rm["genre"], rm["novel"], rm["curve"])
            for k in ("v_as", "a_as", "v_hsp", "a_hsp"):
                novel_data[key][k].append(rm[k])

        novel_rows = [["method", "theme", "genre", "novel", "curve",
                       "v_as_mean", "a_as_mean", "v_hsp_mean", "a_hsp_mean", "n_routes"]]
        for (method, theme, genre, novel, curve), d in sorted(novel_data.items()):
            novel_rows.append([
                method, theme, genre, novel, curve,
                fmt(np.mean(d["v_as"])),  fmt(np.mean(d["a_as"])),
                fmt(np.mean(d["v_hsp"])), fmt(np.mean(d["a_hsp"])),
                len(d["v_as"]),
            ])
        with open(out_root / "NOVEL_METRICS.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(novel_rows)
        print(f"   [OK] NOVEL_METRICS.csv  ({len(novel_rows)-1} novels)")

    print(f"\n[Done] All outputs saved to: {out_root}")
    print(f"[Done] Absolute path: {out_root.resolve()}")
    print("Output structure:")
    print("  All_Methods/   — overall comparison across all 4 methods")
    print("  Each folder: Rigorous_Statistical_Tests_CI95.csv + Statistics_Summary_CI95.csv + 4 bar charts")


if __name__ == "__main__":
    main()