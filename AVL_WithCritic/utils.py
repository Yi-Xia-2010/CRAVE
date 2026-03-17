import os
import json
import time
import glob
import re
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, AuthenticationError


load_dotenv()


MODEL_LOGIC = "gpt-5-mini"      
# MODEL_EFFICIENT = "gpt-5-mini" 


def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file. Using Local Model")
        return "ollama"
    return api_key

def load_prompt_template(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Prompt template file not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error reading prompt file: {e}")
        return None

import re

def sanitize_filename(name):
    if not name:
        return "unknown"
    
    # \ / : * ? " < > | —
    name = re.sub(r'[\\/:*?"<>|—]', '_', str(name))
    
    name = name.replace(' ', '_')
    clean_name = re.sub(r'[^\w_]', '', name)
    
    collapsed = re.sub(r'_+', '_', clean_name).strip('_')
    
    return collapsed if collapsed else "unknown"

def save_json_file(data, folder_path, filename):
    try:
        os.makedirs(folder_path, exist_ok=True)
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Successfully saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error saving file {filename}: {e}")
        return None

def call_gpt_api(api_key, system_prompt, user_prompt, model=MODEL_EFFICIENT, max_retries=2, json_mode=True):
    if not api_key:
        api_key = get_api_key()

    if api_key == "ollama":
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key=api_key,
        )
        
    else:
        client = OpenAI(api_key=api_key)
    retries = 0
    
    while retries <= max_retries:
        try:
            # print(f"Calling OpenAI API [{model}] (JSON Mode: {json_mode})...")
            
            kwargs = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            }
            

            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}

            completion = client.chat.completions.create(**kwargs)
            response_text = completion.choices[0].message.content
            

            if not json_mode:
                return response_text.strip()

            cleaned_text = response_text.strip()
            if cleaned_text.startswith("```json"):
                cleaned_text = cleaned_text[7:]
            if cleaned_text.startswith("```"):
                cleaned_text = cleaned_text[3:]
            if cleaned_text.endswith("```"):
                cleaned_text = cleaned_text[:-3]
            
            cleaned_text = cleaned_text.strip()
            json.loads(cleaned_text) 
            return cleaned_text

        except json.JSONDecodeError:
            print(f"Error: API returned invalid JSON in JSON Mode.")
        except RateLimitError:
            print(f"Rate limit hit. Waiting...")
            time.sleep(2 ** (retries + 1))
        except AuthenticationError:
            print("Error: Invalid API Key.")
            return None
        except Exception as e:
            print(f"API Error: {e}")
            if "model" in str(e).lower() and "not found" in str(e).lower():
                print(f"Tip: Check if '{model}' is valid.")

            if "must contain the word 'json'" in str(e).lower():
                print("Fatal: 'response_format' is json_object but prompt is missing the word 'json'. Check your prompts.")
                return None 
            time.sleep(1)
            
        retries += 1
            
    return None

def compress_text(api_key, text, target_words=800, model=MODEL_EFFICIENT):

    system_prompt = "You are an expert editor. Summarize the provided story context."
    user_prompt = f"""
    The following story summary has become too long for the context window.
    
    **TASK:**
    Rewrite this into a concise summary of approximately {target_words} words.
    
    **REQUIREMENTS:**
    1. Preserve ALL key plot points, major decisions, and inventory changes.
    2. Keep the status of character relationships clear.
    3. Discard minor atmospheric details.
    
    **TEXT TO COMPRESS:**
    {text}
    """
    
    json_user_prompt = user_prompt + '\n\nOutput strictly in JSON format: {"compressed_summary": "YOUR TEXT HERE"}'
    
    print(f"Compressing context (Current len: {len(text)} chars)...")

    response = call_gpt_api(api_key, system_prompt, json_user_prompt, model=model, max_retries=1)
    
    if response:
        try:
            data = json.loads(response)
            return data.get("compressed_summary", text)
        except:
            pass
    
    print("Compression failed or returned invalid data. Using original text.")
    return text