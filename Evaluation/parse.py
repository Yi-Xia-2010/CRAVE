import os
import re
import difflib

# Configuration
SPRITE_FOLDER_NAME = "Sprites"
IGNORE_LABELS = {
    "Scene", "Visual", "Source", "Music", "Sound",
    "Option", "Decision Point", "Draft",
    "Narration", "Background", "Character",
    "Outcome", "MERGE", "INTERACTION", "LINEAR",
}

IGNORE_PATTERNS = [
    re.compile(r"^Option\s+\d+$", re.IGNORECASE),
    re.compile(r"^Outcome\s+[A-Z]$", re.IGNORECASE),
    re.compile(r"^Narration.*$", re.IGNORECASE),
]

def get_best_match(character_name, sprite_files):
    # Create a mapping of {filename_without_extension: full_filename}
    # This helps us compare "Elias" to "Elias Wren" without the ".png" confusing things
    name_map = {os.path.splitext(f)[0]: f for f in sprite_files}
    
    # Use difflib to find the closest match to the character's name
    # cutoff=0.4 means it needs to be at least 40% similar (adjustable)
    matches = difflib.get_close_matches(character_name, name_map.keys(), n=1, cutoff=0.4)
    
    if matches:
        # Return the original full filename (with .png)
        return name_map[matches[0]]
    return None

def process_chapter_scripts(directory_path=".", sprite_folder_path="generated_assets/characters"):   
    # Setup folders
    output_folder = os.path.join(os.path.dirname(directory_path), "Processed_Scripts")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load Sprite List
    sprite_files = []
    if os.path.exists(sprite_folder_path):
        sprite_files = [f for f in os.listdir(sprite_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        print(f"Loaded {len(sprite_files)} sprites from '{sprite_folder_path}'.")
    else:
        print(f"WARNING: '{sprite_folder_path}' not found. Character labeling will be skipped.")

    # Regex Setup
    filename_chapter_pattern = re.compile(r"ch(\d+)", re.IGNORECASE)
    scene_pattern = re.compile(r"\[Scene:.*?\]", re.IGNORECASE)
    visual_pattern = re.compile(r"\[Visual:.*?\]", re.IGNORECASE)
    
    # Matches "Name: Dialog" (e.g., "Jae: Hello" or "Elias Wren: (Softly) Hello")
    # Capture group 1 is the name.
    dialogue_pattern = re.compile(r"^([A-Z0-9][\w\s\-\.]+?)(?:\s*\[.*?\])?\s*:", re.MULTILINE)

    txt_files_found = False
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            txt_files_found = True
            
            # --- Identify Chapter ---
            chapter_match = filename_chapter_pattern.search(filename)
            if not chapter_match:
                continue # Skip files without 'chX'
            
            chapter_num = chapter_match.group(1)
            image_index = 1
            input_path = os.path.join(directory_path, filename)
            
            # script_ch1_Common_ctx_Start.txt → scene_name = "Start"
            ctx_match = re.search(r'ctx_([^\.]+)', filename)
            scene_name = ctx_match.group(1) if ctx_match else "Scene"
            
            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                new_lines = []

                # --- Pass: Line Processing ---
                for i, line in enumerate(lines):
                    
                    # Check for Background Tags ([Visual] only)
                    is_visual = visual_pattern.search(line)
                    
                    if is_visual:
                        bg_filename = f"ch{chapter_num}_{scene_name}_{image_index}"
                        new_lines.append(f'[Background:"{bg_filename}"]\n')
                        image_index += 1
                        continue # Move to next line (replace the original tag)

                    # 3. Check for Character Dialogue
                    # We check if the line starts with "Name:" 
                    dialog_match = dialogue_pattern.search(line)
                    
                    if dialog_match:
                        raw_name = dialog_match.group(1).strip()
                        
                        # Filter out non-character labels (like "Scene:", "Option 1:", etc.)
                        # We also ignore if the name is purely numbers or empty
                        if (raw_name not in IGNORE_LABELS
                            and not any(p.match(raw_name) for p in IGNORE_PATTERNS)
                            and sprite_files):
                            
                            best_sprite = get_best_match(raw_name, sprite_files)
                            if best_sprite:
                                best_sprite = best_sprite.replace(".png", "")
                            
                            if best_sprite:
                                # Insert the Character Label BEFORE the dialogue line
                                new_lines.append(f'[Character:{best_sprite}]\n')
                            else:
                                # Optional: Print warning if no sprite matches (helps debugging)
                                # print(f"Warning: No sprite found for '{raw_name}' in {filename}")
                                pass

                    # 4. Append the original line (dialogue, narration, etc.)
                    new_lines.append(line)
                
                # Write to file
                output_path = os.path.join(output_folder, filename)
                with open(output_path, 'w', encoding='utf-8') as out_f:
                    out_f.writelines(new_lines)
                
                print(f"  ✓ Processed '{filename}'")
                
            except Exception as e:
                print(f"  ✗ Error processing '{filename}': {e}")
    
    if not txt_files_found:
        print(f"  No .txt files found in {directory_path}")
    
    return txt_files_found

def find_and_process_all_scripts(root_folder="results"):
    if not os.path.exists(root_folder):
        print(f"Can't find '{root_folder}'")
        return
    
    processed_count = 0
    
    for root, dirs, files in os.walk(root_folder):
        if os.path.basename(root) == "Scripts_Text":
            print(f"\nProcessing: {root}")
            
            case_folder = os.path.dirname(root)
            sprite_folder = os.path.join(case_folder, "generated_assets", "characters")
            
            if process_chapter_scripts(root, sprite_folder):
                processed_count += 1
    
    print(f"\n" + "="*50)
    print(f"DONE! Processed {processed_count}  Scripts_Text cases")
    print("="*50)

if __name__ == "__main__":
    find_and_process_all_scripts("results")