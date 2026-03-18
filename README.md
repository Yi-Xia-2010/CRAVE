# CRAVE: A <u>C<u>ritic-<u>R<u>efined <u>A<u>ffective <u>V<u>isual Novel <u>E<u>ngine via Fine-Grained Affective Guidance
This repository is for the paper "CRAVE: A <u>C<u>ritic-<u>R<u>efined <u>A<u>ffective <u>V<u>isual Novel <u>E<u>ngine via Fine-Grained Affective Guidance"

If you encounter a filename issue, see the Notes part.
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
                ├── judging_drafts/     #candidates for Critic to select
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

Runs Steps 1–4 (world setting → outline → topology → text scripts) for multiple cases in sequence. Theme, genre, and the set of Curve IDs to run are configured by editing the constants at the top of the script.

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

Step 5 and 6 are not included in CRAVE. For Step 5 and 6, run the `parse.py` and `convert.py` in the Evaluation foleder.
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

### ⚠️ For Windows Users: "Filename too long" Error

When cloning this repository on Windows, you might encounter a `Filename too long` error. This happens because the project contains deep directory structures that exceed the default Windows path length limit (260 characters), combined with Git's default security settings.

You can easily resolve this issue using one of the two methods below:

#### Method 1: Enable Git Long Paths Support (Recommended)

**If you are using the Git CLI:**
Open your terminal (PowerShell or Command Prompt) as an Administrator and run the following command:
`bash
git config --system core.longpaths true
`

**If you are strictly using GitHub Desktop (without a standalone Git installation):**
1. Press `Win + R`, type `%USERPROFILE%`, and press Enter to open your user home directory.
2. Locate the `.gitconfig` file and open it with Notepad.
3. Add the following configuration to the bottom of the file and save:
   ```text
   [core]
       longpaths = true


#### 📦 If You Downloaded the Repository as a ZIP File

If you chose to **"Download ZIP"** instead of cloning the repository, the built-in Windows extraction tool might fail or skip files due to the 260-character path limit. 

Here are the two best ways to fix it:

**Solution 1: Use a robust extraction tool (Recommended & Easiest)**
Use a third-party archiving tool like [WinRAR]. Unlike the native Windows Explorer, WinRAR is designed to bypass the 260-character path limit automatically. Simply open the downloaded `.zip` file with WinRAR and extract it.

**Solution 2: Enable Long Path Support in Windows (System-Wide)**
If you are using Windows 10 (version 1607 or later) or Windows 11, you can permanently remove the 260-character limit at the OS level. This will solve extraction issues once and for all.

* **Using PowerShell (Fastest):**
  1. Open the Start menu, search for **Windows PowerShell**, right-click it, and select **Run as administrator**.
  2. Copy and paste the following command, then press Enter:
     ```powershell
     New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
     ```
  3. Restart your computer for the changes to take effect.

* **Using Registry Editor (GUI):**
  1. Press `Win + R`, type `regedit`, and press Enter.
  2. Navigate to `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`.
  3. Double-click the item named `LongPathsEnabled`, change the **Value data** to `1`, and click **OK**.
  4. Restart your computer.



### Others
**Curve ID (1–6)** controls the narrative arc structure applied to the story. The exact definition of each arc is determined internally by `outline_generator.py`.

**Case archives** — `All_Generated_Cases/` contains all test-generated cases (text output only, no image assets.). 

**Evaluation**   
Before each evaluation, please put the foulders with generated cases in each evaluation folder, and run `extract.py` to get each routes files. (Now the cases in All_Generated_Cases already processed by this step.)

In LLMs_as_Judges Evaluation, first run `eval.sh`, then run `eval_stats.py`, finally run `eval_model.py`.  The detailed results are in this Evaluation folder named "Paper_Results". `route_ranking.py` is the script to help select the exemplar following our exemplar selection protocol. 

In Eval_As (Affective Saliency Evaluation), use routes fiels extracted before evaluation, run `eval_as.py`, then `eval_traj.py`.  Before this evaluation, you might need follow their instuctions to deploy this repository: https://github.com/lc0197/emotional_trajectories_stories


## Disclaimer
This project is developed for academic research purposes. Under certain specific prompts, LLMs may generate content that is uncomfortable or poses certain legal risks. We do not recommend that you disseminate the content generated by the project. We are not responsible for the legality, originality, or risk of infringement of the generated content.