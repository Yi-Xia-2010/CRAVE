import subprocess
import time
import sys
import os
import glob
import json
import re
from rich.console import Console
from utils import sanitize_filename

# 初始化 Rich 控制台
console = Console()

# --- 1. 基础配置 ---
FIXED_THEME = "Climate Change"
FIXED_GENRE = ["Romance"]

# 获取脚本所在目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 生成任务列表
TASK_DICT = {}
for genre in FIXED_GENRE:
    task = []
    for i in range(1):
        for curve_id in range(1, 7):
            task.append({
                "id": f"Curve_{curve_id}_Story_{i+1}", 
                "theme": FIXED_THEME, 
                "genre": genre, 
                "curve": str(curve_id)
            })
    TASK_DICT[genre] = task


def get_actual_chapter_count(world_dir):
    """
    [核心逻辑] 读取 story_outline 文件确定章节总数。
    [FIX] 优先读取原始大纲，或者非空的 Corrected 大纲，防止被错误的空文件误导。
    """
    try:
        if not world_dir or not os.path.exists(world_dir):
            return None
        
        # 1. 优先找原始大纲 (story_outline_X.json)，因为它是基准
        # 排除 _CORRECTED 以防止读取到错误的 0 章节文件
        all_files = glob.glob(os.path.join(world_dir, "story_outline_*.json"))
        raw_files = [f for f in all_files if "_CORRECTED" not in f]
        
        target_file = None
        if raw_files:
            target_file = max(raw_files, key=os.path.getmtime)
        elif all_files:
            target_file = max(all_files, key=os.path.getmtime)
            
        if not target_file: return None
        
        with open(target_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            count = len(data.get('chapter_structure', []))
            # 如果读出来是 0，说明这个文件坏了，返回 None 强制脚本不要跳过
            return count if count > 0 else None
            
    except Exception:
        return None

def main():
    for genre in FIXED_GENRE:
        console.rule("[bold green]🚀 BATCH GENERATION SYSTEM (FLAT STRUCTURE)[/bold green]")
        console.print(f"🌍 Theme: {FIXED_THEME} | Genre: {genre}\n")
        
        start_time = time.time()
        # 切换工作目录
        os.chdir(ROOT_DIR)
        TASKS = TASK_DICT[genre]
        for i, task in enumerate(TASKS):
            idx = i + 1
            task_id = task['id']
            
            # --- 2. 路径对齐 ---
            raw_safe_theme = sanitize_filename(task['theme'])
            raw_safe_genre = sanitize_filename(task['genre'])
            safe_theme = re.sub(r'_+', '_', raw_safe_theme).strip('_')
            safe_genre = re.sub(r'_+', '_', raw_safe_genre).strip('_')
            
            base_results = os.path.abspath(os.path.join("results", safe_theme, safe_genre))
            world_dir = os.path.join(base_results, f"World_{task_id}")
            
            common_args = ["--project_path", world_dir]
            
            # --- 3. 第一阶段：世界设定 ---
            existing_world_files = glob.glob(os.path.join(world_dir, "world_setting_*.json"))
            if not existing_world_files:
                console.print(f"[{idx:02d}/{len(TASKS)}] [bold white]🆕 STARTING[/bold white] | {task_id}")
                os.makedirs(world_dir, exist_ok=True)

                subprocess.run([
                    sys.executable, "world_setting_generator.py",
                    "--theme", task['theme'],
                    "--genre", task['genre'],
                    "--chapters", "6", 
                    "--no-input",
                    "--tag", task_id 
                ], check=True)
            else:
                console.print(f"[{idx:02d}/{len(TASKS)}] [bold blue]⏩ World Ready[/bold blue] | {task_id}")

            # --- 4. 进度判断 ---
            target_count = get_actual_chapter_count(world_dir)
            script_dir = os.path.join(world_dir, "Scripts_Text")
            current_count = len(glob.glob(os.path.join(script_dir, "script_ch*.txt")))

            # [FIX] 只有当目标数量有效且 > 0 时才判断完成
            if target_count and target_count > 0 and current_count >= target_count:
                console.print(f"      [bold green]✔ COMPLETE[/bold green] ({current_count}/{target_count} chs)")
                continue
            else:
                prog_str = f"{current_count}/{target_count if target_count else '?'}"
                console.rule(f"[bold yellow]⏳ RESUMING {task_id} ({prog_str})[/bold yellow]")

            # --- 5. 执行流水线 ---
            try:
                # Step 2: Outline
                # 只要有任何 outline (包括 corrected) 且非空，就认为 Step 2 完成
                # 但这里我们主要依赖下面的 Step 2.5 来修复结构

                outline_pattern = os.path.join(world_dir, "story_outline_*.json")
                if not glob.glob(outline_pattern):
                    console.print(f"   ✍️  Drafting Outline...")
                    subprocess.run([
                        sys.executable, "outline_generator.py",
                        "--arc", task['curve'], 
                        "--theme", task['theme'],
                        "--genre", task['genre'],
                        "--id", task['id'],
                        "--no-input",
                        "--project_path", world_dir
                    ], check=True)
                
                # Step 2.5: Structure Analysis (CRITICAL FIX)
                # 即使 _CORRECTED 存在，如果它是坏的(空)，也要重跑
                corrected_files = glob.glob(os.path.join(world_dir, "*_CORRECTED.json"))
                need_analysis = True
                if corrected_files:
                    # 检查文件大小或内容是否有效
                    try:
                        with open(corrected_files[0], 'r') as f:
                            d = json.load(f)
                            if len(d.get('chapter_structure', [])) > 0:
                                need_analysis = False
                    except: pass
                
                if need_analysis:
                    console.print(f"   🔍 Analyzing Structure (Fixing IDs)...")
                    subprocess.run([sys.executable, "structure_analyzer.py"] + common_args, check=True)
                
                # # Step 3: Chapter Details
                # subprocess.run([sys.executable, "chapter_outline_generator.py"] + common_args, check=True)
                
                # Step 4: Scripts
                subprocess.run([sys.executable, "script_generator.py", "--theme", task['theme'], "--genre", task['genre'],"--id", task['id']] + common_args, check=True)

                console.print(f"      [bold green]✅ Success![/bold green]\n")

            except subprocess.CalledProcessError as e:
                console.print(f"      [bold red]❌ Failed: {e}[/bold red]")
                continue

        total_duration = (time.time() - start_time) / 60
        console.rule(f"[bold green]🎉 BATCH FINISHED IN {total_duration:.2f} MINS[/bold green]")

if __name__ == "__main__":
    main()