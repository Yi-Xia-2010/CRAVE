import os
import re
import json
import glob
import difflib

zoom_size = 0.7

Char_def = ""
img_def = ""
keys = ["at", "with", "for", "bg", "scene", "[", "(", '"']

# ─────────────────────────────────────────────
# Utility helpers
# ─────────────────────────────────────────────

def chapter_key(filename):
    m = re.search(r'ch(\d+)', filename)
    num = int(m.group(1)) if m else float('inf')
    return (num, filename)

RENPY_RESERVED = {
    'init', 'label', 'menu', 'jump', 'call', 'return', 'show', 'hide',
    'scene', 'play', 'stop', 'pause', 'if', 'elif', 'else', 'while',
    'for', 'pass', 'define', 'default', 'transform', 'style', 'screen',
    'image', 'python', 'with', 'at', 'as', 'onlayer', 'zorder',
    'behind', 'expression', 'voice', 'extend', 'nvl', 'window',
    'narrator', 'name', 'true', 'false', 'none',
}

def sanitize_var_name(name):
    name = name.replace("-", "_").replace(" ", "_")
    name = re.sub(r"[^a-zA-Z0-9_]", "", name)
    name = name.lower()
    if not name:
        return "char_unknown"
    if name[0].isdigit():
        name = "c_" + name
    if name in RENPY_RESERVED:
        name = "char_" + name
    return name

def find_world_setting_file(base_path):
    for path in [base_path, os.path.dirname(base_path)]:
        files = glob.glob(os.path.join(path, "world_setting*.json"))
        if files:
            return files[0]
    return None


# Three-tier target file resolver
def find_target_filename(target_file, actual_files):
    target_lower = target_file.lower().strip()
    # Tier 1: exact
    for f in actual_files:
        if f.lower() == target_lower:
            return f
    # Tier 2: ch-number + route slug (ignores ctx hash)
    m = re.search(r'(ch\d+_[A-Za-z_]+?)_ctx', target_file, re.IGNORECASE)
    if m:
        core = m.group(1).lower()
        candidates = [f for f in actual_files if core in f.lower()]
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            print(f"  [Tier2 ambiguous] '{target_file}' matches {len(candidates)} files — need exact ctx match")
            return None
    # Tier 3: ch-number only (同样只在唯一匹配时使用)
    m = re.search(r'(ch\d+)', target_file, re.IGNORECASE)
    if m:
        ch = m.group(1).lower()
        candidates = [f for f in actual_files
                      if re.search(r'\b' + re.escape(ch) + r'\b', f.lower())]
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            print(f"  [Tier3 ambiguous] '{target_file}' matches {len(candidates)} files — need exact match")
            return None
    return None


# Image / sprite helpers
def get_best_match(character_name, sprite_files):
    name_map = {os.path.splitext(f)[0]: f for f in sprite_files}
    matches = difflib.get_close_matches(character_name, name_map.keys(), n=1, cutoff=0.4)
    if matches:
        return os.path.splitext(name_map[matches[0]])[0]
    return None

def generate_image_definitions(image_root):
    lines = []
    bg_dir = os.path.join(image_root, "backgrounds")
    if os.path.isdir(bg_dir):
        for f in sorted(os.listdir(bg_dir)):
            name, ext = os.path.splitext(f)
            if ext.lower() in [".png", ".jpg", ".webp"]:
                clean = name.replace("'", "").replace('"', "").replace("&", "")
                lines.append(f'image bg {clean} = "images/backgrounds/{f}"')
    char_dir = os.path.join(image_root, "characters")
    if os.path.isdir(char_dir):
        for f in sorted(os.listdir(char_dir)):
            name, ext = os.path.splitext(f)
            if ext.lower() in [".png", ".jpg", ".webp"]:
                tag_name = char_tag(name.replace("_", " "))
                lines.append(f'image {tag_name} = "images/characters/{f}"')
    loc_dir = os.path.join(image_root, "locations")
    if os.path.isdir(loc_dir):
        for f in sorted(os.listdir(loc_dir)):
            name, ext = os.path.splitext(f)
            if ext.lower() in [".png", ".jpg", ".webp"]:
                clean = name.replace("'", "").replace('"', "").replace("&", "")
                lines.append(f'image loc {clean} = "images/locations/{f}"')
    return "\n".join(lines) + "\n\n"

def _extract_option_text(raw_text):

    import re as _re

    text = _re.split(r'\s*->\s*TARGET', raw_text, flags=_re.IGNORECASE)[0].strip()

    text = _re.sub(r'^Option\s+\d+\s*:\s*', '', text, flags=_re.IGNORECASE).strip()

    if len(text) >= 2 and text[0] == text[-1] == '"':
        text = text[1:-1].strip()
    elif len(text) >= 2 and text[0] == text[-1] == "'":
        text = text[1:-1].strip()

    return text.replace('"', "'")


def char_tag(name):

    if Char_def:
        name_low = name.lower().strip()
        exact = prefix = None
        substr_candidates = []
        for line in Char_def.split("\n"):
            m = re.match(r"define\s+(\w+)\s*=\s*Character\('(.*?)'\)", line)
            if not m: continue
            def_low = m.group(2).lower().strip()
            var     = m.group(1)
            if def_low == name_low:
                exact = var; break
            elif def_low.startswith(name_low + " ") and not prefix:
                prefix = var
            elif (" " + name_low + " ") in (" " + def_low + " "):
                substr_candidates.append(var)
        if exact:
            return exact
        if prefix:
            return prefix
        if len(substr_candidates) == 1:
            return substr_candidates[0]
        if len(substr_candidates) > 1:
            print(f"  [WARN] char_tag: '{name}' matches multiple characters {substr_candidates}, using sanitize fallback")
    name_parts = name.split()
    if name_parts and name_parts[0].endswith("."):
        name_parts = name_parts[1:]
    return sanitize_var_name(" ".join(name_parts) if name_parts else name)


def preparse_file(content_lines):
    interaction_header  = re.compile(r'^\[INTERACTION\]$')
    decision_header     = re.compile(r'^\[(DECISION POINT|DECISION)\]$', re.IGNORECASE)
    choice_line         = re.compile(r'^>\s*Choice\s+([A-Z]):\s*"(.*?)"$')
    outcome_line        = re.compile(r'^\[Outcome\s+(.+?):\s*(.*?)\]$')
    routing_sep         = re.compile(r'^={5,}')
    routing_option_pat  = re.compile(r'^Option\s+(\d+):')
    routing_target_pat  = re.compile(r'Target\s+File:\s*(.+\.txt)')
    decision_option_pat = re.compile(r'^\s*(\d+)\)\s*(.+)$')

    raw_lines = [l.rstrip('\n') for l in content_lines]


    routing_start_idx = None
    for idx, line in enumerate(raw_lines):
        if routing_sep.match(line.strip()):
            for look in raw_lines[idx:idx + 3]:
                if "SYSTEM ROUTING TABLE" in look:
                    routing_start_idx = idx
                    break
            if routing_start_idx is not None:
                break

    routing_block_lines = []
    if routing_start_idx is not None:
        routing_block_lines = raw_lines[routing_start_idx:]
        raw_lines = raw_lines[:routing_start_idx]


    linear_raw     = None
    option_map_raw = {}
    cur_opt        = None
    linear_flag    = False
    next_chapter_pat = re.compile(r'\[NEXT CHAPTER:\s*(\d+)\]')
    for line in routing_block_lines:
        s = line.strip()
        if '[LINEAR]' in s:
            linear_flag = True
        if linear_flag:
            m = routing_target_pat.search(s)
            if m:
                linear_raw  = m.group(1).strip()
                linear_flag = False
        m = routing_option_pat.match(s)
        if m:
            cur_opt = m.group(1)
            continue
        m = routing_target_pat.search(s)
        if m and cur_opt:
            option_map_raw[cur_opt] = m.group(1).strip()
            cur_opt = None


    if not linear_raw and not option_map_raw:
        for line in raw_lines:
            m = next_chapter_pat.search(line.strip())
            if m:
                linear_raw = f"__ch_idx_{m.group(1)}__"
                break

    blocks = [{'type': 'routing', 'linear': linear_raw, 'option_map': option_map_raw}]


    last_dp_idx = None
    for idx, line in enumerate(raw_lines):
        if decision_header.match(line.strip()):
            last_dp_idx = idx


    i = 0
    n = len(raw_lines)

    while i < n:
        stripped = raw_lines[i].strip()

        if interaction_header.match(stripped):
            interaction = {
                'type': 'interaction',
                'choices': {},
                'outcomes': {},
                'merge_lines': [], 
            }
            i += 1

            # States: 'header' (reading choices/outcomes), 'merge' (inside MERGE block)
            state        = 'header'
            merge_buf    = []   # accumulates lines while inside MERGE

            while i < n:
                s       = raw_lines[i].strip()
                s_orig  = raw_lines[i]  # preserve original indentation for merge

                # Any [DECISION POINT] ends the interaction
                if decision_header.match(s):
                    if state == 'merge':
                        # Close the merge without the final ] line (already consumed)
                        interaction['merge_lines'] = merge_buf
                    if i != last_dp_idx:
                        i += 1  # consume fake DP header
                    break

                # A new [INTERACTION] ends this one
                if interaction_header.match(s):
                    if state == 'merge':
                        interaction['merge_lines'] = merge_buf
                    break

                # Routing separator ends everything
                if routing_sep.match(s):
                    if state == 'merge':
                        interaction['merge_lines'] = merge_buf
                    break

                if state == 'merge':
                    if s.endswith(']') and not s.endswith('"]'):
                        # Final line of MERGE block — strip trailing ]
                        final = s[:-1].rstrip()
                        if final:
                            merge_buf.append(final)
                        interaction['merge_lines'] = merge_buf
                        state = 'done'
                        i += 1
                        break
                    elif s.endswith('"]'):
                        # Line ends with "] where " closes dialogue inside merge
                        # e.g.  Rex-9: "...safe routes."]
                        # Strip the outer ] only
                        final = s[:-1].rstrip()
                        if final:
                            merge_buf.append(final)
                        interaction['merge_lines'] = merge_buf
                        state = 'done'
                        i += 1
                        break
                    else:
                        # Interior line of merge — keep as-is (may be empty = paragraph break)
                        merge_buf.append(s_orig.rstrip())
                    i += 1
                    continue

                m = choice_line.match(s)
                if m:
                    interaction['choices'][m.group(1)] = m.group(2)
                    i += 1
                    continue

                m = outcome_line.match(s)
                if m:
                    key = m.group(1).strip()[-1]
                    raw_outcome = m.group(2).strip()
                    if raw_outcome.startswith('"') and raw_outcome.endswith('"'):
                        raw_outcome = raw_outcome[1:-1]
                    interaction['outcomes'][key] = raw_outcome.replace('"', "'")
                    i += 1
                    continue

                # MERGE start: [MERGE: text...
                if s.startswith('[MERGE:'):
                    # Strip the opening tag to get first-line content
                    first_content = s[len('[MERGE:'):].lstrip()
                    # Check if it closes on the same line
                    if first_content.endswith(']') and not first_content.endswith('"]'):
                        interaction['merge_lines'] = [first_content[:-1].rstrip()]
                        state = 'done'
                        i += 1
                        break
                    elif first_content.endswith('"]'):
                        interaction['merge_lines'] = [first_content[:-1].rstrip()]
                        state = 'done'
                        i += 1
                        break
                    else:
                        merge_buf = [first_content] if first_content else []
                        state = 'merge'
                    i += 1
                    continue

                # Anything else in header state: skip (narration inside interaction header area)
                i += 1

            blocks.append(interaction)
            continue

        if decision_header.match(stripped) and i == last_dp_idx:
            dp = {'type': 'decision', 'options': []}
            i += 1
            while i < n:
                s = raw_lines[i].strip()
                if routing_sep.match(s):
                    break
                if not s:
                    i += 1
                    continue
                m = decision_option_pat.match(s)
                if m:
                    dp['options'].append({'num': m.group(1), 'text': m.group(2)})
                i += 1
            blocks.append(dp)
            continue

        if decision_header.match(stripped) and i != last_dp_idx:
            i += 1
            while i < n:
                s = raw_lines[i].strip()
                if not s or routing_sep.match(s):
                    break
                if decision_option_pat.match(s):
                    i += 1
                    continue
                break
            continue


        blocks.append({'type': 'raw', 'text': stripped})
        i += 1

    return blocks


# Main converter
def convert_txt_to_renpy(input_dir, output_dir, world_setting_path=None, image_root=None, outline_path=None):
    global Char_def, img_def

    Char_def = ""
    img_def  = ""

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if world_setting_path is None:
        world_setting_path = find_world_setting_file(os.path.dirname(input_dir))
        if world_setting_path is None:
            print(f"  Warning: world_setting not found near {input_dir}")
            return False
    if not os.path.exists(world_setting_path):
        candidate = os.path.join(os.path.dirname(input_dir), world_setting_path)
        if os.path.exists(candidate):
            world_setting_path = candidate
        elif os.path.exists(world_setting_path + ".json"):
            world_setting_path += ".json"
        else:
            print(f"  Error: cannot find world_setting: {world_setting_path}")
            return False

    if image_root is None:
        image_root = os.path.join(os.path.dirname(input_dir), "generated_assets")
        if not os.path.exists(image_root):
            image_root = "./generated_assets"

    sprite_files = []
    char_img_dir = os.path.join(image_root, "characters")
    if os.path.isdir(char_img_dir):
        sprite_files = [f for f in os.listdir(char_img_dir)
                        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]


    actual_files = sorted(
        [f for f in os.listdir(input_dir) if f.endswith(".txt")],
        key=chapter_key
    )
    if not actual_files:
        print(f"  Warning: no .txt files in {input_dir}")
        return False

    chapter_map    = {f: f"chapter{i + 1}" for i, f in enumerate(actual_files)}
    referenced_files = set()


    ch_idx_to_labels = {}
    for fn, label in chapter_map.items():
        m = re.search(r'ch(\d+)', fn)
        if m:
            idx = int(m.group(1))
            ch_idx_to_labels.setdefault(idx, []).append(label)

    def label_for_ch_idx(idx):
        """Return the first label for a given chapter_index (best-effort)."""
        labels = ch_idx_to_labels.get(idx)
        return labels[0] if labels else None


    outline_chapters = {}   # {chapter_index: chapter_dict}
    if outline_path is None:
        # Auto-discover: look for story_outline*.json in case directory
        case_dir = os.path.dirname(input_dir)
        candidates = glob.glob(os.path.join(case_dir, "story_outline*.json"))
        if candidates:
            outline_path = candidates[0]
    if outline_path and os.path.exists(outline_path):
        with open(outline_path, 'r', encoding='utf-8') as f:
            outline_data = json.load(f)
        for ch in outline_data.get("chapter_structure", []):
            outline_chapters[ch["chapter_index"]] = ch
        print(f"  Outline loaded: {os.path.basename(outline_path)} ({len(outline_chapters)} chapters)")
    else:
        print("  Warning: no outline file found, falling back to routing table in txt")

 
    with open(world_setting_path, 'r', encoding='utf-8') as f:
        world_data = json.load(f)

    RENPY_RESERVED = {
        "director", "narrator", "menu", "jump", "call", "return", "pass",
        "show", "hide", "scene", "play", "stop", "pause", "with", "at",
        "style", "config", "persistent", "store", "renpy", "audio",
        "music", "sound", "voice", "image", "define", "default",
        "transform", "screen", "init", "python", "label", "if", "else",
        "elif", "for", "while", "not", "and", "or", "in", "true", "false",
    }

    characters = world_data.get("main_characters", []) + world_data.get("secondary_characters", [])
    char_def_lines = ["define you = Character('You')"]
    used_vars = {"you"}
    for ch in characters:
        raw = ch["name"].replace("'", "")
        var = sanitize_var_name(raw) 
        if var in RENPY_RESERVED:
            var = f"chr_{var}"
        if not var:
            var = "char_unknown"
        if var in used_vars:
            k = 2
            while f"{var}_{k}" in used_vars:
                k += 1
            var = f"{var}_{k}"
        used_vars.add(var)
        char_def_lines.append(f"define {var} = Character('{raw}')")

    characters_definition = "\n".join(char_def_lines) + "\n"
    Char_def   = characters_definition
    image_defs = generate_image_definitions(image_root)
    img_def    = image_defs


    with open(os.path.join(output_dir, "script.rpy"), 'w', encoding='utf-8') as f:
        f.write("transform full_bg:\n    xysize (config.screen_width, config.screen_height)\n\n")
        f.write("# AUTO-GENERATED IMAGE DEFINITIONS\n")
        f.write(image_defs)
        f.write(characters_definition)
        f.write("\nlabel start:\n    jump chapter1\n")

    IGNORE_LABELS = {
        "Scene", "Visual", "Source", "Music", "Sound", "Option",
        "Decision Point", "Draft", "Background", "Character",
        "Outcome", "MERGE", "INTERACTION", "LINEAR", "SYSTEM ROUTING TABLE",
    }


    for filename in actual_files:
        file_path  = os.path.join(input_dir, filename)
        label_name = chapter_map[filename]
        ending_flag = "Ending" in filename.split("_")

        with open(file_path, 'r', encoding='utf-8') as f:
            content_lines = f.readlines()

        blocks = preparse_file(content_lines)

        routing_blk    = blocks[0]
        linear_raw     = routing_blk['linear']
        option_map_raw = routing_blk['option_map']

        linear_target = None
        routing_map   = {}        # {opt_num_str: label}

        if linear_raw:
            if linear_raw.startswith("__ch_idx_"):
                ch_idx = int(linear_raw.replace("__ch_idx_", "").replace("__", ""))
                tgt_label = label_for_ch_idx(ch_idx)
                if tgt_label:
                    linear_target = tgt_label
                    referenced_files.update(
                        fn for fn, lbl in chapter_map.items() if lbl == tgt_label)
                else:
                    print(f"  Warning: [NEXT CHAPTER: {ch_idx}] not found in files")
            else:
                matched = find_target_filename(linear_raw, actual_files)
                if matched:
                    linear_target = chapter_map[matched]
                    referenced_files.add(matched)
                else:
                    print(f"  Warning: linear target not found: '{linear_raw}'")

        for opt_num, tgt_file in option_map_raw.items():
            matched = find_target_filename(tgt_file, actual_files)
            if matched:
                routing_map[opt_num] = chapter_map[matched]
                referenced_files.add(matched)
            else:
                print(f"  Warning: routing target not found: '{tgt_file}'")

        visual_pattern    = re.compile(r'\[Visual:\s*(.*?)\]')
        sound_pattern     = re.compile(r'\[Sound:\s*(.*?)\]')
        music_pattern     = re.compile(r'\[Music:\s*(.*?)\]')
        emotional_pattern = re.compile(r'\[Emotional Track:\s*(.*?)\]')
        scene_pattern     = re.compile(r'\[Scene:\s*(.*?)\]')
        background_pattern = re.compile(r'\[Background:\s*"(.*?)"\]')
        character_tag_pat = re.compile(r'\[Character:\s*(.*?)\]')
        dialogue_pattern  = re.compile(r'^(.+?)\s*(?:\[.*?\])?\s*:\s*"(.*)"')

        side         = ["left", "right", "center"]
        side_counter = 0
        prev_char    = None
        on_screen    = []
        forced_character = None

        def _find_in_chardef(display):

            exact = prefix = None
            substr_candidates = []
            disp_low = display.lower().strip()
            for ln in Char_def.split("\n"):
                m = re.match(r"define\s+(\w+)\s*=\s*Character\('(.*?)'\)", ln)
                if not m: continue
                def_name = m.group(2).lower().strip()
                var_name  = m.group(1)
                if def_name == disp_low:
                    exact = var_name; break
                elif def_name.startswith(disp_low + " ") and not prefix:
                    prefix = var_name
                elif (" " + disp_low + " ") in (" " + def_name + " "):
                    substr_candidates.append(var_name)
            if exact: return exact
            if prefix: return prefix
            if len(substr_candidates) == 1: return substr_candidates[0]
            if len(substr_candidates) > 1:
                print(f"  [WARN] _find_in_chardef: '{display}' ambiguous {substr_candidates}")
            return None

        def show_character(rpy, char_display):
            nonlocal side_counter, prev_char
            tag = char_tag(char_display)
            if char_display not in on_screen and prev_char != char_display:
                on_screen.append(char_display)
                if len(on_screen) > 3:
                    old = on_screen.pop(0)
                    rpy.write(f"    hide {char_tag(old)}\n")
                rpy.write(f"    show {tag} at {side[side_counter]}:\n        zoom {zoom_size}\n")
                prev_char = char_display
                side_counter = (side_counter + 1) % 3

        def write_narration(rpy, text):
            text = text.replace('"', "'")
            if not text.strip():
                return
            if len(text.split()) > 50:
                words, chunks, cur = text.split(), [], ""
                for w in words:
                    if len(cur.split()) <= 35:
                        cur = (cur + " " + w).strip()
                    else:
                        chunks.append(cur); cur = w
                if cur:
                    chunks.append(cur)
                text = '"\n    "'.join(chunks)
            rpy.write(f'    "{text}"\n')

        def render_line(rpy, line):
            """Render a single content line (raw or from merge_lines) to rpy."""
            nonlocal forced_character
            if not line: return
            if line.startswith(">") or line.startswith("#"): return
            if line.startswith("---") or "======" in line: return
            if "Choice A" in line or "Choice B" in line: return
            if line.startswith("###"): return
            if line.startswith("# Route:") or line.startswith("# Context:"): return

            m = character_tag_pat.match(line)
            if m:
                forced_character = m.group(1).strip()
                return

            m = background_pattern.match(line)
            if m:
                bg_name = m.group(1).replace("'","").replace('"',"").replace("&","")
                for c in on_screen:
                    rpy.write(f"    hide {char_tag(c)}\n")
                on_screen.clear()
                nonlocal side_counter, prev_char
                side_counter = 0; prev_char = None
                rpy.write(f"\n    scene bg {bg_name} at full_bg\n")
                forced_character = None
                return

            if visual_pattern.search(line):
                rpy.write(f"    # {line}\n"); return
            if sound_pattern.search(line):
                rpy.write(f'    # play sound "sfx_placeholder"  # {line}\n'); return
            if music_pattern.search(line) or emotional_pattern.search(line):
                rpy.write(f'    # play music "music_placeholder"  # {line}\n'); return
            if scene_pattern.search(line):
                rpy.write(f"    # {line}\n"); return
            if re.match(r'^\[NEXT CHAPTER:', line, re.IGNORECASE):
                return
            if line.startswith("["):
                rpy.write(f"    # {line}\n"); return

            m = dialogue_pattern.match(line)
            if m:
                raw_name = m.group(1).strip()
                text     = m.group(2)
                if raw_name in IGNORE_LABELS or not raw_name:
                    write_narration(rpy, line)
                    forced_character = None
                    return
                char_display = forced_character if forced_character else raw_name
                forced_character = None
                text = text.replace("%", " Percentage")
                clean_text = text.replace('"', "'")
                char_var = _find_in_chardef(char_display)
                tag      = char_tag(char_display)
                if char_var and char_var.lower() != "you":
                    show_character(rpy, char_display)
                    rpy.write(f'\n    {char_var.lower()} "{clean_text}"\n')
                elif char_var is None and tag in img_def and tag not in keys:
                    show_character(rpy, char_display)
                    rpy.write(f'\n    "{char_display}" "{clean_text}"\n')
                else:
                    if sprite_files:
                        best = get_best_match(char_display, sprite_files)
                        if best and best in img_def:
                            show_character(rpy, char_display)
                    rpy.write(f'\n    "{char_display}" "{clean_text}"\n')
                return

            write_narration(rpy, line)

        output_file = os.path.join(output_dir, f"{label_name}.rpy")

        try:
            with open(output_file, 'w', encoding='utf-8') as rpy:
                rpy.write(f"label {label_name}:\n\n")

                did_jump = False

                for blk in blocks[1:]:

                    if blk['type'] == 'interaction':
                        choices     = blk['choices']
                        outcomes    = blk['outcomes']
                        merge_lines = blk['merge_lines']

                        if not choices:
                            # No choices → just render merge as narration
                            for ml in merge_lines:
                                render_line(rpy, ml)
                            continue

                        rpy.write("\n    menu:\n")
                        for key, choice_text in choices.items():
                            outcome = outcomes.get(key, "")
                            rpy.write(f'        "{choice_text.replace(chr(34), chr(39))}":\n')
                            if outcome:
                                clean_outcome = outcome.replace(chr(34), chr(39))
                                rpy.write(f'            "{outcome}"\n')
                            # No per-branch merge here; merge is shared below

                        # Merge content rendered AFTER the menu, as shared narration
                        if merge_lines:
                            rpy.write("\n    # --- merge ---\n")
                            for ml in merge_lines:
                                render_line(rpy, ml)

                    elif blk['type'] == 'decision':
                        if ending_flag:
                            continue

                        if not blk['options']:
                            if linear_target:
                                rpy.write(f"\n    jump {linear_target}\n")
                                did_jump = True
                            continue

                        opt_targets = []
                        for opt in blk['options']:
                            t = routing_map.get(opt['num']) or linear_target
                            opt_targets.append(t)

                        unique_targets = set(t for t in opt_targets if t)
                        if len(unique_targets) <= 1:
                            target = next(iter(unique_targets), None) or linear_target
                            if target:
                                rpy.write(f"\n    jump {target}\n")
                                did_jump = True
                            continue

                        rpy.write("\n    menu:\n")
                        for opt, target in zip(blk['options'], opt_targets):
                            clean = _extract_option_text(opt['text'])
                            rpy.write(f'        "{clean}":\n')
                            if target:
                                rpy.write(f"            jump {target}\n")
                            else:
                                rpy.write("            return\n")

                    elif blk['type'] == 'raw':
                        render_line(rpy, blk['text'])

                if linear_target and not did_jump:
                    rpy.write(f"\n    jump {linear_target}\n")
                rpy.write("    return\n")

        except Exception as e:
            import traceback
            print(f"  ✗ Error processing {filename}: {e}")
            traceback.print_exc()
            continue

        print(f"  ✓ {filename} -> {label_name}.rpy")


    orphans = [f for f in actual_files[1:] if f not in referenced_files]
    if orphans:
        print(f"  [WARN] {len(orphans)} unreachable chapter(s):")
        for o in orphans:
            print(f"    - {o}")

    return True


# Batch runner
def process_all_cases(results_root="results"):
    if not os.path.exists(results_root):
        print(f"Error: '{results_root}' not found"); return

    total_ok = total_fail = 0
    for theme_dir in sorted(os.listdir(results_root)):
        theme_path = os.path.join(results_root, theme_dir)
        if not os.path.isdir(theme_path): continue
        print(f"\n{'='*60}\nTheme: {theme_dir}\n{'='*60}")
        for genre_dir in sorted(os.listdir(theme_path)):
            genre_path = os.path.join(theme_path, genre_dir)
            if not os.path.isdir(genre_path): continue
            for world_dir in sorted(os.listdir(genre_path)):
                world_path = os.path.join(genre_path, world_dir)
                if not os.path.isdir(world_path): continue
                scripts_path = os.path.join(world_path, "Processed_Scripts")
                if not os.path.exists(scripts_path):
                    scripts_path = os.path.join(world_path, "Scripts_Text")
                if not os.path.exists(scripts_path): continue
                print(f"\n  → {theme_dir}/{genre_dir}/{world_dir}")
                output_path = os.path.join(world_path, "chapter_renpy")
                try:
                    if convert_txt_to_renpy(scripts_path, output_path):
                        print(f"  ✓ OK"); total_ok += 1
                    else:
                        print(f"  ✗ Failed"); total_fail += 1
                except Exception as e:
                    print(f"  ✗ Exception: {e}"); total_fail += 1

    print(f"\n{'='*60}\nDone — Success: {total_ok}  Failed: {total_fail}\n{'='*60}")


process_all_cases("results")