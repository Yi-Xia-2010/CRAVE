import os
import json
import time
import glob
import argparse
import hashlib
import re

from utils import (
    get_api_key, 
    load_prompt_template, 
    call_gpt_api, 
    MODEL_LOGIC,
    sanitize_filename 
)


MAX_LABEL_LENGTH = 30 

def get_latest_file(pattern):
    files = glob.glob(pattern, recursive=True)
    if not files: return None
    return max(files, key=os.path.getmtime)

def get_latest_outline_corrected(base_dir):

    corrected_pattern = os.path.join(base_dir, "**", "story_outline_*_CORRECTED.json")
    files = glob.glob(corrected_pattern, recursive=True)
    if files: return max(files, key=os.path.getmtime)
    
    normal_pattern = os.path.join(base_dir, "**", "story_outline_*.json")
    files = glob.glob(normal_pattern, recursive=True)
    if not files: return None
    return max(files, key=os.path.getmtime)

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_context_signature(ancestor_ids):

    if not ancestor_ids: return "Start"
    path_str = "-".join(map(str, ancestor_ids))
    return hashlib.md5(path_str.encode('utf-8')).hexdigest()[:6]

def extract_character_names(world_data):
    if not world_data: return "No official names provided."
    lines = []
    main_chars = world_data.get('main_characters', [])
    if main_chars:
        lines.append("MAIN CHARACTERS:")
        for c in main_chars:
            lines.append(f"- {c.get('name', 'Unknown')} ({c.get('role', '')})")
    return "\n".join(lines)

def smart_truncate(text, max_length=2000):
    if len(text) <= max_length: return text
    buffer_len = int(max_length * 1.2)
    chunk = text[-buffer_len:]
    paragraph_idx = chunk.find('\n\n')
    if paragraph_idx != -1 and paragraph_idx < (buffer_len - max_length):
        return chunk[paragraph_idx+2:].strip()
    return text[-max_length:]

def clean_title_strict(title):
    if not title: return ""
    return str(title).strip().lower().rstrip('.,;!?')

def load_clean_draft(filepath):

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        start_idx = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("#") or not stripped: continue
            else:
                start_idx = i
                break
        return "".join(lines[start_idx:])
    except Exception as e:
        print(f"[WARN] Failed to load draft {filepath}: {e}")
        return None


def calculate_chapter_filename(chapter_id, branch_name, context_signature, variant_suffix=""):

    # 1. Sanitize using utils function
    safe_branch = sanitize_filename(branch_name)
    
    # 2. Construct filename
    fname = f"script_ch{chapter_id}_{safe_branch}{variant_suffix}_ctx_{context_signature}.txt"
    
    # 3. Length protection
    if len(fname) > 120:
        short_branch = safe_branch[:10]
        fname = f"script_ch{chapter_id}_{short_branch}{variant_suffix}_ctx_{context_signature}.txt"
        if len(fname) > 120:
             fname = f"script_ch{chapter_id}_long{variant_suffix}_ctx_{context_signature}.txt"
             
    return fname

def smart_resolve_target_id(option, chapter_lookup):

    raw_id = option.get('target_chapter_id') or option.get('target_chapter_index')
    target_title = option.get('target_chapter_title')
    
    # 1. Handle null or -1
    if raw_id is None or str(raw_id) == "-1": 
        return -1
        
    # 2. Try parsing as integer
    try:
        raw_id_int = int(raw_id)
        if raw_id_int in chapter_lookup:
            return raw_id_int
    except (ValueError, TypeError):
        pass
            
    # 3. Fallback: fuzzy matching by title
    if target_title:
        clean_target = clean_title_strict(target_title)
        for ch_id, ch_data in chapter_lookup.items():
            if clean_title_strict(ch_data.get('chapter_title', '')) == clean_target:
                return ch_id
            
    return -1 # Default to Ending


def build_dynamic_context(current_id, path_ids, chapter_lookup, scripts_dir):
    context_text = ""
    try:
        current_index = path_ids.index(current_id)
        ancestor_ids = path_ids[:current_index]
    except ValueError: return "Context Error."

    if not ancestor_ids: return "This is the opening chapter. No history."

    for anc_id in ancestor_ids:
        # Robust ID handling for ancestor lookup
        try: anc_id_int = int(anc_id)
        except: anc_id_int = anc_id

        chapter_header = f"CHAPTER ID {anc_id}"
        
        # 1. Try to read full generated script
        wildcard = os.path.join(scripts_dir, f"script_ch{anc_id}_*.txt")
        found_backups = glob.glob(wildcard)
        file_content = None
        
        if found_backups:
            latest = max(found_backups, key=os.path.getmtime)
            try: 
                with open(latest, 'r', encoding='utf-8') as f: file_content = f.read()
            except: pass

        if file_content:
            context_text += f"\n\n=== [PAST LOG] {chapter_header} (FULL TRANSCRIPT) ===\n"
            context_text += smart_truncate(file_content, 1500)
            context_text += "\n=== [END LOG] ===\n"
        
        # 2. Fallback to Outline Summary (Prioritizing narrative_focus)
        elif anc_id_int in chapter_lookup:
            try:
                data = chapter_lookup[anc_id_int]
                context_text += f"\n=== {chapter_header} (SUMMARY ONLY) ===\n"
                
                summary = (data.get('narrative_focus') or 
                           data.get('summary') or 
                           data.get('story_beat') or 
                           data.get('scene_goal'))
                
                if summary:
                    context_text += f"Summary: {summary}\n"
            except: pass

    return context_text

def extract_last_scene_context(previous_ch_id, scripts_dir):
    pattern = os.path.join(scripts_dir, f"script_ch{previous_ch_id}_*.txt")
    files = glob.glob(pattern)
    if files:
        latest = max(files, key=os.path.getmtime)
        try:
            with open(latest, 'r', encoding='utf-8') as f:
                content = f.read()
                clean_context = smart_truncate(content, max_length=2000)
                return f"**ACTUAL ENDING OF PREVIOUS CHAPTER (Transcript):**\n...\n{clean_context}"
        except: pass
    return "The story starts here."

def get_next_chapter_info(ch_data, chapter_lookup, current_ch_id):
    decision = ch_data.get('major_decision_point', {})
    
    # Case A: Branching
    if decision.get('has_choice'):
        options = decision.get('options', [])
        previews = []
        target_ids = []
        
        for opt in options:
            tid = smart_resolve_target_id(opt, chapter_lookup)
            label = opt.get('label', 'Option')
            target_ids.append(str(tid))
            
            if tid and str(tid) != "-1":
                t_obj = chapter_lookup.get(int(tid))
                t_title = t_obj.get('chapter_title', 'Unknown') if t_obj else f"ID {tid}"
                previews.append(f"- Option '{label}': Leads to '{t_title}'")
            else:
                previews.append(f"- Option '{label}': Leads to a Narrative Ending.")

        is_convergent = len(set(target_ids)) == 1 and len(target_ids) > 1
        
        if is_convergent:
            header = "**UPCOMING FLAVOR CHOICES (Convergent Path):**\n"
            header += "(Instruction: These options lead to the same destination. Focus on the character's reaction/personality differences.)\n"
        else:
            header = "**UPCOMING BRANCHES:**\n"
            
        return header + "\n".join(previews)

    # Case B: Linear
    else:
        def_next = ch_data.get('default_next_chapter_id') or ch_data.get('default_next_chapter')
        
        if def_next and int(def_next) != -1:
            t_obj = chapter_lookup.get(int(def_next))
            if t_obj:
                t_title = t_obj.get('chapter_title', 'Untitled')
                t_idx = t_obj.get('chapter_index', def_next)
                return f"**LINEAR TRANSITION TO:** Chapter {t_idx}: {t_title}"
            return f"**LINEAR TRANSITION TO:** Chapter ID {def_next}"
            
        # Case C: Finale
        return "End of Outline. (FINALE - Deliver a sense of closure.)"

def extract_decision_data(ch_data):
    # Copy decision data and sanitize
    decision = ch_data.get('major_decision_point', {}).copy()
    
    if decision.get('has_choice'):
        clean_opts = []
        for opt in decision.get('options', []):
            clean_opts.append({
                "label": opt.get('label', opt.get('option_label')),
                "target_chapter_id": opt.get('target_chapter_id') or opt.get('target_chapter_index'),
                "target_chapter_index": opt.get('target_chapter_index'),
                "target_chapter_title": opt.get('target_chapter_title'),
                "router_logic": opt.get('router_logic', 'Personality focus')
            })
        decision['options'] = clean_opts
    
    # Inject root default ID for linear transitions
    if 'default_next_chapter' in ch_data:
        decision['root_default_next_chapter'] = ch_data['default_next_chapter']
    elif 'default_next_chapter_id' in ch_data:
        decision['root_default_next_chapter'] = ch_data['default_next_chapter_id']
        
    return decision

def has_routing_table(filepath):
    if not os.path.exists(filepath): return False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return ">>> SYSTEM ROUTING TABLE <<<" in content
    except: return False

def append_routing_info(output_path, ch_id, decision_data, topology, current_ancestor_ids, chapter_lookup, single_ending_id=None):
    if has_routing_table(output_path):
        print(f"      [INFO] Routing table exists. Skipped.")
        return
    
    registry = topology.get('chapter_topology', {})
    
    def get_target_branch_real(tid):
        try: tid_int = int(tid)
        except: tid_int = tid
        
        # 1. Try looking up in Outline
        if tid_int in chapter_lookup:
            return chapter_lookup[tid_int].get('branch_designation', 'Unknown')
            
        # 2. Fallback to Topology
        tid_str = str(tid)
        return registry.get(tid_str, {}).get('branch', 'Unknown') if tid_str in registry else "Unknown"

    info_block = "\n\n" + "="*60 + "\n>>> SYSTEM ROUTING TABLE <<<\n\n"
    
    def predict_target_filename(target_id):
        real_branch = get_target_branch_real(target_id)
        next_ancestors = current_ancestor_ids + [ch_id]
        next_sig = generate_context_signature(next_ancestors)
        
        suffix = ""
        if single_ending_id is not None and str(target_id) == str(single_ending_id):
            suffix = f"_Ending_from_Ch{ch_id}"
            
        return calculate_chapter_filename(target_id, real_branch, next_sig, suffix)

    # Routing Table Generation
    if decision_data.get('has_choice') and decision_data.get('options'):
        info_block += "[DECISION POINT]\n"
        options = decision_data.get('options', [])
        
        for i, opt in enumerate(options):
            option_num = i + 1
            label = opt.get('label', 'Unknown')
            tid = smart_resolve_target_id(opt, chapter_lookup)
            
            if len(label) > 60: label = label[:57] + "..."
            
            info_block += f"Option {option_num}: \"{label}\""
            
            if not tid or str(tid) == "-1":
                info_block += " -> [GAME OVER / ENDING]\n"
            else:
                real_branch = get_target_branch_real(tid)
                target_file = predict_target_filename(tid)
                info_block += f" -> ID {tid} ({real_branch})\n"
                info_block += f"    > Jump Target File: {target_file}\n"
    else:
        def_next = (decision_data.get('root_default_next_chapter') or 
                    decision_data.get('default_next_chapter_id') or 
                    decision_data.get('default_next_chapter'))
        
        if def_next and int(def_next) != -1:
             tid = int(def_next)
             target_file = predict_target_filename(tid)
             info_block += f"[LINEAR] -> ID {tid}\n    > Jump Target File: {target_file}\n"
        else:
             info_block += "[FINAL CHAPTER] -> No further transitions.\n"
        
    try:
        with open(output_path, 'a', encoding='utf-8') as f: 
            f.write(info_block)
    except Exception as e:
        print(f"[ERROR] Writing routing table to {output_path}: {e}")

def run_step_4_draft(api_key, world_str, theme, genre, ch_data, history_str, last_scene_ctx, decision_data, next_chapter_info, existing_draft=None):

    if existing_draft:
        print(f"      [SKIP] Using loaded draft checkpoint.")
        return existing_draft

    writer_sys = load_prompt_template("prompts/ScriptWriter_Sys.txt")
    writer_user_tmpl = load_prompt_template("prompts/ScriptWriter_User.txt")
    
    if not writer_sys or not writer_user_tmpl: return None

    # [SAFETY CHECK] Verify prompt template
    if "{visual_anchors}" in writer_user_tmpl:
        print("\n[CRITICAL ERROR] 'visual_anchors' found in prompts/ScriptWriter_User.txt!")
        print("Please REMOVE {visual_anchors} and ADD {narrative_focus} to your text file.\n")
        return None

    print(f"      ...Running Writer (Drafting)...")
    try:
        # Prepare arguments for prompt
        writer_user = writer_user_tmpl.format(
            theme = theme,
            genre = genre,
            world_setting=world_str,
            previous_context=history_str,
            last_scene_context=last_scene_ctx,
            chapter_detail=json.dumps(ch_data, indent=2, ensure_ascii=False),
            Valance=ch_data.get('Valance', 'Neutral'),
            Arousal=ch_data.get('Arousal', 'Neutral'),
            narrative_focus=ch_data.get('narrative_focus', ch_data.get('summary', 'Develop story based on context.')),
            chapter_id=ch_data.get('id', '??'),
            chapter_title=ch_data.get('chapter_title', 'Untitled'),
            decision_logic=json.dumps(decision_data, indent=2, ensure_ascii=False),
            next_chapter_info=next_chapter_info
        )
        draft_text = call_gpt_api(api_key, writer_sys, writer_user, MODEL_LOGIC, json_mode=False)
        return draft_text
    except Exception as e:
        print(f"[ERROR] Writer Prompt: {e}")
        return None


def run_step_4_parse(api_key, draft_text, character_list_str, decision_data, next_chapter_info):

    if not draft_text: return None

    print(f"      ...Running Parser (Formatting Script)...")
    parser_sys = load_prompt_template("prompts/ScriptParser_Sys.txt")
    parser_user_tmpl = load_prompt_template("prompts/ScriptParser_User.txt")
    
    if not parser_sys: 
        return draft_text 

    try:
        parser_user = parser_user_tmpl.format(
            character_names=character_list_str,
            draft_text=draft_text,
            decision_logic=json.dumps(decision_data, indent=2, ensure_ascii=False),
            next_chapter_info=next_chapter_info
        )
    except:
        parser_user = f"Convert this draft to script:\n{draft_text}"

    final_script = call_gpt_api(api_key, parser_sys, parser_user, MODEL_LOGIC, json_mode=False)
    return final_script

def validate_script_integrity(scripts_dir):
    print("\n[System Integrity Check]")
    print("-" * 30)
    
    script_files = glob.glob(os.path.join(scripts_dir, "script_ch*.txt"))
    if not script_files: return

    errors_found = 0
    for sp in script_files:
        with open(sp, 'r', encoding='utf-8') as f: content = f.read()
        targets = re.findall(r"> Jump Target File: (script_ch.+?\.txt)", content)
        for target_fname in targets:
            target_path = os.path.join(scripts_dir, target_fname)
            if not os.path.exists(target_path):
                print(f"[ERROR] Broken Link: {os.path.basename(sp)} -> Missing {target_fname}")
                errors_found += 1
    
    if errors_found == 0:
        print("[OK] All links verified.")
    else:
        print(f"[WARN] Found {errors_found} broken links.")

def main():
    parser = argparse.ArgumentParser(description="Step 4: Generate VN Scripts")
    parser.add_argument("--theme", type=str, required=True, help="Story theme (e.g. Climate_Change)")
    parser.add_argument("--genre", type=str, required=True, help="Story genre (e.g. Detective)")
    parser.add_argument("--id", type=str, required=True)
    parser.add_argument("--project_path", type=str, help="Specific world folder")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key: return

    if args.project_path:
        topo_file = os.path.join(args.project_path, "project_topology.json")
    else:
        topo_file = get_latest_file(os.path.join("results", "**", "project_topology.json"))

    if not topo_file: return
    world_dir = os.path.dirname(topo_file)
    
    outline_file = get_latest_outline_corrected(world_dir)
    if not outline_file:
        print("[ERROR] Outline file not found.")
        return
        
    print(f"Data Source: {os.path.basename(outline_file)}")
    outline_source_data = load_json(outline_file)
    
    chapters_raw = outline_source_data.get('chapter_structure', [])

    # ARC TYPE USED FOR JUDGE - Story Type
    story_type = outline_source_data.get('_meta_arc_strategy', 'Follow the story type of the story outline.')
    
    # Build global chapter lookup (Golden Source)
    # [ROBUSTNESS FIX] Ensure ID is int for lookup key where possible
    chapter_lookup = {}
    for c in chapters_raw:
        cid = c.get('id') or c.get('chapter_index')
        try: chapter_lookup[int(cid)] = c
        except: chapter_lookup[cid] = c
    
    scripts_dir = os.path.join(world_dir, "Scripts_Text")
    drafts_dir = os.path.join(scripts_dir, "Drafts")
    os.makedirs(scripts_dir, exist_ok=True)
    os.makedirs(drafts_dir, exist_ok=True)

    topology = load_json(topo_file)
    world_file = get_latest_file(os.path.join(world_dir, "world_setting_*.json"))
    
    world_str = "{}"
    character_list_str = "No official names available."
    if world_file:
        with open(world_file, 'r', encoding='utf-8') as f:
            world_str = f.read()
            try: character_list_str = extract_character_names(json.loads(world_str))
            except: pass
            
    routes = topology.get('routes', [])

    # --- Pre-Scan for Single Ending Convergence ---
    all_end_ids = set()
    for r in routes:
        path = r.get('path')
        if path: all_end_ids.add(path[-1])
    
    single_ending_id = None
    if len(all_end_ids) == 1:
        single_ending_id = list(all_end_ids)[0]
        print(f"Single ending convergence detected (ID {single_ending_id}). Variant links enabled.")
    else:
        print(f"Multiple endings detected. Variant links disabled.")

    # --- Main Loop ---
    for i, route in enumerate(routes):
        path_ids = route.get('path')
        if not path_ids: continue
        route_name = route.get('branch_name', 'Unknown')
        print(f"\nProcessing Route #{i+1}: {route_name}")

        for curr_idx, ch_id in enumerate(path_ids):
            # [ROBUSTNESS FIX] Handle String vs Int ID mismatch
            try: lookup_id = int(ch_id)
            except: lookup_id = ch_id
            
            if lookup_id not in chapter_lookup: 
                print(f"   [WARN] ID {ch_id}: Data missing in Outline.")
                continue
            
            ch_data = chapter_lookup[lookup_id]
            ancestor_ids = path_ids[:curr_idx]
            signature = generate_context_signature(ancestor_ids)
            raw_branch = ch_data.get('branch_designation', 'Common')
            
            # --- Variant Logic ---
            variant_suffix = ""
            ending_instruction = ""
            is_last_node = (curr_idx == len(path_ids) - 1)
            
            if single_ending_id and is_last_node and curr_idx > 0:
                prev_id = path_ids[curr_idx-1]
                variant_suffix = f"_Ending_from_Ch{prev_id}"
                
                prev_branch = "Unknown"
                # Lookup prev_id defensively
                try: prev_id_int = int(prev_id)
                except: prev_id_int = prev_id
                
                if prev_id_int in chapter_lookup:
                    prev_d = chapter_lookup[prev_id_int]
                    prev_branch = prev_d.get('branch_designation', 'Unknown')
                
                ending_instruction = (
                    f"\n\n*** CRITICAL ENDING INSTRUCTION ***\n"
                    f"This is the SHARED FINAL CHAPTER (Epilog).\n"
                    f"The player arrived here specifically from the '{prev_branch}' route (Chapter {prev_id}).\n"
                    f"You MUST write this ending variation to reflect the consequences of that specific path.\n"
                )
                print(f"   -> Variant ending from Ch {prev_id} ({prev_branch})")

            # --- Filename Generation ---
            output_filename = calculate_chapter_filename(ch_id, raw_branch, signature, variant_suffix)
            output_path = os.path.join(scripts_dir, output_filename)

            # --- Context Construction ---
            history_str = build_dynamic_context(ch_id, path_ids, chapter_lookup, scripts_dir)
            history_str += ending_instruction 
            
            last_scene_ctx = "Story begins."
            if curr_idx > 0:
                last_scene_ctx = extract_last_scene_context(path_ids[curr_idx-1], scripts_dir)
            
            # --- Extract Decisions ---
            auth_decision = extract_decision_data(ch_data)
            next_chapter_info = get_next_chapter_info(ch_data, chapter_lookup, ch_id)

            # --- Force Ending Logic ---
            final_decision_data = auth_decision.copy() 

            if is_last_node:
                print(f"   [INFO] Ch {ch_id}: Final node. Forcing FINALE mode.")
                
                final_decision_data['has_choice'] = False
                final_decision_data['options'] = []
                final_decision_data['default_next_chapter'] = None
                final_decision_data['root_default_next_chapter'] = None
                
                next_chapter_info = (
                    "**STATUS: FINALE**\n"
                    "This is the final chapter of the route. There are no further options.\n"
                    "INSTRUCTION: Write a conclusive ending with emotional closure. Do NOT write any 'Options' or 'To be continued'."
                )

            # --- Draft Check ---
            draft_filename = f"draft_{output_filename}"
            draft_path = os.path.join(drafts_dir, draft_filename)
            existing_draft = None
            if os.path.exists(draft_path):
                print(f"      [LOAD] Found draft: {draft_filename}")
                existing_draft = load_clean_draft(draft_path)

            if os.path.exists(output_path):
                print(f"   [Ch {ch_id}] Exists. Skipping.")
                continue

            print(f"   [Ch {ch_id}] Generating...")
        
            num_generations = 1
            for i in range(num_generations):
                res_draft = run_step_4_draft(
                    api_key, world_str, args.theme, args.genre, ch_data, history_str, 
                    last_scene_ctx, final_decision_data, next_chapter_info,
                    existing_draft=existing_draft
                )

            # NEW: PARSE ONLY THE BEST DRAFT
            res_script = run_step_4_parse(
                api_key, res_draft, character_list_str, final_decision_data, next_chapter_info
            )
            

            if res_draft and not existing_draft:
                with open(draft_path, 'w', encoding='utf-8') as f:
                    f.write(f"### DRAFT\n# Route: {route_name}\n{ending_instruction}\n\n" + res_draft)

            if res_script:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"### SCRIPT\n# Route: {route_name}\n# Context: {signature}\n\n" + res_script)
                
                append_routing_info(
                    output_path, 
                    ch_id, 
                    final_decision_data,  
                    topology, 
                    ancestor_ids, 
                    chapter_lookup,
                    single_ending_id=single_ending_id
                )
                print(f"      Saved and linked.")

            time.sleep(1)
            
    validate_script_integrity(scripts_dir)

if __name__ == "__main__":
    main()