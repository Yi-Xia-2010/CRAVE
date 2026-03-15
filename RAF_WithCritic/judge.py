import json
import os
from run_all import FIXED_THEME
from utils import call_gpt_api, load_prompt_template, get_api_key


class StoryJudge:
    def __init__(self, role, model):
        self.role = role
        self.model = model
        if self.role == "Story_outline_judge":
            self.criteria = load_prompt_template("prompts/Story_outline_judge_Sys.txt")
            self.user_prompt_template = load_prompt_template("prompts/Story_outline_judge_User.txt")
        else:
            self.criteria = load_prompt_template("prompts/Script_draft_judge_Sys.txt")
            self.user_prompt_template = load_prompt_template("prompts/Script_draft_judge_User.txt")

    
    def judging(self,story: list, story_type, genre, id, script_name = "not needed", emotional_trajectory = "Not needed"):
        try:
            api_key = get_api_key()
            game_theme = FIXED_THEME
            safe_theme = FIXED_THEME.replace(" ","_")
            safe_genre = genre.replace(" ","_")
            W_DIR = f"results/{safe_theme}/{safe_genre}/World_{id}"

            story_order = ""
            role = self.role.replace("_", " ").replace("judge", " ").upper().strip()
            drafts_dir = os.path.join(f"{W_DIR}/judging_drafts/{story_type}", f"{role}")
            os.makedirs(drafts_dir, exist_ok=True)
            for i in range(len(story)):
                story_order += f"\n\n===================================================\n\n#ID->[{i+1}]. {role} {story[i]}\n"
                if script_name == "not needed":
                    with open(os.path.join(drafts_dir, f"{role}_ID_{i+1}.txt"), 'w', encoding='utf-8') as f:
                        f.write(story[i])
                else:
                    with open(os.path.join(drafts_dir, f"{role}_{script_name}_ID_{i+1}.txt"), 'w', encoding='utf-8') as f:
                        f.write(story[i])

            if role == "STORY OUTLINE":
                sys_prompt = self.criteria
                user_prompt_temp = self.user_prompt_template
                user_prompt = user_prompt_temp.format(story_type = story_type,  game_theme = game_theme, genre = genre, story_order = story_order) # as output it should return a single value "index position" as 1,2 or 3.
            
            else:
                sys_prompt = self.criteria
                user_prompt_temp = self.user_prompt_template
                user_prompt = user_prompt_temp.format(game_theme = game_theme, genre = genre, emotional_trajectory = emotional_trajectory, story_order = story_order) # as output it should return a single value "index position" as 1,2 or 3.
            
            response = call_gpt_api(
               api_key, sys_prompt, user_prompt, self.model, json_mode=True
            )
        except Exception as e:
            raise ValueError("Error while getting response from llm: ", e)
        
        response = json.loads(response)
        try:
            best = response["best"]
            # reason = response["reason"]
            # print(reason)
        except:
            print(response)
            return
        
        best = int(best) # convert the response to integer
        best = best - 1 # convert the response to index position

        return best