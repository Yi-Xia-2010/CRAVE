import os
import json
import glob
import datetime
import argparse
import re
from utils import (
    get_api_key, 
    load_prompt_template, 
    call_gpt_api, 
    save_json_file, 
    sanitize_filename, 
    MODEL_LOGIC
)
from judge import StoryJudge


ARC_TYPES = {
    "0": "Auto-Select",
    "1": "Rags to Riches (Rise)",
    "2": "Tragedy (Fall)",
    "3": "Man in a Hole (Fall-Rise)",
    "4": "Icarus (Rise-Fall)",
    "5": "Cinderella (Rise-Fall-Rise)",
    "6": "Oedipus (Fall-Rise-Fall)"
}

ARC_DESCRIPTIONS = {
    "1": "Progress, overcoming obstacles, and gaining strength.",
    "2": "New failures, losses, or tragic mistakes leading to a nadir.",
    "3": "Fall into crisis, struggles at the bottom, then recovery.",
    "4": "Rapid rise to a peak of success, then a catastrophic crash.",
    "5": "Rise to a temporary peak, sudden drop, then achieve permanent victory.",
    "6": "Fall into a problem, solve it temporarily, but leads to ultimate doom."
}



def get_latest_world_setting_in_folder(folder):
    search_pattern = os.path.join(folder, "world_setting_*.json")
    files = glob.glob(search_pattern)
    if not files: return None
    return max(files, key=os.path.getmtime)

def get_latest_world_setting_global():
    search_pattern = os.path.join("results", "**", "world_setting_*.json")
    files = glob.glob(search_pattern, recursive=True)
    if not files: return None
    return max(files, key=os.path.getmtime)

def extract_json(text):
    if not text: return None
    try:
        return json.loads(text)
    except:
        match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
        if match: return json.loads(match.group(1))
        return None


def run_step_2_two_stage(api_key, world_data, arc_key, theme, genre,id, chapters_count="6"):
    arc_name = ARC_TYPES.get(arc_key, "Auto-Select")
    arc_desc = ARC_DESCRIPTIONS.get(arc_key, "Analyze the world setting and choose the best fit.")
    
    print(f"   Strategy: {arc_name}")
    drafts = []

    for i in range(3):
        # Stage 1: Drafting
        writer_sys_tmpl = load_prompt_template("prompts/StoryOutline_Writer_Sys.txt")
        writer_user_tmpl = load_prompt_template("prompts/StoryOutline_Writer_User.txt")
        
        if not writer_sys_tmpl or not writer_user_tmpl: return None, None

        try:
            writer_sys = writer_sys_tmpl
        except:
            writer_sys = writer_sys_tmpl

        writer_user = writer_user_tmpl.format(
            world_setting_json=json.dumps(world_data, indent=2, ensure_ascii=False),
            selected_arc_type_name=arc_name,
            arc_definition_description=arc_desc,
            chapters=chapters_count,
            story_type = arc_name, 
            game_theme = theme, 
            genre = genre,
            length=world_data.get('estimated_story_length', '6000 words')
        )
        
        raw_draft = call_gpt_api(api_key, writer_sys, writer_user, MODEL_LOGIC, json_mode=False)
        if not raw_draft: return None, None
        drafts.append(raw_draft)

    
    story_type = ARC_TYPES.get(arc_key, "Auto-Select")
    judge = StoryJudge(role="Story_outline_judge", model=MODEL_LOGIC)
    best_outline_index = judge.judging(drafts, story_type, genre, id)
    raw_draft = drafts[best_outline_index]

    # Stage 2: Parsing
    parser_sys = load_prompt_template("prompts/StoryOutline_Parser_Sys.txt")
    parser_user_tmpl = load_prompt_template("prompts/StoryOutline_Parser_User.txt")
    if not parser_sys or not parser_user_tmpl: return None, raw_draft

    parser_user = parser_user_tmpl.format(draft_text=raw_draft)
    json_str = call_gpt_api(api_key, parser_sys, parser_user, MODEL_LOGIC, json_mode=True)
    return json_str, raw_draft


def main():
    parser = argparse.ArgumentParser(description="Step 2: Generate Story Outline")
    parser.add_argument("--arc", type=str, default='0')
    parser.add_argument("--theme", type=str, required=True, help="Story theme (e.g. Cyberpunk)")
    parser.add_argument("--genre", type=str, required=True, help="Story genre (e.g. Detective)")
    parser.add_argument("--id", type=str, required=True)
    parser.add_argument("--no-input", action="store_true")
    parser.add_argument("--project_path", type=str, help="Specific world folder to process")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key: return


    if args.project_path:
        world_dir = args.project_path
        world_filepath = get_latest_world_setting_in_folder(world_dir)
    else:
        world_filepath = get_latest_world_setting_global()

    if not world_filepath:
        print("Error: No world setting found.")
        return
    
    world_dir = os.path.dirname(world_filepath)
    ws_filename = os.path.basename(world_filepath)
    
    print(f"Target Project: {world_dir}")

    corrected_files = glob.glob(os.path.join(world_dir, "*_CORRECTED.json"))
    if corrected_files and not args.no_input:
        print("\n WARNING: A '_CORRECTED' outline already exists in this folder!")
        print("   Generating a new outline now will create a parallel version and might cause confusion.")
        print("   The pipeline usually relies on the corrected version.")
        confirm = input("   Are you sure you want to GENERATE NEW OUTLINE? (y/N): ").strip().lower()
        if confirm != 'y':
            print(" Aborted by user.")
            return
    
    with open(world_filepath, 'r', encoding='utf-8') as f:
        world_data = json.load(f)

    arc_choice = args.arc
    if not args.no_input and arc_choice == '0':
        print("\nSelect Narrative Arc (0-6):")
        inp = input("Choice [0]: ").strip()
        if inp in ARC_TYPES: arc_choice = inp

    chapters_val = str(world_data.get('estimated_chapters', '6'))
 
    json_str, raw_draft = run_step_2_two_stage(api_key, world_data, arc_choice, args.theme, args.genre, args.id,chapters_count=chapters_val)
    
    if json_str:
        outline_data = extract_json(json_str)
        if outline_data:
            outline_data["_meta_source_world"] = ws_filename
            outline_data["_meta_arc_strategy"] = ARC_TYPES[arc_choice]

            raw_arc_name = ARC_TYPES[arc_choice].split()[0]
            safe_arc = re.sub(r'_+', '_', sanitize_filename(raw_arc_name)).strip('_')
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"story_outline_{safe_arc}_{timestamp}.json"
            
            save_json_file(outline_data, world_dir, filename)
            
            if raw_draft:
                draft_filename = filename.replace('.json', '_draft.txt')
                with open(os.path.join(world_dir, draft_filename), 'w', encoding='utf-8') as f:
                    f.write(raw_draft)

            print(f"Outline Saved: {filename}")
            print(f"Next Step: Run Step 2.5 (Structure Analyzer) to fix IDs and generate Topology.")
        else:
            print("Error parsing JSON.")

if __name__ == "__main__":
    main()