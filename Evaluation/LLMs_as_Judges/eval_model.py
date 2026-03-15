import os
import pandas as pd
import numpy as np
import argparse


# Configuration
ROOT_REPORT_DIR = os.path.join("Paper_Results", "02_Reports")
OUTPUT_DIR      = os.path.join("Paper_Results", "03_Cross_Model_Summary")

STATS_REPORTS = [
    "Theme_Stats_Adaptive_Top3.csv",
    "Genre_Stats_Adaptive_Top3.csv",
    "Theme_Stats_Adaptive_AllMean.csv",
    "Genre_Stats_Adaptive_AllMean.csv",
    "Curve_Stats_Adaptive_Top3.csv",
    "Curve_Stats_Adaptive_AllMean.csv",
]

SCORES_REPORTS = [
    "Group_Scores_Theme_Top3.csv",
    "Group_Scores_Genre_Top3.csv",
    "Group_Scores_Theme_AllMean.csv",
    "Group_Scores_Genre_AllMean.csv",
    "Group_Scores_Curve_Top3.csv",
    "Group_Scores_Curve_AllMean.csv",
    "Novel_Scores_Top3.csv",
    "Novel_Scores_AllMean.csv",
]

REPORT_METRICS = ["RE", "CH", "EM", "SU", "EG", "CX", "OV"]

METRIC_SORT_WEIGHTS = {
    "RE": 1, "CH": 2, "EM": 3, "SU": 4, "EG": 5, "CX": 6, "OV": 7, "Count": 8
}

FOOTER_STATS = [
    "",
    "--- STATISTICAL SIGNIFICANCE NOTES ---",
    "Note: Statistical tests were conducted across all specified metrics (RE, CH, EM, SU, EG, CX, OV).",
    "(*): p < 0.05, (**): p < 0.01, (***): p < 0.001",
    "(ns): Not significant (p >= 0.05)",
    "If p=0, it is formatted as <0.001 for academic compliance."
]

FOOTER_METRICS = [
    "",
    "--- METRIC DEFINITIONS ---",
    "RE(Relevance), CH(Coherence), EM(Empathy), SU(Surprise), EG(Engagement), CX(Complexity), OV(Overall)",
    "Count(the total number of successfully evaluated story routes)"
]



# Utility

def safe_model_name(model: str) -> str:
    return model.replace(":", "_").replace("/", "_")


def model_report_dir(model: str) -> str:
    """
    Looks for the per-model report folder under 02_Reports.
    Accepts both Model_<safe> (new) and Evaluator_<safe> (legacy) naming.
    """
    sm = safe_model_name(model)
    for candidate in [f"Model_{sm}", f"Evaluator_{sm}", sm]:
        path = os.path.join(ROOT_REPORT_DIR, candidate)
        if os.path.exists(path):
            return path
    # Return the preferred new-style path even if it doesn't exist yet
    return os.path.join(ROOT_REPORT_DIR, f"Model_{sm}")


def format_mean_sd(m, s):
    if pd.isna(m): return "-"
    if pd.isna(s): return f"{m:.2f} ± -"
    return f"{m:.2f} ± {s:.2f}"


def format_p_value(p, sig_mark=""):
    if pd.isna(p) or p == "-": return "-"
    try:
        p_val = float(p)
        if p_val < 0.001:
            return f"<0.001 {sig_mark}".strip()
        return f"{p_val:.4f} {sig_mark}".strip()
    except:
        return str(p)


def determine_winner_raw(m_a, m_b, val_a, val_b, p_val):
    if pd.isna(val_a) or pd.isna(val_b) or pd.isna(p_val):
        return "-"
    is_sig = p_val < 0.05
    if is_sig:
        return f"{m_a} significantly better (*)" if val_a > val_b \
               else f"{m_b} significantly better (*)"
    if val_a > val_b:   return f"{m_a} higher (ns)"
    elif val_b > val_a: return f"{m_b} higher (ns)"
    else:               return "Tie (ns)"


def append_footer_to_csv(filepath, footer_lines):
    with open(filepath, "a", encoding="utf-8-sig") as f:
        for line in footer_lines:
            f.write(f'"{line}"\n')



# Stats splitting: Omnibus + Pairwise

def extract_stats_split(df):
    omni_rows = []
    pair_rows = []

    for _, row in df.iterrows():
        base_info = {"Judge_Model": row.get("Judge_Model", "")}
        for key_col in ["Theme", "Genre", "Curve_Type", "Method"]:
            if key_col in row: base_info[key_col] = row[key_col]

        for metric in REPORT_METRICS:
            # Omnibus 
            omni_test  = row.get(f"{metric}_Omnibus_Test", "-")
            omni_p_val = row.get(f"{metric}_Omnibus_p",    np.nan)
            omni_sig   = row.get(f"{metric}_Omnibus_Sig",  "")

            if pd.notna(omni_p_val) and omni_test not in ("-", "N/A", np.nan):
                is_sig     = isinstance(omni_p_val, (int, float)) and omni_p_val < 0.05
                omni_conc  = ("Significant variance among groups (*)" if is_sig
                              else "Groups are comparable overall (ns)")
                omni_rows.append({
                    **base_info,
                    "Metric":            metric,
                    "Global_Test_Type":  omni_test,
                    "Global_p_value":    format_p_value(omni_p_val, omni_sig),
                    "Global_Conclusion": omni_conc,
                })

            # Pairwise
            pair_prefixes = [
                col.replace("_p_raw", "")
                for col in df.columns
                if col.endswith("_p_raw") and col.startswith(f"{metric}_")
            ]

            for prefix in pair_prefixes:
                pair_str = prefix[len(metric) + 1:]
                try:
                    m_a, m_b = pair_str.split("_vs_")
                except ValueError:
                    continue

                mean_a = row.get(f"{metric}_Mean_{m_a}", np.nan)
                sd_a   = row.get(f"{metric}_SD_{m_a}",   np.nan)
                mean_b = row.get(f"{metric}_Mean_{m_b}", np.nan)
                sd_b   = row.get(f"{metric}_SD_{m_b}",   np.nan)
                p_raw  = row.get(f"{prefix}_p_raw",      np.nan)
                sig_raw = row.get(f"{prefix}_Sig_raw",   "")

                pair_rows.append({
                    **base_info,
                    "Metric":      metric,
                    "Comparison":  f"{m_a} vs {m_b}",
                    "N (A/B)":     f"{row.get(f'{metric}_N_{m_a}', '-')} vs "
                                   f"{row.get(f'{metric}_N_{m_b}', '-')}",
                    "Mean±SD (A)": format_mean_sd(mean_a, sd_a),
                    "Mean±SD (B)": format_mean_sd(mean_b, sd_b),
                    "Test_Type":   row.get(f"{prefix}_Test", "-"),
                    "Pairwise_p":  format_p_value(p_raw, sig_raw),
                    "Conclusion":  determine_winner_raw(m_a, m_b, mean_a, mean_b, p_raw),
                })

    return pd.DataFrame(omni_rows), pd.DataFrame(pair_rows)



# Process stats reports

def process_stats_reports(models):
    print("\n--- Processing Statistical Reports ---")
    for report in STATS_REPORTS:
        combined_wide = []
        for model in models:
            file_path = os.path.join(model_report_dir(model), report)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df.insert(0, "Judge_Model", model)
                combined_wide.append(df)
                print(f"   [Loaded] {model} / {report}")
            else:
                print(f"   [Missing] {file_path}")

        if not combined_wide:
            continue

        full_df = pd.concat(combined_wide, ignore_index=True)
        df_omni, df_pair = extract_stats_split(full_df)

        # Sort keys
        sort_base = [c for c in ["Theme", "Genre", "Curve_Type", "Method"]
                     if c in full_df.columns]

        for df_out, label in [(df_omni, "Omnibus"), (df_pair, "Pairwise")]:
            if df_out.empty:
                continue
            df_out["_mw"] = df_out["Metric"].map(lambda x: METRIC_SORT_WEIGHTS.get(x, 99))
            sort_cols = [c for c in sort_base if c in df_out.columns]
            sort_cols += ["_mw", "Judge_Model"]
            if label == "Pairwise" and "Comparison" in df_out.columns:
                sort_cols.insert(-1, "Comparison")
            df_out.sort_values(by=sort_cols, inplace=True)
            df_out.drop(columns=["_mw"], inplace=True)
            df_out.reset_index(drop=True, inplace=True)

            out_path = os.path.join(OUTPUT_DIR, f"CrossModel_{label}_{report}")
            df_out.to_csv(out_path, index=False, encoding="utf-8-sig")
            append_footer_to_csv(out_path, FOOTER_STATS)
            print(f"   [OK] CrossModel_{label}_{report}  ({len(df_out)} rows)")



# Process scores reports

def process_scores_reports(models):
    print("\n--- Processing Dimensional & Novel Scores ---")
    for report in SCORES_REPORTS:
        combined_rows = []
        for model in models:
            file_path = os.path.join(model_report_dir(model), report)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df.insert(0, "Judge_Model", model)
                combined_rows.append(df)

        if not combined_rows:
            continue

        combined_df = pd.concat(combined_rows, ignore_index=True)

        sort_cols = [c for c in ["Theme", "Genre", "Curve_Type"] if c in combined_df.columns]
        if "Metric" in combined_df.columns:
            combined_df["_mw"] = combined_df["Metric"].map(
                lambda x: METRIC_SORT_WEIGHTS.get(x, 99))
            sort_cols.append("_mw")
        sort_cols.append("Judge_Model")

        valid = [c for c in sort_cols if c in combined_df.columns]
        if valid:
            combined_df.sort_values(by=valid, inplace=True)
            combined_df.reset_index(drop=True, inplace=True)
        if "_mw" in combined_df.columns:
            combined_df.drop(columns=["_mw"], inplace=True)

        out_path = os.path.join(OUTPUT_DIR, f"CrossModel_{report}")
        combined_df.to_csv(out_path, index=False, encoding="utf-8-sig")
        append_footer_to_csv(out_path, FOOTER_METRICS)
        print(f"   [OK] CrossModel_{report}  ({len(combined_df)} rows)")



# Factorial 2x2 — vertical summary

FACTORIAL_TAGS = ["Top3", "AllMean"]

# Effect blocks to extract: (prefix in CSV, readable label)
FACTORIAL_EFFECTS = [
    ("MainEffect_A_Curve",          "Main Effect A (Curve: RAF vs AVL)"),
    ("MainEffect_B_Critic",         "Main Effect B (Critic: No vs With)"),
    ("SimpleEffect_Critic_at_RAF",  "Simple Effect: Critic @ RAF"),
    ("SimpleEffect_Critic_at_AVL",  "Simple Effect: Critic @ AVL"),
    ("SimpleEffect_Curve_NoCritic", "Simple Effect: Curve @ No_Critic"),
    ("SimpleEffect_Curve_Critic",   "Simple Effect: Curve @ With_Critic"),
]

FACTORIAL_CELL_COLS = [
    ("Cell_RAF_NoCritic_N",    "RAF_NoCritic N"),
    ("Cell_RAF_NoCritic_Mean", "RAF_NoCritic Mean"),
    ("Cell_RAF_Critic_N",      "RAF_Critic N"),
    ("Cell_RAF_Critic_Mean",   "RAF_Critic Mean"),
    ("Cell_AVL_NoCritic_N",    "AVL_NoCritic N"),
    ("Cell_AVL_NoCritic_Mean", "AVL_NoCritic Mean"),
    ("Cell_AVL_Critic_N",      "AVL_Critic N"),
    ("Cell_AVL_Critic_Mean",   "AVL_Critic Mean"),
    ("Marginal_RAF_Mean",      "Marginal RAF Mean"),
    ("Marginal_AVL_Mean",      "Marginal AVL Mean"),
    ("Marginal_NoCritic_Mean", "Marginal NoCritic Mean"),
    ("Marginal_Critic_Mean",   "Marginal Critic Mean"),
    ("Interaction_Gain_RAF",   "Critic Gain in RAF"),
    ("Interaction_Gain_AVL",   "Critic Gain in AVL"),
    ("Interaction_Delta",      "Interaction Delta (RAF−AVL)"),
    ("Interaction_Direction",  "Interaction Direction"),
]

FOOTER_FACTORIAL = [
    "",
    "--- FACTORIAL 2x2 NOTES ---",
    "Factor A (Curve): RAF = Rise-and-Fall curve; AVL = A-V-A levels curve.",
    "Factor B (Critic): No_Critic = without critic feedback; With_Critic = with critic feedback.",
    "Main Effects: marginal means collapsing across the other factor.",
    "Simple Effects: pairwise comparison within one level of the other factor.",
    "Interaction Delta = Critic gain in RAF minus Critic gain in AVL.",
    "All pairwise comparisons are pre-planned; no correction applied.",
    "Test selected per pair: Welch's t (both groups normal via Shapiro-Wilk) or Mann-Whitney U.",
    "(*): p < 0.05, (**): p < 0.01, (***): p < 0.001  |  (ns): p >= 0.05",
]


def process_factorial(models):
    print("\n--- Processing Factorial 2x2 Reports ---")
    for tag in FACTORIAL_TAGS:
        fname = f"Factorial_2x2_{tag}.csv"
        combined = []
        for model in models:
            file_path = os.path.join(model_report_dir(model), fname)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df.insert(0, "Judge_Model", model)
                combined.append(df)
                print(f"   [Loaded] {model} / {fname}")
            else:
                print(f"   [Missing] {file_path}")

        if not combined:
            continue

        full_df = pd.concat(combined, ignore_index=True)
        rows = []

        for _, row in full_df.iterrows():
            judge  = row.get("Judge_Model", "")
            metric = row.get("Metric", "")

            def fmt(v, decimals=4):
                return round(float(v), decimals) if pd.notna(v) else "-"

            # Cell means embedded as fixed columns in every effect row
            shared = {
                "RAF_NoCritic (N/Mean)": f"{fmt(row.get('Cell_RAF_NoCritic_N', np.nan), 0)} / {fmt(row.get('Cell_RAF_NoCritic_Mean', np.nan))}",
                "RAF_Critic (N/Mean)":   f"{fmt(row.get('Cell_RAF_Critic_N',   np.nan), 0)} / {fmt(row.get('Cell_RAF_Critic_Mean',   np.nan))}",
                "AVL_NoCritic (N/Mean)": f"{fmt(row.get('Cell_AVL_NoCritic_N', np.nan), 0)} / {fmt(row.get('Cell_AVL_NoCritic_Mean', np.nan))}",
                "AVL_Critic (N/Mean)":   f"{fmt(row.get('Cell_AVL_Critic_N',   np.nan), 0)} / {fmt(row.get('Cell_AVL_Critic_Mean',   np.nan))}",
                "Interaction_Delta":     fmt(row.get("Interaction_Delta",     np.nan)),
                "Interaction_Direction": row.get("Interaction_Direction", "-") or "-",
            }

            # One row per effect
            for prefix, effect_label in FACTORIAL_EFFECTS:
                test      = row.get(f"{prefix}_Test",       "-")
                sw_a      = row.get(f"{prefix}_SW_p_A",     np.nan)
                sw_b      = row.get(f"{prefix}_SW_p_B",     np.nan)
                stat      = row.get(f"{prefix}_Stat",       np.nan)
                mean_d    = row.get(f"{prefix}_Mean_Diff",  np.nan)
                ci_lo     = row.get(f"{prefix}_CI95_Lower", np.nan)
                ci_hi     = row.get(f"{prefix}_CI95_Upper", np.nan)
                cohen_d   = row.get(f"{prefix}_Cohen_d",    np.nan)
                p_raw_v   = row.get(f"{prefix}_p_raw",      np.nan)
                sig_raw_v = row.get(f"{prefix}_Sig_raw",    "")

                if pd.notna(p_raw_v) and pd.notna(mean_d):
                    direction = "A > B" if float(mean_d) > 0 else ("A < B" if float(mean_d) < 0 else "A = B")
                    conclusion = f"{direction} ({sig_raw_v if sig_raw_v else 'ns'})"
                else:
                    conclusion = "-"

                rows.append({
                    "Judge_Model": judge,
                    "Metric":      metric,
                    "Effect":      effect_label,
                    **shared,
                    "Mean_Diff":   fmt(mean_d),
                    "CI95":        (f"[{ci_lo:.4f}, {ci_hi:.4f}]" if pd.notna(ci_lo) and pd.notna(ci_hi) else "-"),
                    "Cohen_d":     fmt(cohen_d),
                    "Test_Used":   test,
                    "SW_p_A":      fmt(sw_a),
                    "SW_p_B":      fmt(sw_b),
                    "Statistic":   fmt(stat),
                    "p_raw":       format_p_value(p_raw_v, sig_raw_v),
                    "Conclusion":  conclusion,
                })

        if not rows:
            continue

        out_df = pd.DataFrame(rows)
        out_df["_mw"] = out_df["Metric"].map(lambda x: METRIC_SORT_WEIGHTS.get(x, 99))
        EFFECT_ORDER = {e: i for i, (_, e) in enumerate(FACTORIAL_EFFECTS)}
        out_df["_eo"] = out_df["Effect"].map(lambda x: EFFECT_ORDER.get(x, 99))
        out_df.sort_values(by=["Judge_Model", "_mw", "_eo"], inplace=True)
        out_df.drop(columns=["_mw", "_eo"], inplace=True)
        out_df.reset_index(drop=True, inplace=True)

        out_path = os.path.join(OUTPUT_DIR, f"CrossModel_Factorial_2x2_{tag}.csv")
        out_df.to_csv(out_path, index=False, encoding="utf-8-sig")
        append_footer_to_csv(out_path, FOOTER_FACTORIAL)
        print(f"   [OK] CrossModel_Factorial_2x2_{tag}.csv  ({len(out_df)} rows)")



# Route count tables

def extract_route_counts(models):
    print("\n--- Extracting Dataset Route Counts ---")
    all_dfs = []
    for model in models:
        file_path = os.path.join(model_report_dir(model), "Novel_Scores_AllMean.csv")
        if os.path.exists(file_path):
            all_dfs.append(pd.read_csv(file_path))

    if not all_dfs:
        print("   [Warning] No Novel_Scores_AllMean.csv found for any model.")
        return

    combined_df  = pd.concat(all_dfs, ignore_index=True)
    base_cols    = [c for c in ["Theme", "Genre", "Curve_Type", "Novel"]
                    if c in combined_df.columns]
    count_cols   = [c for c in combined_df.columns if str(c).endswith("_Count")]
    if not count_cols:
        return

    novel_df     = combined_df.groupby(base_cols, as_index=False)[count_cols].max()
    rename_map   = {c: f"{c.replace('_Count', '')} (Routes)" for c in count_cols}

    level_groups = [
        ("Novel",      base_cols,                  "Dataset_Route_Count_Novel.csv"),
        ("Genre",      ["Theme", "Genre"],          "Dataset_Route_Count_Genre.csv"),
        ("Theme",      ["Theme"],                   "Dataset_Route_Count_Theme.csv"),
        ("Curve_Type", ["Curve_Type"],              "Dataset_Route_Count_Curve.csv"),
    ]

    for label, group_cols, fname in level_groups:
        gc = [c for c in group_cols if c in novel_df.columns]
        if not gc:
            continue
        agg  = novel_df.groupby(gc, as_index=False)[count_cols].sum()
        agg  = agg.rename(columns=rename_map).sort_values(gc).reset_index(drop=True)
        if label == "Novel" and "Novel" in agg.columns:
            agg.rename(columns={"Novel": "Novel (Case)"}, inplace=True)
        out  = os.path.join(OUTPUT_DIR, fname)
        agg.to_csv(out, index=False, encoding="utf-8-sig")
        print(f"   [OK] {fname}  ({len(agg)} rows)")


# Main

def main():
    parser = argparse.ArgumentParser(
        description="eval_crossmodel.py — Vertical cross-model summary tables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python eval_model.py --models qwen3:14b-fp16 mistral:7b-instruct-v0.3-fp16 gemma3:12b-it-fp16
        """)
    parser.add_argument("--models", nargs="+", required=True,
                        help="Model names exactly as used in eval_runner.py")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("=" * 60)
    print(f"eval_crossmodel  |  Models: {args.models}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)

    process_stats_reports(args.models)
    process_scores_reports(args.models)
    process_factorial(args.models)
    extract_route_counts(args.models)

    print(f"\n[Done] All cross-model summaries saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()