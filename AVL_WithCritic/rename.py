import os
import re

# 设置 results 目录路径
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")

# 匹配模式：World_Story_数字_Curve_数字
pattern = re.compile(r'^(World)_Story_(\d+)_Curve_(\d+)$')

print("=== 文件重命名工具 ===")
print("1. 交换 Story 和 Curve 的位置（World_Story_X_Curve_Y → World_Curve_Y_Story_X）")
print("2. 统一修改 Story 数字")
print("3. 统一修改 Curve 数字")
print("4. 交换位置 + 统一修改 Story 数字")
print("5. 交换位置 + 统一修改 Curve 数字")
print("6. 统一修改 Story 和 Curve 数字")
print("7. 交换位置 + 统一修改 Story 和 Curve 数字")

mode = input("\n请选择操作模式（1-7）：").strip()
if mode not in {"1", "2", "3", "4", "5", "6", "7"}:
    print("输入无效，请输入 1-7。")
    exit(1)

# 根据模式决定是否需要输入数字
target_story = None
target_curve = None

if mode in {"2", "4", "6", "7"}:
    target_story = input("请输入目标 Story 数字：").strip()
    if not target_story.isdigit():
        print("输入无效，请输入一个整数。")
        exit(1)

if mode in {"3", "5", "6", "7"}:
    target_curve = input("请输入目标 Curve 数字：").strip()
    if not target_curve.isdigit():
        print("输入无效，请输入一个整数。")
        exit(1)

def build_new_name(prefix, story_num, curve_num, mode):
    s = target_story if target_story else story_num
    c = target_curve if target_curve else curve_num
    if mode in {"1", "4", "5", "7"}:
        return f"{prefix}_Curve_{c}_Story_{s}"
    else:
        return f"{prefix}_Story_{s}_Curve_{c}"

renamed_count = 0
skipped_count = 0

for root, dirs, files in os.walk(base_dir, topdown=False):
    # 处理文件夹名
    for name in dirs:
        match = pattern.match(name)
        if match:
            prefix, story_num, curve_num = match.groups()
            new_name = build_new_name(prefix, story_num, curve_num, mode)
            if new_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                print(f"[文件夹] {name}  →  {new_name}")
                os.rename(old_path, new_path)
                renamed_count += 1

    # 处理文件名（保留扩展名）
    for name in files:
        base_name, ext = os.path.splitext(name)
        match = pattern.match(base_name)
        if match:
            prefix, story_num, curve_num = match.groups()
            new_base = build_new_name(prefix, story_num, curve_num, mode)
            if new_base != base_name:
                new_name = new_base + ext
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                print(f"[文  件] {name}  →  {new_name}")
                os.rename(old_path, new_path)
                renamed_count += 1
        else:
            skipped_count += 1

print(f"\n完成！共重命名 {renamed_count} 个，跳过 {skipped_count} 个不匹配项。")