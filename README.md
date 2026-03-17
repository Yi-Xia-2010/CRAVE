# CRAVE: A \underline{C}ritic-\underline{R}efined \underline{A}ffective \underline{V}isual Novel \underline{E}ngine via Fine-Grained Affective Guidance
This repository is for the paper "CRAVE: A \underline{C}ritic-\underline{R}efined \underline{A}ffective \underline{V}isual Novel \underline{E}ngine via Fine-Grained Affective Guidance"


---

## Table of Contents

- [Repository Contents](#repository-contents)
- [SENSE Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Pipeline Overview](#pipeline-overview)
- [Output Directory Structure](#output-directory-structure)
- [Notes](#notes)
- [Disclaimer](#Disclaimer)

---

## Repository Contents

| Folder / File | Description |
|---------------|-------------|
| `AVL_WithCritic/` | Arousal and Valence Levels (AVL) guidance variant with the Critic module enabled — core scripts and `prompts/` folder live here |
| `AVL_WithoutCritic/` | Ablation variant of AVL guidance that runs without the Critic module |
| `RAF_WithCritic/` | Rise and Fall (RAF) cue guidance variant with the Critic enabled |
| `RAF_WithoutCritic/` | **Baseline** — Rise and Fall (RAF) cue guidance without the Critic module |
| `All_Generated_Cases/` | Archive of all test-generated cases (text output only, no image assets) |
| `Evaluation/` | Evaluation scripts and results |
| `supplementary_file.pdf` | Supplementary material including detailed statistical test tables, condensed prompts used across pipeline components and stages, and the LLM-as-a-judge evaluation prompt |
| `LICENSE` | Project license |
| `README.md` | This file |

---

## Project Structure

```
AVL_WithCritic/
├── run_all.py                    # Main entry point — runs the full pipeline for all cases
├── world_setting_generator.py    # Step 1: World setting generation
├── outline_generator.py          # Step 2: Story outline generation
├── structure_analyzer.py         # Step 3: Topology analysis & structure correction
├── script_generator.py           # Step 4: Text scripts generation
├── judge.py                      # Critic module — evaluates and critiques generated content
├── utils.py                      # Shared utilities (e.g. sanitize_filename)
├── prompts/                      # Folder containing all prompts for each pipeline step
│
└── results/                      # Root output directory for all generated cases
    └── <Theme>/
        └── <Genre>/
            └── World_Story_1_Curve_<N>/
                ├── world_setting_*.json
                ├── story_outline_*.json
                ├── project_topology.json
                ├── *_CORRECTED.json
                ├── Chapters_Detail/
                ├── Scripts_Text/
                ├── Processed_Scripts/  #output from the parse.py in the Evaluation foleder
                ├── chapter_renpy/      #output from the convert.py in the Evaluation foleder
                └── Story_Routes/       #output from the extract.py in the Evaluation foleder
```
---

## Environment Setup

### Conda Environment

The project uses a dedicated conda environment named `CRAVE` running **Python 3.10.19**. To recreate it, run`environment.yml`:

```bash
conda env create -f environment.yml
```

Then activate the environment before running anything:

```bash
conda activate vn
```

---

## Quick Start

### Batch Generation — Text Scripts Only (Steps 1–4)

```bash
conda activate vn
python run_all.py
```

Runs Steps 1–4 (world setting → outline → topology → text scripts) for multiple cases in sequence. Theme, genre, and the set of Curve IDs to run are configured by editing the constants at the top of the script:

---

## Pipeline Overview

```
Step 1   world_setting_generator     World setting (characters, locations, visual style)
  ↓
Step 2   outline_generator           Story outline (overall arc and branch structure)
  ↓
Step 3   structure_analyzer            Topology analysis (chapter validation & correction)
  ↓
Step 4   script_generator            Dialogue scripts (scene, choice, and interaction tags)
  ↓
Step 5   parse                Script parsing (inserts Character/Background tags, this code is in the Evaluation folder)
  ↓
Step 6   convert              Ren'Py conversion (outputs .rpy files,the code is in the Evaluation folder)
```

Step 5 and 6 are not included in CRAVE.  
To deploy, copy the contents of `chapter_renpy/` into the `game/` directory of a newly created Ren'Py project. And copy the`locations/` and `characters/` into the `game/images/`. 

---

## Output Directory Structure

```
results/<Theme>/<Genre>/World_Curve_<X>_Story_<Y>/
│
├── world_setting_Curve_<X>_Story_<Y>.json   ← World setting (Step 1)
├── story_outline_*.json                   ← Story outline (Step 2)
├── project_topology.json                  ← Chapter topology map (Step 3)
├── *_CORRECTED.json                       ← Corrected outline (Step 3)
│
├── Scripts_Text/                          ← Dialogue scripts (Step 4)
│   └── script_ch<ID>_*.txt
│
├── Processed_Scripts/                     ← Tagged scripts (Step 5)
│   └── script_ch<ID>_*.txt
│
└── chapter_renpy/                         ← Ren'Py project files (Step 6)
    ├── script.rpy
    ├── chapter1.rpy
    ├── chapter2.rpy
    └── ...
```

---

## Notes

**Curve ID (1–6)** controls the narrative arc structure applied to the story. The exact definition of each arc is determined internally by `outline_generator.py`.

**Case archives** — `All_Generated_Cases/` contains all test-generated cases (text output only, no image assets.). 

**Evaluation**   
Before each evaluation, please put the foulders with generated cases in each evaluation folder, and run `extract.py` to get each routes files. (Now the cases in All_Generated_Cases already processed by this step.)

In LLMs_as_Judges Evaluation, first run `eval.sh`, then run `eval_stats.py`, finally run `eval_model.py`.  The detailed results are in this Evaluation folder named "Paper_Results". `route_ranking.py` is the script to help select the exemplar following our exemplar selection protocol. 

In Eval_As (Affective Saliency Evaluation), use routes fiels extracted before evaluation, run `eval_as.py`, then `eval_traj.py`.  Before this evaluation, you might need follow their instuctions to deploy this repository: https://github.com/lc0197/emotional_trajectories_stories


## Disclaimer
This project is developed for academic research purposes. Under certain specific prompts, LLMs may generate content that is uncomfortable or poses certain legal risks. We do not recommend that you disseminate the content generated by the project. We are not responsible for the legality, originality, or risk of infringement of the generated content.