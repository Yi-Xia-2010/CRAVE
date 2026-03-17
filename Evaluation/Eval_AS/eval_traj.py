"""
emotion_plot.py — Route-Level Trajectory Plotting from Pre-computed Sentence Sequences

Reads Raw_Sequences/<method>/<theme>/<genre>/<novel>/<route>_sequence.csv
and produces route-level trajectory plots without re-running the emotion model.

Expected CSV columns: Sentence_Index, Sentence, Valence, Arousal

Usage:
    python emotion_plot.py \\
        --seq_dir  Paper_Results/Emotion_Reports/Raw_Sequences \\
        --output_dir Paper_Results/Emotion_Reports/emo_traj
"""

import csv
import re
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None


# Configuration

METHODS = ["RAF_NoCritic", "RAF_Critic", "AVL_NoCritic", "AVL_Critic"]

METHOD_COLORS = {
    "RAF_NoCritic": "#4C72B0",
    "RAF_Critic":   "#1A4A8A",
    "AVL_NoCritic": "#C44E52",
    "AVL_Critic":   "#8A1A1E",
}

N_INTERP   = 100
INTERP_X   = np.linspace(0, 100, N_INTERP)
SMA_WINDOW = 10   # 10% of N_INTERP — non-parametric sliding window

# ── Set the curves to plot. Empty set() means no filter (plot all curves). ──
TARGET_CURVES = {"Curve_2"}   # e.g. {"Curve_1", "Curve_3"}


def smooth_sma(arr):
    """Simple Moving Average with a 10-point (10%) sliding window.
    Uses 'same' convolution so output length equals input length;
    edges are handled by the smaller effective window near boundaries.
    """
    kernel = np.ones(SMA_WINDOW) / SMA_WINDOW
    return np.convolve(arr, kernel, mode="same")


# Helpers 

def interpolate_sequence(values):
    """Resample a variable-length sequence to N_INTERP points on 0–100% axis."""
    n = len(values)
    if n == 0:
        return np.full(N_INTERP, 0.5)
    if n == 1:
        return np.full(N_INTERP, values[0])
    x_orig = np.linspace(0, 100, n)
    raw = np.interp(INTERP_X, x_orig, values)
    return smooth_sma(raw)


# CSV loading 

def load_sequence_csv(path):
    """Return (valences, arousals) as lists of floats from a _sequence.csv file."""
    valences, arousals = [], []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                valences.append(float(row["Valence"]))
                arousals.append(float(row["Arousal"]))
            except (KeyError, ValueError):
                continue
    return valences, arousals


def discover_sequences(seq_dir):
    """
    Walk seq_dir and collect all *_sequence.csv files.

    Expected structure:
        <seq_dir>/<method>/<theme>/<genre>/<novel>/<route>_sequence.csv

    Returns a list of dicts:
        {method, theme, genre, novel, curve, route, valences, arousals}
    """
    seq_dir = Path(seq_dir)
    records = []

    csv_files = sorted(seq_dir.rglob("*_sequence.csv"))
    if not csv_files:
        print(f"[Warning] No *_sequence.csv files found under: {seq_dir}")
        return records

    it = tqdm(csv_files, desc="Loading CSVs") if tqdm else csv_files

    for csv_path in it:
        try:
            rel = csv_path.relative_to(seq_dir)
        except ValueError:
            continue

        parts = rel.parts   # method / theme / genre / novel / filename
        if len(parts) < 5:
            print(f"  [Skip] Unexpected path depth: {csv_path}")
            continue

        method = parts[0]
        theme  = parts[1]
        genre  = parts[2]
        novel  = parts[3]
        route  = csv_path.stem.replace("_sequence", "")

        if method not in METHODS:
            print(f"  [Skip] Unknown method '{method}': {csv_path}")
            continue

        m = re.search(r"Curve_(\d+)", novel, re.IGNORECASE)
        curve = f"Curve_{m.group(1)}" if m else "unknown"

        valences, arousals = load_sequence_csv(csv_path)
        if len(valences) < 2:
            print(f"  [Skip] Too few sentences ({len(valences)}): {csv_path}")
            continue

        records.append({
            "method":   method,
            "theme":    theme,
            "genre":    genre,
            "novel":    novel,
            "curve":    curve,
            "route":    route,
            "valences": valences,
            "arousals": arousals,
        })

    print(f"  Loaded {len(records)} routes from {seq_dir}")
    return records


# Plotting

def _style():
    plt.style.use("seaborn-v0_8-darkgrid")


def plot_route_trajectory(valences, arousals, title, out_path):
    """
    Single route: separate Valence and Arousal figures.
    Background: scatter plot of raw per-sentence scores (alpha=0.3).
    Foreground: SMA-smoothed line interpolated to 100 points.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    base = out_path.parent / out_path.stem
    for values, color, dim in [
        (valences, "#4C72B0", "Valence"),
        (arousals, "#C44E52", "Arousal"),
    ]:
        smoothed = interpolate_sequence(values)
        x_raw    = np.linspace(0, 100, len(values))
        _style()
        fig, ax = plt.subplots(figsize=(10, 4))
        # Background: raw sentence scores as scatter
        ax.scatter(x_raw, values, color=color, alpha=0.3, s=12, linewidths=0)
        # Foreground: smoothed line
        ax.plot(INTERP_X, smoothed, color=color, linewidth=2)
        ax.axhline(0.5, color="gray", linewidth=0.8, linestyle="--", alpha=0.6)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.set_xlabel("Story Progress (%)", fontsize=10)
        ax.set_ylabel(f"{dim} Score", fontsize=10)
        ax.set_title(f"{title} — {dim}", fontweight="bold", fontsize=10)
        plt.tight_layout()
        plt.savefig(f"{base}_{dim}.png", dpi=150)
        plt.close(fig)


# Main generation logic 

def generate_all_plots(records, out_root):
    out_root = Path(out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    # Filter to TARGET_CURVES if specified
    if TARGET_CURVES:
        records = [r for r in records if r["curve"] in TARGET_CURVES]
        print(f"  [Filter] Curves: {sorted(TARGET_CURVES)} → {len(records)} routes remaining")
        if not records:
            print("[Error] No routes match TARGET_CURVES. Check the constant at the top of the file.")
            return

    print(f"\nRoute-level trajectory plots...")
    for rec in records:
        out_path = (out_root / "Route"
                    / rec["method"] / rec["theme"] / rec["genre"] / rec["novel"]
                    / f"{rec['route']}_trajectory.png")
        plot_route_trajectory(
            rec["valences"], rec["arousals"],
            title=f"{rec['method']} | {rec['novel']} | {rec['route']}",
            out_path=out_path,
        )
    print(f"   Done — {len(records)} routes")
    print(f"\n[Done] All plots saved to: {out_root.resolve()}")
    print("Output structure:")
    print("  Route/<method>/<theme>/<genre>/<novel>/  — per-route Valence + Arousal trajectory")


def main():
    parser = argparse.ArgumentParser(
        description="Re-generate route-level trajectory plots from pre-computed sequence CSVs.")
    parser.add_argument("--seq_dir", required=True,
                        help="Path to Raw_Sequences/ directory")
    parser.add_argument("--output_dir", default="Trajectories_replot",
                        help="Output directory for plots (default: Trajectories_replot)")
    args = parser.parse_args()

    records = discover_sequences(args.seq_dir)
    if not records:
        print("[Error] No valid sequence CSVs loaded. Check --seq_dir path.")
        return

    generate_all_plots(records, args.output_dir)


if __name__ == "__main__":
    main()