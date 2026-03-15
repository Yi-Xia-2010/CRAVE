"""
eval.py — LLM Evaluation Script
=======================================
Runs triple-seed LLM evaluation for all 4 methods and one evaluator model.
Outputs one CSV per method under:
  Paper_Results/01_Raw_Evaluations/method_<NAME>/Model_<MODEL>/Scores_<NAME>_by_<MODEL>.csv

Usage:
  python eval.py --model qwen3:14b-fp16
"""

import os
import csv
import json
import re
import argparse
import ast
import sys
import time

import numpy as np
from openai import OpenAI


DEFAULT_MODEL    = "qwen3:14b-fp16"
DEFAULT_API_URL  = "http://localhost:11434/v1"
DEFAULT_API_KEY  = "ollama"
ROOT_OUTPUT_DIR  = "Paper_Results"
PROMPT_FILE_PATH = "eval_prompt.txt"
MAX_RETRIES      = 3

TRIPLE_RUN_CONFIGS = [
    {"run": 1, "temperature": 0, "seed": 42},
    {"run": 2, "temperature": 0, "seed": 43},
    {"run": 3, "temperature": 0, "seed": 44},
]

DEFAULT_METHOD = {
    "RAF_NoCritic": "./Rise_and_Fall",
    "RAF_Critic":   "./Rise_and_Fall_Critic",
    "AVL_NoCritic": "./V_and_A_levels",
    "AVL_Critic":   "./V_and_A_levels_Critic",
}

TARGET_FILE_PREFIX = "Route_"

METRICS_CODES  = ["RE", "CH", "EM", "SU", "EG", "CX"]
REPORT_METRICS = METRICS_CODES + ["OV"]

KEY_MAP = {
    "RE": "RE", "CH": "CH", "EM": "EM", "SU": "SU", "EG": "EG", "CX": "CX",
    "RELEVANCE": "RE", "COHERENCE": "CH", "EMPATHY": "EM",
    "SURPRISE":  "SU", "ENGAGEMENT": "EG", "COMPLEXITY": "CX",
}


def load_prompt_strict(filepath):
    if not os.path.exists(filepath):
        print(f"[Error] Prompt file not found: {filepath}")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def robust_json_extract(text):
    if not text:
        return None
    try:
        return json.loads(text)
    except Exception:
        pass
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL | re.IGNORECASE)
    text = match.group(1) if match else text
    match = re.search(r'(\{.*\})', text, re.DOTALL)
    text = match.group(1) if match else text
    text = re.sub(r',\s*\}', '}', text)
    try:
        return json.loads(re.sub(r'([0-9"])\s*\n\s*(")', r'\1,\n\2', text))
    except Exception:
        pass
    try:
        return ast.literal_eval(text)
    except Exception:
        return None


def smart_parse_score(val):
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, dict):
        for k in val.values():
            res = smart_parse_score(k)
            if res > 0:
                return res
    if isinstance(val, str):
        m = re.search(r"(\d+(\.\d+)?)", val)
        if m:
            return float(m.group(1))
    return 0


def smart_parse_explanation(val):
    if isinstance(val, str):
        return val
    if isinstance(val, dict):
        for k in ["explanation", "reason", "comment"]:
            for vk in val.keys():
                if k in vk.lower():
                    return str(val[vk])
    return "N/A"


def clean_name(s):
    return " ".join(s.replace("_", " ").replace("-", " ").split()).title().replace(" ", "_")


def natural_keys(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', str(text))]


def extract_metadata_from_path(file_path):
    parts = os.path.abspath(file_path).split(os.sep)
    if "Story_Routes" not in parts:
        return "Unknown", "Unknown", "Unknown"
    try:
        idx = parts.index("Story_Routes")
        return clean_name(parts[idx - 3]), clean_name(parts[idx - 2]), clean_name(parts[idx - 1])
    except Exception:
        return "Unknown", "Unknown", "Unknown"


def extract_curve_type(novel_name: str) -> str:
    m = re.search(r'(Curve_\d+)', str(novel_name), re.IGNORECASE)
    return m.group(1).title() if m else str(novel_name)


def extract_story_id(novel_name: str) -> str:
    m = re.search(r'(Story_\d+)', str(novel_name), re.IGNORECASE)
    return m.group(1).title() if m else "Story_1"


def call_llm_once(client, model, prompt_content, task, seed):
    with open(task["path"], "r", encoding="utf-8") as f:
        story = f.read()

    prompt = (prompt_content
              .replace("{{THEME}}", task["theme"])
              .replace("{{GENRE}}", task["genre"])
              .replace("{{STORY}}", story))

    for attempt in range(MAX_RETRIES):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert critic of Visual Novels. Output strictly in JSON."},
                    {"role": "user",   "content": prompt},
                ],
                temperature=0,
                seed=seed + attempt,
            )
            raw    = resp.choices[0].message.content
            parsed = robust_json_extract(raw)
            if parsed:
                return raw, parsed
            time.sleep(1)
        except Exception:
            time.sleep(1)
    return None, None


def extract_scores_from_parsed(parsed):
    extracted    = {}
    valid_scores = []
    for m in METRICS_CODES:
        val = 0; expl = "N/A"
        for k, v in parsed.items():
            norm_k = k.upper().split("_")[0]
            if KEY_MAP.get(norm_k) == m or norm_k == m:
                if isinstance(v, dict):
                    val  = smart_parse_score(v)
                    expl = smart_parse_explanation(v)
                else:
                    val = smart_parse_score(v)
                    for k2, v2 in parsed.items():
                        if k2.upper().startswith(m) and ("EXPL" in k2.upper() or "REASON" in k2.upper()):
                            expl = v2; break
                break
        extracted[m] = (val, expl)
        if val >= 1.0:
            valid_scores.append(val)
    ov_val  = round(np.mean(valid_scores), 4) if valid_scores else 0.0
    ov_expl = "Average of valid metrics" if valid_scores else "All metrics failed"
    return extracted, ov_val, ov_expl


def evaluate_triple(client, model, prompt_content, task, raw_dir):
    route_key       = f"{task['theme']}_{task['genre']}_{task['novel']}_{task['file'].replace('.txt','')}"
    route_cache_dir = os.path.join(raw_dir, route_key)
    os.makedirs(route_cache_dir, exist_ok=True)

    run_results = []
    for cfg in TRIPLE_RUN_CONFIGS:
        run_num  = cfg["run"]
        run_file = os.path.join(route_cache_dir, f"run{run_num}.json")
        parsed   = None

        if os.path.exists(run_file):
            try:
                with open(run_file, "r", encoding="utf-8") as rf:
                    parsed = robust_json_extract(rf.read())
                status = f"[Cached] run{run_num}" if parsed else f"[Corrupt] run{run_num}, re-eval"
            except Exception:
                status = f"[Read Error] run{run_num}, re-eval"
        else:
            status = f"[New] run{run_num}"

        if parsed is None:
            sys.stdout.write(f"   {status} | seed={cfg['seed']} ...")
            sys.stdout.flush()
            raw, parsed = call_llm_once(client, model, prompt_content, task, cfg["seed"])
            if raw and parsed:
                with open(run_file, "w", encoding="utf-8") as rf:
                    rf.write(raw)
                status = f"[Done] run{run_num}"
            else:
                status = f"[Failed] run{run_num}"
                sys.stdout.write(f"\r   {status}\n")
                continue
        else:
            sys.stdout.write(f"   {status}\n")

        sys.stdout.write(f"\r   {status}\n")
        extracted, ov_val, ov_expl = extract_scores_from_parsed(parsed)
        run_results.append((extracted, ov_val, ov_expl))

    if not run_results:
        return None, None

    mean_scores = {}
    for m in METRICS_CODES:
        vals = [r[0][m][0] for r in run_results if r[0][m][0] >= 1.0]
        mean_scores[m] = round(np.mean(vals), 4) if vals else 0.0
    ov_vals = [r[1] for r in run_results if r[1] >= 1.0]
    mean_scores["OV"] = round(np.mean(ov_vals), 4) if ov_vals else 0.0

    explanations = []
    for r in run_results:
        expl_parts = [r[0][m][1] for m in METRICS_CODES if r[0][m][1] != "N/A"]
        explanations.append(expl_parts[0] if expl_parts else r[2])

    return mean_scores, explanations


def evaluate_single_method(method_name, root_dir, model, api_url, api_key, prompt_content):
    safe_model    = model.replace(":", "_").replace("/", "_")
    base_eval_dir = os.path.join(ROOT_OUTPUT_DIR, "01_Raw_Evaluations",
                                 f"method_{method_name}", f"Model_{safe_model}")
    raw_dir       = os.path.join(base_eval_dir, "Raw_JSONs")
    os.makedirs(raw_dir, exist_ok=True)
    detail_csv    = os.path.join(base_eval_dir, f"Scores_{method_name}_by_{safe_model}.csv")

    print(f"\n[Eval] {method_name} @ {root_dir}")
    if not os.path.exists(root_dir):
        print(f"[Error] Directory not found: {root_dir}")
        return None

    tasks = []
    for root, _, files in os.walk(root_dir):
        if os.path.basename(root) != "Story_Routes":
            continue
        for file in sorted(files):
            if file.endswith(".txt") and file.startswith(TARGET_FILE_PREFIX):
                full_path = os.path.join(root, file)
                theme, genre, novel = extract_metadata_from_path(full_path)
                tasks.append({"path": full_path, "file": file,
                               "theme": theme, "genre": genre, "novel": novel})
    tasks.sort(key=lambda x: (natural_keys(x["theme"]), natural_keys(x["genre"]),
                               natural_keys(x["novel"]), natural_keys(x["file"])))

    # CSV headers
    headers = ["Theme", "Genre", "Novel", "Curve_Type", "Story_ID",
               "Route_File", "Num_Runs", "Status"]
    headers += [f"{m}_Score" for m in REPORT_METRICS]
    headers += [f"Run{i}_Explanation" for i in range(1, 4)]

    with open(detail_csv, "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow(headers)

    failed_csv = os.path.join(base_eval_dir, f"Failed_Routes_{method_name}.csv")
    with open(failed_csv, "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow(["Theme", "Genre", "Novel", "Curve_Type", "Story_ID",
                                 "Route_File", "Num_Runs", "Failure_Reason"])

    client         = OpenAI(base_url=api_url, api_key=api_key)
    ok = partial = failed = 0

    for i, task in enumerate(tasks):
        curve    = extract_curve_type(task["novel"])
        story_id = extract_story_id(task["novel"])
        sys.stdout.write(f"\r[{i+1}/{len(tasks)}] {task['novel'][:25]:<25} {task['file']:<20}\n")
        sys.stdout.flush()

        mean_scores, explanations = evaluate_triple(client, model, prompt_content, task, raw_dir)
        num_runs = len(explanations) if explanations else 0

        if mean_scores and num_runs == len(TRIPLE_RUN_CONFIGS):
            status = "OK";                                              ok      += 1
        elif mean_scores and num_runs > 0:
            status = f"PARTIAL({num_runs}/{len(TRIPLE_RUN_CONFIGS)})"; partial += 1
        else:
            status = "FAILED";                                          failed  += 1

        row  = [task["theme"], task["genre"], task["novel"], curve, story_id,
                task["file"], num_runs, status]
        row += [mean_scores.get(m, 0.0) for m in REPORT_METRICS] if mean_scores else [0.0]*len(REPORT_METRICS)
        row += [explanations[j] if explanations and j < len(explanations) else "" for j in range(3)]

        with open(detail_csv, "a", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerow(row)

        if status != "OK":
            reason = "All runs failed" if status == "FAILED" \
                     else f"Only {num_runs}/{len(TRIPLE_RUN_CONFIGS)} runs succeeded"
            with open(failed_csv, "a", newline="", encoding="utf-8-sig") as f:
                csv.writer(f).writerow([task["theme"], task["genre"], task["novel"],
                                        curve, story_id, task["file"], num_runs, reason])

    print(f"\n   [Done] {method_name}: {ok} OK, {partial} Partial, {failed} Failed.")
    if failed + partial > 0:
        print(f"   [Warning] See: {failed_csv}")
    return detail_csv


def main():
    parser = argparse.ArgumentParser(
        description="eval.py — LLM evaluation only (one evaluator model per run)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python eval.py --model qwen3:14b-fp16
  python eval.py --model qwen3:14b-fp16 \\
      --method RAF_NoCritic=./Rise_and_Fall RAF_Critic=./Rise_and_Fall_Critic \\
               AVL_NoCritic=./V_and_A_levels AVL_Critic=./V_and_A_levels_Critic
        """)
    parser.add_argument("--model",       default=DEFAULT_MODEL,   help="Evaluator LLM model name")
    parser.add_argument("--url",         default=DEFAULT_API_URL, help="API base URL")
    parser.add_argument("--key",         default=DEFAULT_API_KEY, help="API key")
    parser.add_argument("--prompt-file", default=PROMPT_FILE_PATH)
    parser.add_argument("--method",      nargs="+",
                        help="Name=Path pairs, e.g. RAF_NoCritic=./Rise_and_Fall")
    args = parser.parse_args()

    prompt_content = load_prompt_strict(args.prompt_file)

    method_config = {}
    if args.method:
        for item in args.method:
            if "=" in item:
                name, path = item.split("=", 1)
                method_config[name] = path
    else:
        method_config = DEFAULT_METHOD

    safe_model = args.model.replace(":", "_").replace("/", "_")
    print("=" * 60)
    print(f"eval  |  Evaluator: {args.model}")
    print("=" * 60)
    for name, path in method_config.items():
        print(f"  {name:<25} -> {path}")
    print()

    for name, path in method_config.items():
        evaluate_single_method(name, path, args.model, args.url, args.key, prompt_content)

    print("\n[Done] All methods evaluated.")
    print(f"Output: {ROOT_OUTPUT_DIR}/01_Raw_Evaluations/method_*/Model_{safe_model}/")


if __name__ == "__main__":
    main()