"""
route_ranking.py — Per-Route Scores across Models, Best Route per Curve

Reads per-model Scores_*.csv from:
  01_Raw_Evaluations/method_<name>/Model_<model>/Scores_<method>_by_<model>.csv

Output (one CSV):
  Route_Scores_Full.csv
    - One row per method × route × model  (3 rows per route if 3 models ran)
    - Columns: Method, Curve_Type, Novel, Route_File, Model, RE..OV scores
    - Best_OV  : "YES" if this route is the majority-model OV  winner in its method×curve
    - Best_EM  : "YES" if this route is the majority-model EM  winner in its method×curve

"Selected" = "YES" if this route is selected based on the exemplar selection protocal
within its method × curve group.

Usage:
    python route_ranking.py \\
        --raw_dir    Paper_Results/01_Raw_Evaluations \\
        --output_dir Paper_Results/04_Route_Rankings
"""

import csv
import re
import argparse
from pathlib import Path
from collections import defaultdict


# Configuration 

METRICS    = ["RE", "CH", "EM", "SU", "EG", "CX", "OV"]
SCORE_COLS = [f"{m}_Score" for m in METRICS]

FOLDER_TO_METHOD = {
    "method_RAF_NoCritic":  "RAF_NoCritic",
    "method_RAF_Critic":    "RAF_Critic",
    "method_AVL_NoCritic":  "AVL_NoCritic",
    "method_AVL_Critic":    "AVL_Critic",
    "RAF_NoCritic":         "RAF_NoCritic",
    "RAF_Critic":           "RAF_Critic",
    "AVL_NoCritic":         "AVL_NoCritic",
    "AVL_Critic":           "AVL_Critic",
}


# Loading 

def load_scores_csv(path, method, model):
    records = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "FAIL" in row.get("Status", "").upper():
                continue
            scores = {}
            valid = True
            for col in SCORE_COLS:
                try:
                    scores[col] = float(row[col])
                except (KeyError, ValueError):
                    valid = False
                    break
            if not valid:
                continue
            records.append({
                "Method":     method,
                "Curve_Type": row.get("Curve_Type", ""),
                "Theme":      row.get("Theme", ""),
                "Genre":      row.get("Genre", ""),
                "Novel":      row.get("Novel", ""),
                "Story_ID":   row.get("Story_ID", ""),
                "Route_File": row.get("Route_File", ""),
                "Model":      model,
                "Num_Runs":   row.get("Num_Runs", ""),
                "Status":     row.get("Status", ""),
                **scores,
            })
    return records


def discover_and_load(raw_dir):
    """
    Walk raw_dir for per-model CSVs.
    Expected: <raw_dir>/method_<X>/Model_<M>/Scores_<X>_by_<M>.csv
    """
    raw_dir = Path(raw_dir)
    all_records = []

    for csv_path in sorted(raw_dir.rglob("Scores_*.csv")):
        # Infer method: look for a parent folder matching FOLDER_TO_METHOD
        method = None
        for part in csv_path.parts:
            if part in FOLDER_TO_METHOD:
                method = FOLDER_TO_METHOD[part]
                break
        if method is None:
            print(f"  [Skip] Cannot infer method: {csv_path}")
            continue

        # Infer model from Model_<X> folder name
        model = None
        for part in csv_path.parts:
            if part.startswith("Model_"):
                model = part[len("Model_"):]
                break
        if model is None:
            # Fall back: extract from filename Scores_<method>_by_<model>.csv
            m = re.search(r"_by_(.+)\.csv$", csv_path.name)
            model = m.group(1) if m else csv_path.stem

        records = load_scores_csv(csv_path, method, simplify_model_name(model))
        print(f"  [OK] {csv_path.relative_to(raw_dir)}  ->  {method} | {model}  ({len(records)} routes)")
        all_records.extend(records)

    return all_records


def simplify_model_name(name):
    """Shorten model folder names, e.g. qwen3_14b-fp16 -> Qwen3-14B."""
    n = name.lower()
    if "qwen3" in n:
        m = re.search(r"(\d+\.?\d*)b", n)
        return f"Qwen3-{m.group(0).upper()}" if m else "Qwen3"
    if "gemma3" in n:
        m = re.search(r"(\d+\.?\d*)b", n)
        return f"Gemma3-{m.group(0).upper()}" if m else "Gemma3"
    if "mistral" in n:
        m = re.search(r"(\d+\.?\d*)b", n)
        return f"Mistral-{m.group(0).upper()}" if m else "Mistral"
    # Fallback
    return re.sub(r"[-_](fp|int|q)\d+.*$", "", name, flags=re.IGNORECASE).replace("_", "-").title()


# Route selection logic

def _consensus_level(vote_count, n_models):
    if vote_count == n_models: return 3
    if vote_count > n_models / 2: return 2
    return 0


def _get_votes(group_records, score_col):
    by_model = defaultdict(list)
    for r in group_records:
        by_model[r["Model"]].append(r)
    votes = defaultdict(int)
    for model_recs in by_model.values():
        best = max(float(r[score_col]) for r in model_recs)
        for r in model_recs:
            if float(r[score_col]) == best:
                votes[(r["Novel"], r["Route_File"])] += 1
    return votes


def select_best_route(group_records, ov_threshold, n_models):
    """
    1. Keep routes where ALL models give OV >= ov_threshold.
    2. Among candidates, vote on EM; prefer unanimous (3/3) over majority (2/3).
    3. Tiebreak by OV consensus, then cross-model mean OV.
    Returns dict with Novel/Route_File of winner, or None.
    """
    route_model_scores = defaultdict(dict)
    for r in group_records:
        route_model_scores[(r["Novel"], r["Route_File"])][r["Model"]] = r

    candidates = [
        (novel, rf)
        for (novel, rf), model_dict in route_model_scores.items()
        if len(model_dict) >= n_models
        and all(float(rec["OV_Score"]) >= ov_threshold for rec in model_dict.values())
    ]
    if not candidates:
        return None

    cand_set     = set(candidates)
    cand_records = [r for r in group_records if (r["Novel"], r["Route_File"]) in cand_set]

    em_votes     = _get_votes(cand_records, "EM_Score")
    best_em_tier = max(_consensus_level(em_votes.get(c, 0), n_models) for c in candidates)
    em_finalists = [c for c in candidates
                    if _consensus_level(em_votes.get(c, 0), n_models) == best_em_tier]

    if len(em_finalists) == 1:
        winner = em_finalists[0]
    else:
        tb_records   = [r for r in cand_records if (r["Novel"], r["Route_File"]) in set(em_finalists)]
        ov_votes     = _get_votes(tb_records, "OV_Score")
        best_ov_tier = max(_consensus_level(ov_votes.get(c, 0), n_models) for c in em_finalists)
        ov_finalists = [c for c in em_finalists
                        if _consensus_level(ov_votes.get(c, 0), n_models) == best_ov_tier]

        def mean_ov(novel_rf):
            recs = route_model_scores[novel_rf]
            return sum(float(r["OV_Score"]) for r in recs.values()) / len(recs)

        winner = max(ov_finalists, key=mean_ov)

    novel, route_file = winner
    return {"Novel": novel, "Route_File": route_file}


def find_majority_best(all_records, metric_col):
    """
    For each (method, curve) group:
      - Each model finds its highest score for metric_col in this group.
      - All routes tied at that highest score each get 1 vote from that model.
      - Only routes with votes strictly > N_models / 2 are candidates.
      - If multiple candidates tie on vote count, keep only those with the
        highest cross-model mean score for metric_col (tiebreak).
      - If no route reaches majority, nothing is flagged.
    Returns a set of (method, curve, novel, route_file) tuples.
    """
    group = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for r in all_records:
        group[r["Method"]][r["Curve_Type"]][r["Model"]].append(r)

    # Cross-model mean per route
    route_mean = defaultdict(list)
    for r in all_records:
        key = (r["Method"], r["Curve_Type"], r["Novel"], r["Route_File"])
        route_mean[key].append(float(r[metric_col]))

    majority_best = set()
    voters = defaultdict(list)  # (method,curve,novel,rf) -> [model_names that voted]

    for method, curves in group.items():
        for curve, models in curves.items():
            votes  = defaultdict(int)
            voted_by = defaultdict(list)  # (novel,rf) -> [model_names]
            n_models = len(models)

            for model_name, records in models.items():
                if not records:
                    continue
                best_score = max(float(r[metric_col]) for r in records)
                for r in records:
                    if float(r[metric_col]) == best_score:
                        votes[(r["Novel"], r["Route_File"])] += 1
                        if model_name not in voted_by[(r["Novel"], r["Route_File"])]:
                            voted_by[(r["Novel"], r["Route_File"])].append(model_name)

            majority_threshold = n_models / 2
            candidates = [(n, rf) for (n, rf), v in votes.items()
                          if v > majority_threshold]

            if not candidates:
                continue

            # Among candidates, only keep those with the highest vote count
            max_votes = max(votes[(n, rf)] for n, rf in candidates)
            candidates = [(n, rf) for n, rf in candidates
                          if votes[(n, rf)] == max_votes]

            if len(candidates) == 1:
                n, rf = candidates[0]
                majority_best.add((method, curve, n, rf))
                voters[(method, curve, n, rf)] = voted_by[(n, rf)]
            else:
                def get_mean(n, rf):
                    vals = route_mean[(method, curve, n, rf)]
                    return sum(vals) / len(vals) if vals else 0.0

                best_mean = max(get_mean(n, rf) for n, rf in candidates)
                for n, rf in candidates:
                    if get_mean(n, rf) >= best_mean:
                        majority_best.add((method, curve, n, rf))
                        voters[(method, curve, n, rf)] = voted_by[(n, rf)]

    return majority_best, voters


# Output 

OUT_COLS = (["Method", "Curve_Type", "Theme", "Genre", "Novel",
             "Story_ID", "Route_File", "Model", "Num_Runs", "Status"]
            + SCORE_COLS
            + ["Best_OV", "OV_Voters", "Best_EM", "EM_Voters", "Selected"])


def write_full_table(all_records, majority_ov, voters_ov, majority_em, voters_em, selected_set, out_path):
    """
    One row per method × route × model, sorted by:
      Curve_Type → Method → Route_File → Model
    Best_OV / Best_EM flagged per majority vote.
    """
    def sort_key(r):
        m = re.search(r"\d+", r["Curve_Type"])
        cnum = int(m.group()) if m else 99
        return (cnum, r["Method"], r["Novel"], r["Route_File"], r["Model"])

    rows = sorted(all_records, key=sort_key)

    for r in rows:
        key = (r["Method"], r["Curve_Type"], r["Novel"], r["Route_File"])
        r["Best_OV"] = "YES" if key in majority_ov else ""
        r["OV_Voters"] = "; ".join(voters_ov.get(key, [])) if key in majority_ov else ""
        r["Best_EM"] = "YES" if key in majority_em else ""
        r["EM_Voters"] = "; ".join(voters_em.get(key, [])) if key in majority_em else ""
        r["Selected"] = "YES" if key in selected_set else ""

    with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    flagged_ov  = sum(1 for r in rows if r["Best_OV"]  == "YES")
    flagged_em  = sum(1 for r in rows if r["Best_EM"]  == "YES")
    n_selected  = sum(1 for r in rows if r["Selected"] == "YES")
    print(f"  [OK] Route_Scores_Full.csv  ({len(rows)} rows, "
          f"{flagged_ov} Best_OV flags, {flagged_em} Best_EM flags, {n_selected} Selected)")


# Main

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_dir",    required=True,
                        help="Path to 01_Raw_Evaluations/ directory")
    parser.add_argument("--output_dir", default="Paper_Results/Route_Rankings",
                        help="Output directory")
    parser.add_argument("--ov_threshold", type=float, default=4.0,
                        help="OV threshold for Selected flag (default: 4.0)")
    parser.add_argument("--curve", default=None,
                        help="Restrict selection to one curve type, e.g. Curve_2 (default: all curves)")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nLoading scores from: {args.raw_dir}")
    records = discover_and_load(args.raw_dir)

    if not records:
        print("[Error] No valid route scores found. Check --raw_dir path.")
        return

    print(f"\nTotal rows loaded: {len(records)}")

    print("\nComputing majority-best routes...")
    majority_ov, voters_ov = find_majority_best(records, "OV_Score")
    majority_em, voters_em = find_majority_best(records, "EM_Score")

    curve_filter = args.curve  # e.g. "Curve_2" or None
    print("\nRunning route selection (OV >= {:.1f}{})...".format(
        args.ov_threshold, f", curve={curve_filter}" if curve_filter else ""))
    n_models = len({r["Model"] for r in records})
    groups = defaultdict(list)
    for r in records:
        groups[(r["Method"], r["Curve_Type"])].append(r)
    selected_set = set()
    for (method, curve), recs in groups.items():
        if curve_filter and curve != curve_filter:
            continue
        result = select_best_route(recs, args.ov_threshold, n_models)
        if result:
            selected_set.add((method, curve, result["Novel"], result["Route_File"]))
    print(f"  Selected {len(selected_set)} routes")

    n_models = len({r["Model"] for r in records})
    print(f"  Models detected: {n_models}  "
          f"(majority threshold: >{n_models/2:.1f} votes)")
    print(f"  Majority-best OV routes: {len(majority_ov)}")
    print(f"  Majority-best EM routes: {len(majority_em)}")

    print("\nWriting output...")
    write_full_table(records, majority_ov, voters_ov, majority_em, voters_em, selected_set,
                     out_dir / "Route_Scores_Full.csv")

    print(f"\n[Done] Saved to: {out_dir.resolve()}")
    print("\nColumns: Method | Curve_Type | Novel | Route_File | Model | "
          "RE..OV | Best_OV | Best_EM")
    print("Best_OV / Best_EM = YES  ->  majority of models voted this route "
          "best for that metric within its method x curve group")


if __name__ == "__main__":
    main()