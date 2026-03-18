"""
eval_stats.py — Statistical Analysis Script
============================================
Reads score CSVs and generates full statistical reports.

Produces reports under Paper_Results/02_Reports/<report_tag>/:
  Novel_Scores_Top3.csv / Novel_Scores_AllMean.csv
  Group_Scores_Theme/Genre/Curve_*.csv
  Theme_Stats_Adaptive_*.csv  /  Genre_Stats_Adaptive_*.csv
  Curve_Stats_Adaptive_*.csv
  Factorial_2x2_*.csv

Usage:
  # Report from a single evaluator model's scores
  python eval_stats.py --source model --model qwen3:14b-fp16

  # Report from all 3 models independently (3 separate report folders)
  python eval_stats.py --source all-models --models qwen3:14b-fp16 mistral:7b-instruct-v0.3-fp16 gemma3:12b-it-fp16
"""

import os
import argparse

import numpy as np
import pandas as pd
from scipy import stats as scipy_stats
from itertools import combinations
import statsmodels.formula.api as smf
import statsmodels.api as sm
import re



# Shared Configuration (must match eval_runner.py)
ROOT_OUTPUT_DIR = "Paper_Results"
RAW_DIR         = os.path.join(ROOT_OUTPUT_DIR, "01_Raw_Evaluations")
REPORTS_DIR     = os.path.join(ROOT_OUTPUT_DIR, "02_Reports")

DEFAULT_METHODS = ["RAF_NoCritic", "RAF_Critic", "AVL_NoCritic", "AVL_Critic"]

FACTORIAL_META = {
    "RAF_NoCritic": {"curve_strategy": "RAF", "critic": "No_Critic"},
    "RAF_Critic":   {"curve_strategy": "RAF", "critic": "With_Critic"},
    "AVL_NoCritic": {"curve_strategy": "AVL", "critic": "No_Critic"},
    "AVL_Critic":   {"curve_strategy": "AVL", "critic": "With_Critic"},
}

# Planned pairwise comparisons (no correction — pre-planned)
COMPARISON_PAIRS = [
    ("RAF_NoCritic", "RAF_Critic"),    # Critic effect @ RAF
    ("AVL_NoCritic", "AVL_Critic"),    # Critic effect @ AVL
    ("RAF_NoCritic", "AVL_NoCritic"),  # Curve  effect @ No_Critic
    ("RAF_Critic",   "AVL_Critic"),    # Curve  effect @ With_Critic
]

METRICS_CODES  = ["RE", "CH", "EM", "SU", "EG", "CX"]
REPORT_METRICS = METRICS_CODES + ["OV"]

NAME_ALIASES = {
    "Sci_Fi": "SciFi", "Scifi": "SciFi",
    "Sci_fi": "SciFi", "Science_Fiction": "SciFi",
}

TOP_K = 3



def clean_name(s):
    return " ".join(s.replace("_", " ").replace("-", " ").split()).title().replace(" ", "_")


def natural_keys(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', str(text))]


def safe_model_name(model: str) -> str:
    return model.replace(":", "_").replace("/", "_")


def extract_curve_type(novel_name: str) -> str:
    import re
    m = re.search(r'(Curve_\d+)', str(novel_name), re.IGNORECASE)
    return m.group(1).title() if m else str(novel_name)


def extract_story_id(novel_name: str) -> str:
    import re
    m = re.search(r'(Story_\d+)', str(novel_name), re.IGNORECASE)
    return m.group(1).title() if m else "Story_1"


def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in ["Theme", "Genre", "Novel"]:
        if col in df.columns:
            df[col] = df[col].astype(str).apply(clean_name)
            df[col] = df[col].map(lambda s: NAME_ALIASES.get(s, s))
    if "Novel" in df.columns:
        df["Curve_Type"] = df["Novel"].apply(extract_curve_type)
        df["Story_ID"]   = df["Novel"].apply(extract_story_id)
    for metric in REPORT_METRICS:
        col = f"{metric}_Score"
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df




def get_sig_asterisks(p_value: float) -> str:
    if np.isnan(p_value): return ""
    if p_value < 0.001:   return "***"
    elif p_value < 0.01:  return "**"
    elif p_value < 0.05:  return "*"
    return ""


def check_normality(data) -> bool:
    if len(data) < 3 or np.max(data) == np.min(data):
        return False
    return scipy_stats.shapiro(data)[1] > 0.05


def shapiro_wilk_p(data) -> float:
    data = [x for x in data if not np.isnan(x)]
    if len(data) < 3 or len(data) > 5000 or np.max(data) == np.min(data):
        return np.nan
    return round(float(scipy_stats.shapiro(data)[1]), 4)


def compute_mean_ci(data, confidence=0.95):
    n = len(data)
    if n < 2: return np.nan, np.nan
    se = scipy_stats.sem(data)
    if se == 0: return np.mean(data), np.mean(data)
    h = se * scipy_stats.t.ppf((1 + confidence) / 2., n - 1)
    m = np.mean(data)
    return m - h, m + h


def compute_diff_ci(a, b, confidence=0.95):
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2: return np.nan, np.nan, np.nan, np.nan
    v1, v2 = np.var(a, ddof=1), np.var(b, ddof=1)
    diff = np.mean(a) - np.mean(b)
    se   = np.sqrt(v1/n1 + v2/n2)
    if se == 0: return diff, diff, diff, 0.0
    df_w   = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))
    margin = scipy_stats.t.ppf((1+confidence)/2., df_w) * se
    s_pool = np.sqrt(((n1-1)*v1 + (n2-1)*v2) / (n1+n2-2))
    d      = diff / s_pool if s_pool != 0 else 0.0
    return diff, diff-margin, diff+margin, d


def run_adaptive_pairwise(a: list, b: list) -> dict:
    """
    Normality via Shapiro-Wilk:
      Both normal       -> Welch's t (never assumes equal variance)
      Either non-normal -> Mann-Whitney U
    No correction applied — comparisons are pre-planned.
    """
    a = [x for x in a if not np.isnan(x)]
    b = [x for x in b if not np.isnan(x)]
    result = {
        "Test_Used": "N/A", "SW_p_A": np.nan, "SW_p_B": np.nan,
        "Statistic": np.nan, "p_raw": np.nan,
        "Sig_raw": "",
        "Mean_Diff": np.nan, "CI95_Lower": np.nan,
        "CI95_Upper": np.nan, "Cohen_d": np.nan,
    }
    if len(a) < 3 or len(b) < 3:
        result["Test_Used"] = "N/A (N<3)"; return result

    sw_a = shapiro_wilk_p(a); sw_b = shapiro_wilk_p(b)
    result["SW_p_A"] = sw_a;  result["SW_p_B"] = sw_b

    if check_normality(a) and check_normality(b):
        stat, p_raw = scipy_stats.ttest_ind(a, b, equal_var=False)
        result["Test_Used"] = "Welch's t"
    else:
        stat, p_raw = scipy_stats.mannwhitneyu(a, b, alternative="two-sided")
        result["Test_Used"] = "Mann-Whitney U"

    diff, ci_low, ci_high, cohen_d = compute_diff_ci(a, b)
    result.update({
        "Statistic":  round(stat, 4),
        "p_raw":      round(p_raw, 4),
        "Sig_raw":    get_sig_asterisks(p_raw),
        "Mean_Diff":  round(diff, 4),
        "CI95_Lower": round(ci_low, 4), "CI95_Upper": round(ci_high, 4),
        "Cohen_d":    round(cohen_d, 4),
    })
    return result


def run_two_way_omnibus(data: dict, metric_col: str) -> dict:
    """
    Two-Way ANOVA (normal residuals) or Scheirer-Ray-Hare (non-normal).
    data: {method_name: [scores]}
    """
    cell_map = {m: FACTORIAL_META[m] for m in FACTORIAL_META if m in data}
    rows = []
    for method, meta in cell_map.items():
        for score in data.get(method, []):
            if not np.isnan(score):
                rows.append({"score": score,
                             "Curve":  meta["curve_strategy"],
                             "Critic": meta["critic"]})
    empty = {
        "Omnibus_Test": "N/A", "Omnibus_SW_resid_p": np.nan,
        "Omnibus_A_Curve_Stat": np.nan,  "Omnibus_A_Curve_p": np.nan,
        "Omnibus_A_Curve_Sig":  "",      "Omnibus_A_Curve_ES": np.nan,
        "Omnibus_B_Critic_Stat": np.nan, "Omnibus_B_Critic_p": np.nan,
        "Omnibus_B_Critic_Sig":  "",     "Omnibus_B_Critic_ES": np.nan,
        "Omnibus_AxB_Stat": np.nan,      "Omnibus_AxB_p": np.nan,
        "Omnibus_AxB_Sig":  "",          "Omnibus_AxB_ES": np.nan,
    }
    if len(rows) < 8:
        empty["Omnibus_Test"] = "N/A (insufficient data)"; return empty

    df = pd.DataFrame(rows)
    try:
        ols   = smf.ols("score ~ C(Curve) * C(Critic)", data=df).fit()
        resids = ols.resid.tolist()
        sw_p   = shapiro_wilk_p(resids)
        use_p  = (not np.isnan(sw_p)) and sw_p > 0.05
    except Exception:
        sw_p = np.nan; use_p = False

    result = {"Omnibus_SW_resid_p": sw_p}

    if use_p:
        try:
            tbl      = sm.stats.anova_lm(ols, typ=2)
            ss_total = tbl["sum_sq"].sum()
            def _f(t):  return round(float(tbl.loc[t,"F"]),      4) if t in tbl.index else np.nan
            def _p(t):  return round(float(tbl.loc[t,"PR(>F)"]), 4) if t in tbl.index else np.nan
            def _e2(t):
                ss = float(tbl.loc[t,"sum_sq"]) if t in tbl.index else np.nan
                return round(ss/ss_total, 4) if (not np.isnan(ss) and ss_total>0) else np.nan
            result.update({
                "Omnibus_Test":          "Two-Way ANOVA (Type II SS)",
                "Omnibus_A_Curve_Stat":  _f("C(Curve)"),
                "Omnibus_A_Curve_p":     _p("C(Curve)"),
                "Omnibus_A_Curve_Sig":   get_sig_asterisks(_p("C(Curve)")),
                "Omnibus_A_Curve_ES":    _e2("C(Curve)"),
                "Omnibus_B_Critic_Stat": _f("C(Critic)"),
                "Omnibus_B_Critic_p":    _p("C(Critic)"),
                "Omnibus_B_Critic_Sig":  get_sig_asterisks(_p("C(Critic)")),
                "Omnibus_B_Critic_ES":   _e2("C(Critic)"),
                "Omnibus_AxB_Stat":      _f("C(Curve):C(Critic)"),
                "Omnibus_AxB_p":         _p("C(Curve):C(Critic)"),
                "Omnibus_AxB_Sig":       get_sig_asterisks(_p("C(Curve):C(Critic)")),
                "Omnibus_AxB_ES":        _e2("C(Curve):C(Critic)"),
            })
        except Exception as e:
            result.update({**empty, "Omnibus_Test": f"ANOVA error: {e}",
                           "Omnibus_SW_resid_p": sw_p})
    else:
        df["rank"] = scipy_stats.rankdata(df["score"])
        ss_r = df["rank"].var(ddof=0) * len(df)
        def srh(col):
            groups = [g["rank"].tolist() for _,g in df.groupby(col) if len(g)>=2]
            if len(groups)<2: return np.nan, np.nan, np.nan
            all_vals = [v for g in groups for v in g]
            if len(set(all_vals)) <= 1: return 0.0, 1.0, 0.0
            try:
                h,p = scipy_stats.kruskal(*groups)
            except ValueError:
                return np.nan, np.nan, np.nan
            return round(h,4), round(p,4), round(h/ss_r,4) if ss_r>0 else np.nan
        h_c,p_c,e_c = srh("Curve"); h_r,p_r,e_r = srh("Critic")
        # approximate interaction
        try:
            h_all,_ = scipy_stats.kruskal(*[g["rank"].tolist()
                       for _,g in df.groupby(["Curve","Critic"]) if len(g)>=2])
            h_axb   = round(max(0.0, h_all-h_c-h_r), 4)
            p_axb   = round(float(scipy_stats.chi2.sf(h_axb,1)), 4)
            e_axb   = round(h_axb/ss_r,4) if ss_r>0 else np.nan
        except Exception:
            h_axb=p_axb=e_axb=np.nan
        result.update({
            "Omnibus_Test":          "Scheirer-Ray-Hare",
            "Omnibus_A_Curve_Stat":  h_c, "Omnibus_A_Curve_p":  p_c,
            "Omnibus_A_Curve_Sig":   get_sig_asterisks(p_c), "Omnibus_A_Curve_ES": e_c,
            "Omnibus_B_Critic_Stat": h_r, "Omnibus_B_Critic_p": p_r,
            "Omnibus_B_Critic_Sig":  get_sig_asterisks(p_r), "Omnibus_B_Critic_ES": e_r,
            "Omnibus_AxB_Stat":      h_axb, "Omnibus_AxB_p": p_axb,
            "Omnibus_AxB_Sig":       get_sig_asterisks(p_axb), "Omnibus_AxB_ES": e_axb,
        })
    return result



# Novel-level aggregation(not used in this paper)
def build_novel_scores_df(df: pd.DataFrame, method_name: str, mode="top3") -> pd.DataFrame:
    valid = df[df["Status"] != "FAILED"].copy() if "Status" in df.columns else df.copy()
    for m in REPORT_METRICS:
        valid[f"{m}_Score"] = pd.to_numeric(valid[f"{m}_Score"], errors="coerce")

    rows = []
    for (theme, genre, novel), grp in valid.groupby(["Theme","Genre","Novel"], sort=False):
        grp = grp.dropna(subset=["OV_Score"])
        if grp.empty: continue
        if mode == "top3":
            grp = grp.nlargest(TOP_K, "OV_Score")
        row = {
            "Theme": theme, "Genre": genre, "Novel": novel,
            "Curve_Type": extract_curve_type(novel),
            "Story_ID":   extract_story_id(novel),
            "Method":     method_name, "Route_Count": len(grp),
        }
        for m in REPORT_METRICS:
            col = f"{m}_Score"
            row[m] = round(float(grp[col].mean()), 4) if col in grp.columns else np.nan
        rows.append(row)
    return pd.DataFrame(rows)


def make_wide_novel_table(novel_dfs: dict, all_methods: list) -> pd.DataFrame:
    base = ["Theme","Genre","Novel","Curve_Type","Story_ID"]
    merged = None
    for m in all_methods:
        if m not in novel_dfs: continue
        rmap = {"Route_Count": f"{m}_Count"}
        rmap.update({dim: f"{m}_{dim}" for dim in REPORT_METRICS})
        sub = novel_dfs[m][base + ["Route_Count"] + REPORT_METRICS].rename(columns=rmap)
        merged = sub if merged is None else pd.merge(merged, sub, on=base, how="outer")
    return merged.sort_values(base).reset_index(drop=True) if merged is not None else pd.DataFrame()


def build_group_scores_table(novel_dfs, ordered_method, report_dir, tag):
    all_methods = [m for m in ordered_method if m in novel_dfs]
    for level, key_cols in [("Genre",["Theme","Genre"]), ("Theme",["Theme"]), ("Curve",["Curve_Type"])]:
        all_keys = sorted({
            tuple(r[c] for c in key_cols)
            for m in all_methods
            for _,r in novel_dfs[m][key_cols].drop_duplicates().iterrows()
        })
        rows = []
        for kv in all_keys:
            kd = dict(zip(key_cols, kv))
            cache = {}
            for m in all_methods:
                mask = pd.Series(True, index=novel_dfs[m].index)
                for col,val in kd.items(): mask &= (novel_dfs[m][col] == val)
                grp = novel_dfs[m][mask]
                cache[m] = {"Count": int(grp["Route_Count"].sum()) if "Route_Count" in grp else len(grp)}
                for dim in REPORT_METRICS:
                    vals = grp[dim].dropna().tolist() if dim in grp else []
                    cache[m][dim] = round(float(np.mean(vals)),4) if vals else np.nan
            for metric in ["Count"] + REPORT_METRICS:
                row = dict(kd); row["Metric"] = metric
                for m in all_methods: row[m] = cache[m][metric]
                rows.append(row)
        pd.DataFrame(rows).to_csv(
            os.path.join(report_dir, f"Group_Scores_{level}_{tag}.csv"),
            index=False, encoding="utf-8-sig")
        print(f"   [OK] Group_Scores_{level}_{tag}.csv")



# Route-level preparation
def get_route_level_dfs(dfs_by_method: dict, mode="all") -> dict:
    route_dfs = {}
    for m, df in dfs_by_method.items():
        valid = df[df["Status"] != "FAILED"].copy() if "Status" in df.columns else df.copy()
        if "OV_Score" in valid.columns:
            valid["OV_Score"] = pd.to_numeric(valid["OV_Score"], errors="coerce")
            valid = valid.dropna(subset=["OV_Score"])
        if valid.empty:
            print(f"   [Critical] Method '{m}': 0 valid routes.")
        if mode == "top3" and not valid.empty:
            valid = (valid.sort_values("OV_Score", ascending=False)
                         .groupby(["Theme","Genre","Novel"]).head(TOP_K))
        if "Novel" in valid.columns:
            valid["Curve_Type"] = valid["Novel"].apply(extract_curve_type)
            valid["Story_ID"]   = valid["Novel"].apply(extract_story_id)
        route_dfs[m] = valid
    return route_dfs



# Adaptive stats (Theme/Genre level — Omnibus + pairwise)
def build_adaptive_stat_row(group_info, all_methods, pairs, route_dfs, filter_fn):
    row = dict(group_info)
    for metric in REPORT_METRICS:
        col = f"{metric}_Score"
        data = {}
        for m in all_methods:
            if m not in route_dfs: continue
            scores = route_dfs[m][filter_fn(route_dfs[m])][col].tolist()
            clean  = [x for x in scores if not np.isnan(x)]
            data[m] = clean
            row[f"{metric}_N_{m}"]          = len(clean)
            row[f"{metric}_Mean_{m}"]       = round(np.mean(clean),4)       if clean        else np.nan
            row[f"{metric}_SD_{m}"]         = round(np.std(clean,ddof=1),4) if len(clean)>1 else np.nan
            ci_l,ci_h = compute_mean_ci(clean)
            row[f"{metric}_CI95_Lower_{m}"] = round(ci_l,4) if not np.isnan(ci_l) else np.nan
            row[f"{metric}_CI95_Upper_{m}"] = round(ci_h,4) if not np.isnan(ci_h) else np.nan

        # Two-Way ANOVA / Scheirer-Ray-Hare Omnibus
        omni = run_two_way_omnibus(data, col)
        for k,v in omni.items():
            row[f"{metric}_{k}"] = v

        # Planned pairwise comparisons
        for m_a, m_b in pairs:
            pk = f"{metric}_{m_a}_vs_{m_b}"
            if m_a in data and m_b in data:
                res = run_adaptive_pairwise(data[m_a], data[m_b])
                row[f"{pk}_Test"]       = res["Test_Used"]
                row[f"{pk}_SW_p_A"]     = res["SW_p_A"]
                row[f"{pk}_SW_p_B"]     = res["SW_p_B"]
                row[f"{pk}_Stat"]       = res["Statistic"]
                row[f"{pk}_Mean_Diff"]  = res["Mean_Diff"]
                row[f"{pk}_CI95_Lower"] = res["CI95_Lower"]
                row[f"{pk}_CI95_Upper"] = res["CI95_Upper"]
                row[f"{pk}_Cohen_d"]    = res["Cohen_d"]
                row[f"{pk}_p_raw"]      = res["p_raw"]
                row[f"{pk}_Sig_raw"]    = res["Sig_raw"]
            else:
                row.update({f"{pk}_Test":"-", f"{pk}_SW_p_A":np.nan, f"{pk}_SW_p_B":np.nan,
                             f"{pk}_Stat":np.nan, f"{pk}_Mean_Diff":np.nan,
                             f"{pk}_CI95_Lower":np.nan, f"{pk}_CI95_Upper":np.nan,
                             f"{pk}_Cohen_d":np.nan, f"{pk}_p_raw":np.nan,
                             f"{pk}_Sig_raw":""})
    return row


def run_all_stats(route_dfs, pairs, report_dir, tag):
    all_methods = list(route_dfs.keys())
    all_themes  = sorted({r for m in route_dfs for r in route_dfs[m]["Theme"].unique()})
    all_tg      = sorted({(r["Theme"],r["Genre"])
                          for m in route_dfs
                          for _,r in route_dfs[m][["Theme","Genre"]].drop_duplicates().iterrows()})
    print(f"\n   [{tag}] Two-Way omnibus & pairwise tests...")

    theme_rows = []
    for theme in all_themes:
        row = build_adaptive_stat_row(
            {"Theme": theme}, all_methods, pairs, route_dfs,
            lambda df,t=theme: df["Theme"]==t)
        omni_p = row.get("OV_Omnibus_A_Curve_p", np.nan)
        print(f"     Theme={theme:<20} | Two-Way ANOVA/SRH: Curve p={omni_p}")
        theme_rows.append(row)

    genre_rows = []
    for (theme,genre) in all_tg:
        row = build_adaptive_stat_row(
            {"Theme":theme,"Genre":genre}, all_methods, pairs, route_dfs,
            lambda df,t=theme,g=genre: (df["Theme"]==t)&(df["Genre"]==g))
        genre_rows.append(row)

    pd.DataFrame(theme_rows).to_csv(
        os.path.join(report_dir, f"Theme_Stats_Adaptive_{tag}.csv"),
        index=False, encoding="utf-8-sig")
    pd.DataFrame(genre_rows).to_csv(
        os.path.join(report_dir, f"Genre_Stats_Adaptive_{tag}.csv"),
        index=False, encoding="utf-8-sig")
    print(f"   [OK] Theme_Stats_Adaptive_{tag}.csv  ({len(theme_rows)} rows)")
    print(f"   [OK] Genre_Stats_Adaptive_{tag}.csv  ({len(genre_rows)} rows)")
    run_curve_stats(route_dfs, report_dir, tag)



# Curve-level stats (within-method, 6 curves, One-Way ANOVA / Kruskal-Wallis)
def run_curve_stats(route_dfs, report_dir, tag):
    all_methods = list(route_dfs.keys())
    all_curves  = sorted({c for m in all_methods
                           if "Curve_Type" in route_dfs[m].columns
                           for c in route_dfs[m]["Curve_Type"].dropna().unique()},
                          key=natural_keys)
    if not all_curves: return

    curve_pairs = list(combinations(all_curves, 2))
    n_comp      = len(curve_pairs)
    print(f"\n   [{tag}] Curve ablation — {len(all_curves)} curves, {n_comp} pairs per method")

    rows = []
    for method in all_methods:
        df_m = route_dfs.get(method)
        if df_m is None or "Curve_Type" not in df_m.columns: continue
        cd   = {c: df_m[df_m["Curve_Type"]==c] for c in all_curves}

        for metric in REPORT_METRICS:
            col = f"{metric}_Score"
            row = {"Method": method, "Metric": metric}
            sbc = {}; vg = []

            for curve in all_curves:
                scores = cd[curve][col].dropna().tolist() if col in cd[curve].columns else []
                sbc[curve] = scores
                row[f"{curve}_N"]          = len(scores)
                row[f"{curve}_Mean"]       = round(np.mean(scores),4)       if scores        else np.nan
                row[f"{curve}_SD"]         = round(np.std(scores,ddof=1),4) if len(scores)>1 else np.nan
                cl,ch = compute_mean_ci(scores)
                row[f"{curve}_CI95_Lower"] = round(cl,4) if not np.isnan(cl) else np.nan
                row[f"{curve}_CI95_Upper"] = round(ch,4) if not np.isnan(ch) else np.nan
                if len(scores) >= 3: vg.append(scores)

            if len(vg) >= 3:
                all_vals = [v for g in vg for v in g]
                if len(set(all_vals)) <= 1:
                    row.update({"Omnibus_Test":"N/A (identical values)",
                                "Omnibus_Stat":np.nan, "Omnibus_p":np.nan, "Omnibus_Sig":""})
                else:
                    is_normal = all(check_normality(g) for g in vg)
                    try:
                        if is_normal:
                            st,pv = scipy_stats.f_oneway(*vg); tn = "One-Way ANOVA"
                        else:
                            st,pv = scipy_stats.kruskal(*vg); tn = "Kruskal-Wallis"
                        row.update({"Omnibus_Test":tn, "Omnibus_Stat":round(st,4),
                                    "Omnibus_p":round(pv,4), "Omnibus_Sig":get_sig_asterisks(pv)})
                    except ValueError:
                        row.update({"Omnibus_Test":"N/A (error)","Omnibus_Stat":np.nan,
                                    "Omnibus_p":np.nan,"Omnibus_Sig":""})
            else:
                row.update({"Omnibus_Test":"N/A","Omnibus_Stat":np.nan,
                            "Omnibus_p":np.nan,"Omnibus_Sig":""})

            for ca,cb in curve_pairs:
                pk  = f"{ca}_vs_{cb}"
                res = run_adaptive_pairwise(sbc.get(ca,[]), sbc.get(cb,[]))
                row[f"{pk}_Test"]       = res["Test_Used"]
                row[f"{pk}_SW_p_A"]     = res["SW_p_A"]
                row[f"{pk}_SW_p_B"]     = res["SW_p_B"]
                row[f"{pk}_Stat"]       = res["Statistic"]
                row[f"{pk}_Mean_Diff"]  = res["Mean_Diff"]
                row[f"{pk}_CI95_Lower"] = res["CI95_Lower"]
                row[f"{pk}_CI95_Upper"] = res["CI95_Upper"]
                row[f"{pk}_Cohen_d"]    = res["Cohen_d"]
                row[f"{pk}_p_raw"]      = res["p_raw"]
                row[f"{pk}_Sig_raw"]    = res["Sig_raw"]
            rows.append(row)

    if rows:
        pd.DataFrame(rows).to_csv(
            os.path.join(report_dir, f"Curve_Stats_Adaptive_{tag}.csv"),
            index=False, encoding="utf-8-sig")
        print(f"   [OK] Curve_Stats_Adaptive_{tag}.csv ({len(rows)} rows)")



# 2x2 Factorial analysis
def run_factorial_analysis(route_dfs, report_dir, tag):
    def get_s(method, metric):
        col = f"{metric}_Score"
        if method not in route_dfs or col not in route_dfs[method].columns: return []
        return route_dfs[method][col].dropna().tolist()

    def sm_(lst): return round(float(np.mean(lst)),4) if lst else np.nan

    rows = []
    for metric in REPORT_METRICS:
        rn = get_s("RAF_NoCritic",metric); ry = get_s("RAF_Critic",metric)
        an = get_s("AVL_NoCritic",metric); ay = get_s("AVL_Critic",metric)
        raf_all = rn+ry; avl_all = an+ay
        no_all  = rn+an; cr_all  = ry+ay

        res_A   = run_adaptive_pairwise(raf_all, avl_all)
        res_B   = run_adaptive_pairwise(no_all,  cr_all)
        res_crf = run_adaptive_pairwise(rn, ry)
        res_cra = run_adaptive_pairwise(an, ay)
        res_cvn = run_adaptive_pairwise(rn, an)
        res_cvy = run_adaptive_pairwise(ry, ay)

        g_raf = sm_(ry)-sm_(rn) if (ry and rn) else np.nan
        g_avl = sm_(ay)-sm_(an) if (ay and an) else np.nan
        delta = round(g_raf-g_avl,4) if not(np.isnan(g_raf) or np.isnan(g_avl)) else np.nan
        dirn  = ("RAF benefits more from Critic" if not np.isnan(delta) and delta>0
                 else "AVL benefits more from Critic" if not np.isnan(delta) and delta<0
                 else "Equal gain" if delta==0 else "N/A")

        def pk(pfx, res):
            return {f"{pfx}_{k}": v for k,v in {
                "Test":res["Test_Used"], "SW_p_A":res["SW_p_A"], "SW_p_B":res["SW_p_B"],
                "Stat":res["Statistic"], "Mean_Diff":res["Mean_Diff"],
                "CI95_Lower":res["CI95_Lower"], "CI95_Upper":res["CI95_Upper"],
                "Cohen_d":res["Cohen_d"], "p_raw":res["p_raw"], "Sig_raw":res["Sig_raw"],
            }.items()}

        rows.append({
            "Metric": metric,
            "Cell_RAF_NoCritic_N":sm_(rn) and len(rn), "Cell_RAF_NoCritic_Mean":sm_(rn),
            "Cell_RAF_Critic_N":len(ry),   "Cell_RAF_Critic_Mean":sm_(ry),
            "Cell_AVL_NoCritic_N":len(an), "Cell_AVL_NoCritic_Mean":sm_(an),
            "Cell_AVL_Critic_N":len(ay),   "Cell_AVL_Critic_Mean":sm_(ay),
            "Marginal_RAF_Mean":sm_(raf_all), "Marginal_RAF_N":len(raf_all),
            "Marginal_AVL_Mean":sm_(avl_all), "Marginal_AVL_N":len(avl_all),
            "Marginal_NoCritic_Mean":sm_(no_all), "Marginal_NoCritic_N":len(no_all),
            "Marginal_Critic_Mean":sm_(cr_all),   "Marginal_Critic_N":len(cr_all),
            "Interaction_Gain_RAF":round(g_raf,4) if not np.isnan(g_raf) else np.nan,
            "Interaction_Gain_AVL":round(g_avl,4) if not np.isnan(g_avl) else np.nan,
            "Interaction_Delta":delta, "Interaction_Direction":dirn,
            **pk("MainEffect_A_Curve",         res_A),
            **pk("MainEffect_B_Critic",        res_B),
            **pk("SimpleEffect_Critic_at_RAF", res_crf),
            **pk("SimpleEffect_Critic_at_AVL", res_cra),
            **pk("SimpleEffect_Curve_NoCritic",res_cvn),
            **pk("SimpleEffect_Curve_Critic",  res_cvy),
        })

        if metric == "OV":
            print(f"\n   ── Factorial [{tag}] OV ──────────────────────────────────────────")
            print(f"   Cell: RAF/No={sm_(rn)} RAF/Crit={sm_(ry)} AVL/No={sm_(an)} AVL/Crit={sm_(ay)}")
            print(f"   Main A (Curve):  [{res_A['Test_Used']}] p={res_A['p_raw']} {res_A['Sig_raw']} d={res_A['Cohen_d']}")
            print(f"   Main B (Critic): [{res_B['Test_Used']}] p={res_B['p_raw']} {res_B['Sig_raw']} d={res_B['Cohen_d']}")
            print(f"   Interaction Δ={delta} → {dirn}")
            print("   ─────────────────────────────────────────────────────────────────────")

    pd.DataFrame(rows).to_csv(
        os.path.join(report_dir, f"Factorial_2x2_{tag}.csv"),
        index=False, encoding="utf-8-sig")
    print(f"   [OK] Factorial_2x2_{tag}.csv")



# Top-level report generation for one set of CSVs
def generate_reports(dfs_by_method: dict, ordered_method: list, report_dir: str):
    os.makedirs(report_dir, exist_ok=True)

    print("\n[Step 1] Novel-level scores...")
    novel_top3 = {}; novel_all = {}
    for method, df in dfs_by_method.items():
        novel_top3[method] = build_novel_scores_df(df, method, mode="top3")
        novel_all[method]  = build_novel_scores_df(df, method, mode="allmean")

    for tag, novel_dfs in [("Top3", novel_top3), ("AllMean", novel_all)]:
        wide = make_wide_novel_table(novel_dfs, ordered_method)
        if not wide.empty:
            wide.to_csv(os.path.join(report_dir, f"Novel_Scores_{tag}.csv"),
                        index=False, encoding="utf-8-sig")
            print(f"   [OK] Novel_Scores_{tag}.csv ({len(wide)} novels)")
        build_group_scores_table(novel_dfs, ordered_method, report_dir, tag)

    avail_pairs = [(a,b) for a,b in COMPARISON_PAIRS
                   if a in dfs_by_method and b in dfs_by_method]
    r_top3 = get_route_level_dfs(dfs_by_method, mode="top3")
    r_all  = get_route_level_dfs(dfs_by_method, mode="all")

    print("\n[Step 2] Statistical tests...")
    for tag, rdfs in [("Top3",r_top3), ("AllMean",r_all)]:
        print(f"\n  == {tag} ==")
        run_all_stats(rdfs, avail_pairs, report_dir, tag)

    print("\n[Step 3] Factorial analysis...")
    for tag, rdfs in [("Top3",r_top3), ("AllMean",r_all)]:
        print(f"\n  == {tag} ==")
        run_factorial_analysis(rdfs, report_dir, tag)

    print(f"\n[Done] Reports -> {report_dir}")


# CSV loading
def load_csvs_for_model(model: str, methods: list) -> dict:
    sm   = safe_model_name(model)
    dfs  = {}
    for method in methods:
        path = os.path.join(RAW_DIR, f"method_{method}",
                            f"Model_{sm}", f"Scores_{method}_by_{sm}.csv")
        if os.path.exists(path):
            dfs[method] = normalize_df(pd.read_csv(path))
            print(f"   [Loaded] {method} / {model}")
        else:
            print(f"   [Missing] {path}")
    return dfs


# Main
def main():
    parser = argparse.ArgumentParser(
        description="eval_stats.py — Statistical analysis from eval_runner CSVs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From one evaluator model
  python eval_stats.py --source model --model qwen3:14b-fp16

  # All 3 models independently (3 separate report folders)
  python eval_stats.py --source all-models --models qwen3:14b-fp16 mistral:7b-instruct-v0.3-fp16 gemma3:12b-it-fp16
        """)
    parser.add_argument("--source", choices=["merged","model","all-models"],
                        default="merged",
                        help="Which scores to use as input")
    parser.add_argument("--model",  default=None,
                        help="Single model name (required for --source model)")
    parser.add_argument("--models", nargs="+", default=None,
                        help="All model names (required for --source all-models)")
    parser.add_argument("--method", nargs="+", default=DEFAULT_METHODS,
                        help="Method names to include")
    args = parser.parse_args()

    os.makedirs(REPORTS_DIR, exist_ok=True)
    print("=" * 60)
    print(f"eval_stats  |  source={args.source}")
    print("=" * 60)

    if args.source == "model":
        if not args.model:
            print("[Error] --model required for --source model"); return
        print(f"\n[Loading] Single model: {args.model}")
        dfs = load_csvs_for_model(args.model, args.method)
        if not dfs:
            print("[Error] No CSVs found."); return
        report_dir = os.path.join(REPORTS_DIR, f"Model_{safe_model_name(args.model)}")
        generate_reports(dfs, args.method, report_dir)

    elif args.source == "all-models":
        if not args.models:
            print("[Error] --models required for --source all-models"); return
        for model in args.models:
            print(f"\n{'='*60}")
            print(f"[Loading] Model: {model}")
            dfs = load_csvs_for_model(model, args.method)
            if not dfs:
                print(f"[Skip] No CSVs for {model}"); continue
            report_dir = os.path.join(REPORTS_DIR, f"Model_{safe_model_name(model)}")
            generate_reports(dfs, args.method, report_dir)


if __name__ == "__main__":
    main()