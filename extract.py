import re
import os
import glob
import argparse
from collections import defaultdict

# Configuration 
DEFAULT_ROOT_FOLDER = r"" 


try:
    from graphviz import Digraph
    HAS_GRAPHVIZ = True
except ImportError:
    HAS_GRAPHVIZ = False

class RoutePlanner:
    def __init__(self):
        self.label_map = {}
        self.file_graph = defaultdict(set)
        self.file_content = {}
        self.visual_edges = []
        
        self.re_label = re.compile(r'^\s*label\s+(\w+):')
        self.re_jump = re.compile(r'^\s*jump\s+(\w+)')
        self.re_call = re.compile(r'^\s*call\s+(\w+)')
        self.re_menu = re.compile(r'^\s*menu\s*:')
        self.re_choice = re.compile(r'^\s*"(.*)"\s*:')
        self.re_if = re.compile(r'^\s*if\s+')
        self.re_elif = re.compile(r'^\s*elif\s+')
        self.re_else = re.compile(r'^\s*else\s*:')
    
    def scan_project(self, file_paths):
        for path in file_paths:
            fname = os.path.basename(path)
            try:
                with open(path, 'r', encoding='utf-8') as f: 
                    content = f.read()
            except:
                try: 
                    with open(path, 'r', encoding='utf-8-sig') as f: 
                        content = f.read()
                except: 
                    continue
            
            self.file_content[fname] = content.split('\n')
            for line in self.file_content[fname]:
                clean = line.split('#')[0].strip()
                match = self.re_label.match(clean)
                if match:
                    self.label_map[match.group(1)] = fname

        for fname, lines in self.file_content.items():
            self._analyze_connections(fname, lines)

    def _analyze_connections(self, fname, lines):
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            indent = len(line) - len(line.lstrip())
            
            if not stripped or stripped.startswith("#"):
                i += 1
                continue
            
            target_label = None
            
            j_match = self.re_jump.match(stripped)
            if j_match: 
                target_label = j_match.group(1)
            
            if not target_label:
                c_match = self.re_call.match(stripped)
                if c_match: 
                    target_label = c_match.group(1)
            
            if target_label and target_label in self.label_map:
                target_file = self.label_map[target_label]
                if target_file != fname:
                    self.file_graph[fname].add(target_file)
                    self.visual_edges.append((fname, target_file, ""))

            if self.re_menu.match(stripped):
                menu_indent = indent
                j = i + 1
                
                choice_targets = []
                choice_texts = []
                
                while j < len(lines):
                    sub = lines[j]
                    sub_stripped = sub.strip()
                    sub_indent = len(sub) - len(sub.lstrip())
                    
                    if sub_indent <= menu_indent and sub_stripped: 
                        break
                    
                    c_match = self.re_choice.match(sub)
                    if c_match:
                        c_text = c_match.group(1)
                        choice_texts.append(c_text)
                        k = j + 1
                        found_target = None

                        while k < len(lines):
                            inner = lines[k]
                            inner_stripped = inner.strip()
                            inner_indent = len(inner) - len(inner.lstrip())
                            
                            if inner_indent <= sub_indent and inner_stripped: 
                                break
                            
                            if not inner_stripped or inner_stripped.startswith("#"):
                                k += 1
                                continue
                            
                            i_jump = self.re_jump.match(inner_stripped)
                            i_call = self.re_call.match(inner_stripped)
                            
                            if i_jump or i_call:
                                t_lbl = i_jump.group(1) if i_jump else i_call.group(1)
                                
                                if t_lbl in self.label_map:
                                    t_file = self.label_map[t_lbl]
                                    found_target = t_file
                                    break
                            
                            k += 1
                        
                        if not found_target:
                            found_target = fname
                        
                        choice_targets.append(found_target)
                    j += 1
                
                unique_targets = set(choice_targets)
                unique_external_targets = set(t for t in unique_targets if t != fname)
                
                if len(unique_external_targets) > 1:
                    for idx, target in enumerate(choice_targets):
                        if target != fname:
                            self.file_graph[fname].add(target)
                            clean_text = choice_texts[idx][:15] + ".." if len(choice_texts[idx]) > 15 else choice_texts[idx]
                            self.visual_edges.append((fname, target, clean_text))
                elif len(unique_external_targets) == 1:
                    target = list(unique_external_targets)[0]
                    self.file_graph[fname].add(target)
                    self.visual_edges.append((fname, target, "[interaction]"))

                
                i = j
                continue
            
            i += 1

    def calculate_routes(self, start_label="start"):
        start_file = None
        
        if start_label in self.label_map:
            start_file = self.label_map[start_label]
            print(f" Starting from label '{start_label}' ({start_file})")
        elif "chapter1" in self.label_map:
            start_file = self.label_map["chapter1"]
            print(f" Starting from 'chapter1' ({start_file})")
        elif self.label_map:
            # Exclude script.rpy (usually just init definitions)
            files = [f for f in self.file_content.keys() if f != 'script.rpy']
            if files:
                start_file = sorted(files)[0]
                print(f" Starting from the first file ({start_file})")
            else:
                start_file = list(self.file_content.keys())[0]
                print(f" Starting from the only file ({start_file})")
        else:
            print("  No labels found.")
            return []
        
        if not start_file:
            print("  Could not determine the starting file.")
            return []

        # Find all paths using DFS
        all_routes = []
        stack = [(start_file, [start_file])]
        visited_states = set()
        
        while stack:
            curr, path = stack.pop()
            
            # Avoid redundant state processing
            state = (curr, tuple(path))
            if state in visited_states:
                continue
            visited_states.add(state)
            
            next_nodes = self.file_graph.get(curr, set())
            
            if not next_nodes:
                # Reached a leaf node (complete route)
                all_routes.append(path)
            else:
                for nxt in sorted(next_nodes):  # Sort for consistency
                    if nxt not in path:  # Prevent infinite loops
                        stack.append((nxt, path + [nxt]))
        
        # Remove duplicate routes
        unique = []
        seen = set()
        for r in all_routes:
            t = tuple(r)
            if t not in seen:
                unique.append(r)
                seen.add(t)
        
        # Diagnostics
        print(f"File graph: {len(self.file_graph)} files connected.")
        for fname, targets in sorted(self.file_graph.items()):
            if targets:
                print(f"      {fname} -> {', '.join(sorted(targets))}")
        
        if not unique:
            print("   Warning: No complete routes found.")
            print("   Possible reasons:")
            print("      - All files are interconnected (circular dependency)")
            print("      - The starting file lacks jump statements")
            print("      - No connections established between files")
            
            # Fallback to single file if no routes found
            if start_file:
                print(f"   Falling back to single-file route: [{start_file}]")
                return [[start_file]]
        
        return unique

class GraphArtist:
    """Generate flowcharts."""
    def __init__(self, edges):
        self.edges = edges 

    def draw(self, output_dir, project_name):
        print(" [Stage 2] Generating flowchart...")
        if not os.path.exists(output_dir): 
            os.makedirs(output_dir)
        
        m_path = os.path.join(output_dir, "file_topology.mmd")
        with open(m_path, 'w', encoding='utf-8') as f:
            f.write("graph TD\n")
            f.write("    classDef fileNode fill:#e1f5fe,stroke:#01579b,stroke-width:2px;\n")
            
            nodes = set()
            for s, t, _ in self.edges:
                nodes.add(s)
                nodes.add(t)
            
            for n in nodes:
                f.write(f"    {n.replace('.', '_')}[{n}]:::fileNode\n")
            
            merged_edges = defaultdict(list)
            for s, t, txt in self.edges:
                merged_edges[(s, t)].append(txt)
            
            for (s, t), txts in merged_edges.items():
                s_id, t_id = s.replace('.', '_'), t.replace('.', '_')
                valid_txts = [t for t in txts if t]
                if valid_txts:
                    label = " / ".join(valid_txts)
                    f.write(f"    {s_id} -->|{label}| {t_id}\n")
                else:
                    f.write(f"    {s_id} --> {t_id}\n")

        if HAS_GRAPHVIZ:
            try:
                dot = Digraph(comment=project_name, format='png')
                dot.attr(rankdir='TB')
                dot.attr('node', shape='note', style='filled', fillcolor='#e3f2fd', fontname="Arial")
                
                merged_edges = defaultdict(list)
                for s, t, txt in self.edges:
                    merged_edges[(s, t)].append(txt)

                for (s, t), txts in merged_edges.items():
                    valid_txts = [t for t in txts if t]
                    label = " / ".join(valid_txts)
                    dot.edge(s, t, label=label, color="#546e7a", fontsize="10")
                
                dot.render(filename=os.path.join(output_dir, "file_topology"), cleanup=True)
                print("   PNG flowchart generated.")
            except Exception as e:
                pass

class StoryTeller:
    """Extract player-visible story text."""
    def __init__(self, planner):
        self.planner = planner
        self.re_menu = re.compile(r'^\s*menu\s*:')
        self.re_choice = re.compile(r'^\s*"(.*)"\s*:')
        self.re_jump = re.compile(r'^\s*jump\s+(\w+)')
        self.re_dialogue = re.compile(r'^\s*(\w+)\s+"(.*)"')
        self.re_narrator = re.compile(r'^\s*"(.*)"')

    def extract_route(self, route_chain):
        """Extract the full story for a given route."""
        story_lines = []
        next_step_map = {route_chain[i]: route_chain[i+1] for i in range(len(route_chain)-1)}
        
        for file_name in route_chain:
            target_next_file = next_step_map.get(file_name, None)
            file_text = self._process_file(file_name, target_next_file)
            if file_text:
                story_lines.extend(file_text)
        
        return story_lines

    def _is_technical_line(self, line):
        """Check if a line is a technical script command (hidden from player)."""
        stripped = line.strip()
        
        if not stripped or stripped.startswith("#"):
            return True
        
        # Menu choice lines are not narration, must be excluded before checking technical_starts
        if self.re_choice.match(stripped):
            return True
        
        technical_starts = [
            'label ', 'jump ', 'call ', 'return', 'menu:',
            'show ', 'scene ', 'hide ', 'with ', 'at ',
            'play ', 'stop ', 'pause', 'window ',
            'define ', 'default ', 'init ', 'transform ',
            'image ', 'python:', 'if ', 'elif ', 'else:',
            'while ', 'for ', '$', 'zoom ', 'xalign ', 'yalign ',
            'voice ', 'extend ', 'nvl ', 'centered ',
        ]
        
        return any(stripped.startswith(kw) for kw in technical_starts)

    def _extract_text(self, line):
        """Extract dialogue or narration."""
        stripped = line.strip()
        
        # Narration: "text" (Must precede dialogue check to avoid capturing quoted technical args)
        narrator = self.re_narrator.match(stripped)
        if narrator:
            return narrator.group(1)
        
        # Character dialogue: character "text"
        dlg = self.re_dialogue.match(stripped)
        if dlg:
            return f"{dlg.group(1)}: \"{dlg.group(2)}\""
        
        return None

    def _process_file(self, filename, required_next_file):
        """Process a file and extract only story content."""
        lines = self.planner.file_content[filename]
        output = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Handle menus
            if self.re_menu.match(stripped):
                menu_result = self._process_menu(lines, i, required_next_file)
                if menu_result['content']:
                    output.extend(menu_result['content'])
                i = menu_result['next_index']
                continue
            
            # Skip script commands
            if self._is_technical_line(line):
                i += 1
                continue
            
            # Extract story text
            text = self._extract_text(line)
            if text:
                output.append(text)
            
            i += 1
        
        return output

    def _process_menu(self, lines, start_index, required_next_file):
        """Process a menu block to extract choices and nested content."""
        menu_indent = len(lines[start_index]) - len(lines[start_index].lstrip())
        result = {'content': [], 'next_index': start_index + 1}
        
        choices = []
        j = start_index + 1
        
        # Parse all choices
        while j < len(lines):
            sub = lines[j]
            sub_indent = len(sub) - len(sub.lstrip())
            
            if sub_indent <= menu_indent and sub.strip():
                break
            
            choice_match = self.re_choice.match(sub)
            if choice_match:
                choice_text = choice_match.group(1)
                choice_data = self._extract_choice(lines, j)
                choices.append({
                    'text': choice_text,
                    'target': choice_data['target'],
                    'content': choice_data['content']
                })
                j = choice_data['next_index']
            else:
                if not self._is_technical_line(sub):
                    caption = self._extract_text(sub)
                    if caption:
                        result['content'].append(caption)
                j += 1
        
        result['next_index'] = j
        
        # Locate the main route choice
        if required_next_file:
            for choice in choices:
                if choice['target'] == required_next_file:
                    result['content'].append(f"\n[Choice: \"{choice['text']}\"]")
                    if choice['content']:
                        result['content'].extend(choice['content'])
                    result['content'].append("")
                    return result
        
        if len(choices) > 0:
            result['content'].append("\n[Available Choices:]")
            for choice in choices:
                result['content'].append(f"  • {choice['text']}")
                if choice['content']:
                    for line in choice['content']:
                        result['content'].append(f"      {line}")
            result['content'].append("")
        
        return result

    def _extract_choice(self, lines, choice_index):
        """Extract the contents of a single choice block."""
        choice_indent = len(lines[choice_index]) - len(lines[choice_index].lstrip())
        content = []
        target = None
        k = choice_index + 1
        
        while k < len(lines):
            inner = lines[k]
            inner_indent = len(inner) - len(inner.lstrip())
            
            if inner_indent <= choice_indent and inner.strip():
                break
            
            # Find jump targets
            jump_match = self.re_jump.match(inner.strip())
            if jump_match:
                label = jump_match.group(1)
                if label in self.planner.label_map:
                    target = self.planner.label_map[label]
            
            # Extract dialogue
            if not self._is_technical_line(inner):
                text = self._extract_text(inner)
                if text:
                    content.append(text)
            
            k += 1
        
        return {'content': content, 'target': target, 'next_index': k}

def process_case_folder(case_path):
    """Process a single case directory."""
    case_name = os.path.basename(case_path)
    chapter_renpy_path = os.path.join(case_path, "chapter_renpy")
    
    if not os.path.exists(chapter_renpy_path):
        print(f" Skipping {case_name}: 'chapter_renpy' folder not found.")
        return
    
    print(f"\n{'='*70}")
    print(f"Processing Case: {case_name}")
    print(f"{'='*70}")
    
    files = glob.glob(os.path.join(chapter_renpy_path, "*.rpy"))
    
    if not files:
        print(" No .rpy files found.")
        return
    
    print(f" Found {len(files)} .rpy files:")
    for f in sorted(files):
        print(f"   - {os.path.basename(f)}")
    
    # 1. Planning phase
    planner = RoutePlanner()
    planner.scan_project(files)
    
    print("\n Label mapping:")
    if planner.label_map:
        for label, fname in sorted(planner.label_map.items()):
            print(f"   {label} -> {fname}")
    else:
        print(" No labels found.")
    
    # 2. Route calculation
    print("\n Calculating story routes...")
    routes = planner.calculate_routes()
    
    if not routes:
        print(" Failed to calculate routes.")
        return
    
    print(f"\n Identified {len(routes)} story routes:")
    for idx, route in enumerate(routes, 1):
        print(f"   Route {idx}: {' -> '.join(route)}")
    
    # 3. Filter valid files
    valid_files = set()
    for r in routes:
        valid_files.update(r)
    
    print(f"\n Files used in routes: {len(valid_files)}")
    unused_files = set(os.path.basename(f) for f in files) - valid_files
    if unused_files:
        print(f"     Unused files: {', '.join(sorted(unused_files))}")
        
    filtered_edges = [
        e for e in planner.visual_edges 
        if e[0] in valid_files and e[1] in valid_files
    ]

    # 4. Flowchart generation
    print("\n Generating flowchart...")
    artist = GraphArtist(filtered_edges)
    out_dir = os.path.join(case_path, "Story_Routes")
    artist.draw(out_dir, case_name)

    # 5. Story extraction
    print("\n Extracting story content...")
    teller = StoryTeller(planner)
    for idx, route_chain in enumerate(routes):
        story_text = teller.extract_route(route_chain)
        
        filename = f"Route_{idx+1}.txt"
        filepath = os.path.join(out_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(story_text))
        
        # Stats
        line_count = len(story_text)
        char_count = sum(len(line) for line in story_text)
        print(f"   {filename}: {line_count} lines, {char_count} chars")
    
    print(f"\n {case_name} processing complete!")
    print(f"   Output directory: {out_dir}")

def find_all_cases(results_dir):
    """Locate all case folders."""
    case_folders = []
    
    if not os.path.exists(results_dir):
        print(f"Directory does not exist: {results_dir}")
        return case_folders
    
    for category in os.listdir(results_dir):
        category_path = os.path.join(results_dir, category)
        if not os.path.isdir(category_path):
            continue
        
        for subcategory in os.listdir(category_path):
            subcategory_path = os.path.join(category_path, subcategory)
            if not os.path.isdir(subcategory_path):
                continue
            
            for case_folder in os.listdir(subcategory_path):
                case_path = os.path.join(subcategory_path, case_folder)
                if not os.path.isdir(case_path):
                    continue
                
                if os.path.isdir(os.path.join(case_path, "chapter_renpy")):
                    case_folders.append(case_path)
    
    return case_folders

def main():
    parser = argparse.ArgumentParser(description="Extract story content from Ren'Py projects.")
    parser.add_argument("folder", nargs="?", help="Root directory for results")
    args = parser.parse_args()
    
    root = args.folder
    if not root:
        if DEFAULT_ROOT_FOLDER: 
            root = DEFAULT_ROOT_FOLDER
        else: 
            root = input("Enter the path to the results folder: ").strip().replace('"', '').replace("'", "")
    
    if not os.path.exists(root): 
        print("Path does not exist.")
        return
    
    case_folders = find_all_cases(root)
    
    if not case_folders:
        print("No cases found.")
        return
    
    print(f"\nFound {len(case_folders)} cases.")
    
    print("\n" + "=" * 60)
    for case_path in case_folders:
        try:
            process_case_folder(case_path)
        except Exception as e:
            case_name = os.path.basename(case_path)
            print(f" Error processing {case_name}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Done! Results are saved in the 'Story_Routes' folder of each case.")

if __name__ == "__main__":
    main()