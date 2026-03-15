import os
import json
import datetime
import argparse
from utils import (
    get_api_key, 
    load_prompt_template, 
    call_gpt_api, 
    save_json_file, 
    sanitize_filename, 
    MODEL_LOGIC
)

def run_step_1(api_key, theme, genre, chapters="15"):

    sys_prompt = load_prompt_template("prompts/StorySetting_Sys.txt")
    user_prompt_tmpl = load_prompt_template("prompts/StorySetting_User.txt")

    if not sys_prompt or not user_prompt_tmpl:
        return None

    user_prompt = user_prompt_tmpl.format(
        theme=theme,
        genre=genre,
        chapters=chapters
    )

    print(f"Generating World Setting for: {theme} ({genre})...")
    
    response = call_gpt_api(
        api_key=api_key,
        system_prompt=sys_prompt,
        user_prompt=user_prompt,
        model=MODEL_LOGIC,
        json_mode=True
    )
    
    return response

def main():
    parser = argparse.ArgumentParser(description="Step 1: Generate World Setting (Project Initialization)")
    
    parser.add_argument("--theme", type=str, required=True, help="Story theme (e.g. Cyberpunk)")
    parser.add_argument("--genre", type=str, required=True, help="Story genre (e.g. Detective)")
    
    parser.add_argument("--chapters", type=str, default="6", help="Estimated chapter length")
    parser.add_argument("--tag", type=str, help="Unique tag for folder naming (e.g. Story_1)")
    parser.add_argument("--no-input", action="store_true", help="Skip interactive confirmation")
    

    parser.add_argument("--project_path", type=str, help="Force specific output directory")
    
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key:
        print("Error: API Key not found.")
        return

    result_json_str = run_step_1(api_key, args.theme, args.genre, args.chapters)
    
    if result_json_str:
        try:
            world_data = json.loads(result_json_str)
            
            print("\nWorld Setting Generated Successfully!")
            print(f"   Preview: {str(world_data)[:300]}...\n")
        
            safe_theme = sanitize_filename(args.theme)
            safe_genre = sanitize_filename(args.genre)

            if args.tag:
                safe_tag = sanitize_filename(args.tag)
                folder_name = f"World_{safe_tag}"
                filename = f"world_setting_{safe_tag}.json"
            else:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                folder_name = f"World_{timestamp}"
                filename = f"world_setting_{timestamp}.json"

            if args.project_path:
                save_dir = args.project_path
                os.makedirs(save_dir, exist_ok=True)
            else:
                save_dir = os.path.join("results", safe_theme, safe_genre, folder_name)
            

            saved_path = save_json_file(world_data, save_dir, filename)
            
            if saved_path:
                print(f"Project initialized at: {save_dir}")
                print(f"File saved as: {filename}")
                print("-" * 30)
                print(f"Next Step: Run Step 2 with this path:")
                print(f"   python step2_outline.py --project_path \"{save_dir}\"")
            
        except json.JSONDecodeError:
            print("Error: Failed to parse valid JSON from API response.")
    else:
        print("Error: Generation failed.")

if __name__ == "__main__":
    main()