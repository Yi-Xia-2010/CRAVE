import os
import json
import glob
import datetime
import argparse
import re
import copy
from datetime import datetime
from collections import defaultdict, deque

try:
    from graphviz import Digraph
    HAS_GRAPHVIZ = True
except ImportError:
    HAS_GRAPHVIZ = False


# 1. Basic Utilities
def get_latest_outline(base_dir="results"):
    search_pattern = os.path.join(base_dir, "**", "story_outline_*.json")
    files = glob.glob(search_pattern, recursive=True)
    raw_files = [f for f in files if "_CORRECTED" not in f]
    
    if not raw_files: 
        if files: return max(files, key=os.path.getmtime)
        return None
    return max(raw_files, key=os.path.getmtime)

def clean_json_text(text):
    text = re.sub(r'^```json\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^```\s*', '', text, flags=re.MULTILINE)
    return text.strip()

def clean_title_strict(title):
    if not title: return ""
    t = str(title).strip().lower()
    t = t.rstrip('.,;!?')
    return t

def clean_title_fuzzy(title):
    if not title: return ""
    clean = re.sub(r'\[.*?\]', '', str(title))
    clean = re.sub(r'[^\w\s]', '', clean)
    return clean.strip().lower()

def find_target_by_priority(parent_id, target_info, id_map, existing_connections):
    target_title = target_info.get('target_chapter_title', '')
    target_id = target_info.get('target_chapter_id') or target_info.get('target_chapter_index')
    target_branch = target_info.get('target_branch', '')
    
    # 0. Check invalid ID (-1 indicates no target)
    if target_id and str(target_id) == "-1":
        return None, "Target ID is -1 (No target)"
    
    # 1. Full title match (Highest priority)
    if target_title:
        clean_target = clean_title_strict(target_title)
        for node_id, node_data in id_map.items():
            if node_id == parent_id:
                continue
            node_title = node_data.get('chapter_title', '')
            if node_title and clean_title_strict(node_title) == clean_target:
                # Check for cycle
                if not (node_id, parent_id) in existing_connections:
                    return node_id, f"Full title match: '{target_title}' -> '{node_title}'"
    
    # 2. ID match (Second priority)
    if target_id and str(target_id) != "-1":
        try:
            tid = int(target_id)
            if tid in id_map and tid != parent_id:
                # Check for cycle
                if not (tid, parent_id) in existing_connections:
                    return tid, f"ID match: {target_id} -> {tid}"
        except ValueError:
            pass
    
    # 3. Cleaned title match (Remove emotion tags)
    if target_title:
        core_target = extract_title_without_emotion(target_title).lower()
        for node_id, node_data in id_map.items():
            if node_id == parent_id:
                continue
            node_title = node_data.get('chapter_title', '')
            if node_title:
                core_node = extract_title_without_emotion(node_title).lower()
                if core_node and core_target and core_node == core_target:
                    # Check for cycle
                    if not (node_id, parent_id) in existing_connections:
                        return node_id, f"Cleaned title match: '{core_target}' -> '{core_node}'"
    
    # 4. Branch + Title keyword match
    if target_branch and target_title:
        core_target = extract_title_without_emotion(target_title).lower()
        target_keywords = set(core_target.split())
        
        for node_id, node_data in id_map.items():
            if node_id == parent_id:
                continue
            node_branch = node_data.get('branch_designation', '')
            node_title = node_data.get('chapter_title', '')
            
            if node_branch and node_title:
                # Branch match (exact equality to avoid e.g. "A" matching "Branch A Extended")
                if target_branch == node_branch:
                    core_node = extract_title_without_emotion(node_title).lower()
                    node_keywords = set(core_node.split())
                    
                    # Check keyword overlap
                    if target_keywords & node_keywords:
                        # Check for cycle
                        if not (node_id, parent_id) in existing_connections:
                            return node_id, f"Branch + Keyword match: {target_branch}, keywords overlap"
    
    # 5. Branch match
    if target_branch:
        for node_id, node_data in id_map.items():
            if node_id == parent_id:
                continue
            node_branch = node_data.get('branch_designation', '')
            # Exact equality to avoid substring false positives
            if node_branch and node_branch == target_branch:
                # Check for cycle
                if not (node_id, parent_id) in existing_connections:
                    return node_id, f"Branch match: {target_branch}"
    
    # No match found
    return None, "No match found"

def extract_emotion_tag(title):
    if not title:
        return None
    match = re.search(r'\[(.*?)\]', title)
    return match.group(1).lower() if match else None

def extract_title_without_emotion(title):
    if not title:
        return ""
    # Remove bracketed content
    clean = re.sub(r'\s*\[.*?\]', '', str(title))
    return clean.strip()

def find_all_paths(graph, start_node):
    routes = []
    if start_node not in graph: return []
    
    # Stack structure: (current_node, current_path)
    stack = [(start_node, [start_node])]
    max_iterations = 50000 
    iterations = 0
    
    while stack:
        iterations += 1
        if iterations > max_iterations: break
        
        current, path = stack.pop()
        children = graph.get(current, [])
        
        if not children:
            routes.append(path)
        else:
            for child in children:
                if child not in path: # Simple cycle prevention
                    stack.append((child, path + [child]))
    return routes

def parse_entry_condition(entry_condition):

    if not entry_condition:
        return None, None

    entry_lower = entry_condition.lower().strip()

    if entry_lower.startswith("none") or "start" in entry_lower:
        return None, "start"

    match = re.search(r'from chapter\s+(\d+)', entry_lower)
    if not match:
        return None, None

    parent_idx = int(match.group(1))
    link_type = "option" if "option" in entry_lower else "default"
    return parent_idx, link_type


def rescue_orphans_by_entry_condition(
    chapters, id_map, index_to_id, children_map,
    existing_connections, start_node_id
):

    log = []
    added = 0

    def _has_parent_set():
        hp = set()
        for p, ch_list in children_map.items():
            for c in ch_list:
                hp.add(c)
        return hp

    start_ids = set()
    for ch in chapters:
        entry = ch.get('entry_condition', '')
        uid = ch.get('id') or ch.get('chapter_index')
        if 'start' in entry.lower() or entry.lower().startswith('none'):
            start_ids.add(uid)

    has_parent = _has_parent_set()

    orphans = [
        ch for ch in chapters
        if (ch.get('id') or ch.get('chapter_index')) not in has_parent
        and (ch.get('id') or ch.get('chapter_index')) not in start_ids
    ]

    if not orphans:
        log.append("No orphaned chapters remain for entry_condition rescue.")
        return added, log

    log.append(f"Found {len(orphans)} orphaned chapter(s), starting entry_condition rescue...")

    for ch in orphans:
        uid = ch.get('id') or ch.get('chapter_index')
        entry = ch.get('entry_condition', '')
        parent_idx, link_type = parse_entry_condition(entry)

        if parent_idx is None:
            log.append(f"  Ch{uid}: No parseable entry_condition, skipping.")
            continue

        parent_id = index_to_id.get(parent_idx)
        if parent_id is None and parent_idx in id_map:
            parent_id = parent_idx

        if parent_id is None:
            fallback = start_node_id
            if fallback == uid or (uid, fallback) in existing_connections:
                log.append(
                    f"  Ch{uid}: Parent Ch{parent_idx} missing; "
                    f"fallback Ch{fallback} skipped (self-loop or reverse edge)."
                )
                continue
            if (fallback, uid) in existing_connections:
                log.append(f"  Ch{uid}: Already connected from Ch{fallback}.")
                has_parent.add(uid)
                continue

            existing_connections.add((fallback, uid))
            children_map.setdefault(fallback, [])
            if uid not in children_map[fallback]:
                children_map[fallback].append(uid)
            has_parent.add(uid)
            log.append(
                f"  [TypeB] Ch{fallback}(start) --> Ch{uid} "
                f"(parent Ch{parent_idx} missing, fallback to start node)"
            )
            added += 1
            continue

        if parent_id == uid:
            continue
        if (parent_id, uid) in existing_connections:
            has_parent.add(uid)
            continue
        if (uid, parent_id) in existing_connections:
            log.append(f"  Ch{uid}: Reverse edge to Ch{parent_id} exists, skipping.")
            continue

        parent_ch = id_map[parent_id]
        parent_decision = parent_ch.get('major_decision_point', {})
        parent_has_choice = parent_decision.get('has_choice', False)

        if parent_has_choice:
            options = parent_decision.get('options', [])
            fixed = False
            entry_lower = entry.lower()

            for opt in options:
                opt_target = opt.get('target_chapter_index') or opt.get('target_chapter_id')
                if opt_target and int(opt_target) != -1:
                    continue

                opt_label = opt.get('label', '').strip()
                if opt_label:
                    first_letter = opt_label[0].lower()
                    if re.search(r'\boption\b.*\b' + re.escape(first_letter) + r'\b', entry_lower):
                        opt['target_chapter_index'] = uid
                        opt['target_chapter_id'] = uid
                        existing_connections.add((parent_id, uid))
                        children_map.setdefault(parent_id, [])
                        if uid not in children_map[parent_id]:
                            children_map[parent_id].append(uid)
                        has_parent.add(uid)
                        log.append(
                            f"  [TypeC] Ch{parent_id}.option['{opt.get('label')}'] "
                            f"target -1 → {uid} (entry_condition reverse inference)"
                        )
                        fixed = True
                        added += 1
                        break

            if not fixed:
                existing_connections.add((parent_id, uid))
                children_map.setdefault(parent_id, [])
                if uid not in children_map[parent_id]:
                    children_map[parent_id].append(uid)
                has_parent.add(uid)
                log.append(
                    f"  [TypeC-fallback] Ch{parent_id} --> Ch{uid} "
                    f"(no exact option slot matched, implicit edge added)"
                )
                added += 1

        else:
            existing_connections.add((parent_id, uid))
            children_map.setdefault(parent_id, [])
            if uid not in children_map[parent_id]:
                children_map[parent_id].append(uid)
            has_parent.add(uid)

            current_default = parent_ch.get('default_next_chapter', -1)
            if current_default in (-1, 0, None):
                parent_ch['default_next_chapter'] = uid
                log.append(
                    f"  [TypeA] Ch{parent_id}.default_next_chapter "
                    f"-1 → {uid} (field rewritten + linear edge added)"
                )
            else:
                log.append(
                    f"  [TypeA] Ch{parent_id} --> Ch{uid} "
                    f"(linear edge added, existing default_next={current_default})"
                )
            added += 1

    return added, log


# 2.1 Smart Connection Validation & Repair System
def resolve_target_node(target_val, id_map):

    if target_val is None: return None
    
    # 1. Try direct ID match
    try:
        t_int = int(target_val)
        if t_int in id_map: return t_int
    except: pass
    
    # 2. Try Index match (Fallback mechanism)
    target_str = str(target_val)
    for cid, data in id_map.items():
        c_idx = data.get('chapter_index')
        if c_idx is not None and str(c_idx) == target_str:
            return cid
            
    return None

def compute_connection_quality(parent_node, child_node, target_info):

    score = 0
    
    # 1. Title match (Highest weight)
    target_title = target_info.get('target_chapter_title', '')
    child_title = child_node.get('chapter_title', '')
    
    if target_title and child_title:
        # Exact title match (including emotion tags)
        clean_target = clean_title_strict(target_title)
        clean_child = clean_title_strict(child_title)
        
        if clean_target and clean_child:
            if clean_target == clean_child:
                score += 5  # Exact match
    
    # 2. Emotion tag consistency check
    target_emotion = extract_emotion_tag(target_title)
    child_emotion = extract_emotion_tag(child_title)
    
    if target_emotion and child_emotion:
        if target_emotion == child_emotion:
            score += 2  # Emotion tags match
        else:
            score -= 1  # Emotion tags mismatch
    
    # 3. Branch match
    target_branch = target_info.get('target_branch', '')
    child_branch = child_node.get('branch_designation', '')
    parent_branch = parent_node.get('branch_designation', '')
    
    if target_branch and child_branch:
        # Exact branch match
        if target_branch == child_branch:
            score += 3
        # Branch subset relationship
        elif target_branch in child_branch or child_branch in target_branch:
            score += 2
    
    # 4. Branch transition logic check
    if parent_branch and child_branch:
        # Spine to Limb is a common transition
        if "spine" in parent_branch.lower() and "limb" in child_branch.lower():
            score += 1
        # Transition within the same branch
        elif parent_branch == child_branch:
            score += 1
        # Control to Sealed Command is a special transition
        elif "control" in parent_branch.lower() and "sealed command" in child_branch.lower():
            score += 1
        # Protective to Haven Hoarder is a special transition
        elif "protective" in parent_branch.lower() and "haven hoarder" in child_branch.lower():
            score += 1
    
    return score

def detect_all_cycles(children_map):

    cycles_found = []
    visited = set()
    
    # DFS to detect cycles
    def dfs(node, current_path):
        # If node is already in current path, cycle found
        if node in current_path:
            # Find cycle start index
            start_index = current_path.index(node)
            cycle = current_path[start_index:] + [node]
            return cycle
        
        # If node already visited and not in current path, skip
        if node in visited:
            return None
        
        # Mark node as visited
        visited.add(node)
        
        # Add node to current path
        new_path = current_path + [node]
        
        # Recursively check children
        for child in children_map.get(node, []):
            cycle = dfs(child, new_path)
            if cycle:
                return cycle
        
        return None
    
    # DFS on all unvisited nodes
    for node in list(children_map.keys()):
        if node not in visited:
            cycle = dfs(node, [])
            if cycle:
                cycles_found.append(cycle)
    
    return cycles_found

def break_cycles_intelligently(children_map, id_map):

    cycles = detect_all_cycles(children_map)
    cycles_broken = 0
    broken_connections = []
    
    fixed_children_map = copy.deepcopy(children_map)
    
    for cycle in cycles:
        if len(cycle) <= 2:  # Self-loop or direct back-loop
            # Directly break the last connection
            if len(cycle) == 2:  # Self-loop
                parent = cycle[0]
                child = cycle[0]
                if child in fixed_children_map.get(parent, []):
                    fixed_children_map[parent].remove(child)
                    cycles_broken += 1
                    broken_connections.append((parent, child, f"Broke self-loop"))
            elif len(cycle) == 3:  # Direct loop A->B, B->A
                parent = cycle[0]
                child = cycle[1]
                if child in fixed_children_map.get(parent, []):
                    fixed_children_map[parent].remove(child)
                    cycles_broken += 1
                    broken_connections.append((parent, child, f"Broke direct loop"))
        else:
            # For complex cycles, find and break the weakest connection
            weakest_score = float('inf')
            weakest_connection = None
            
            for i in range(len(cycle)-1):
                parent = cycle[i]
                child = cycle[i+1]
                
                # Compute connection quality (simplified)
                parent_node = id_map.get(parent, {})
                child_node = id_map.get(child, {})
                
                score = 0
                parent_branch = parent_node.get('branch_designation', '')
                child_branch = child_node.get('branch_designation', '')
                
                # Same branch connections have higher quality
                if parent_branch and child_branch and parent_branch == child_branch:
                    score += 2
                
                # Natural index progression has higher quality
                parent_idx = parent_node.get('chapter_index', 0)
                child_idx = child_node.get('chapter_index', 0)
                if child_idx > parent_idx:
                    score += 1
                elif child_idx == parent_idx:
                    score += 0
                else:
                    score -= 1  # Index regression, lower quality
                
                if score < weakest_score:
                    weakest_score = score
                    weakest_connection = (parent, child)
            
            # Break weakest connection
            if weakest_connection:
                parent, child = weakest_connection
                if child in fixed_children_map.get(parent, []):
                    fixed_children_map[parent].remove(child)
                    cycles_broken += 1
                    broken_connections.append((parent, child, f"Broke complex cycle (score {weakest_score})"))
    
    return fixed_children_map, cycles_broken, broken_connections


# 2.2 Core Smart Analysis Logic
def analyze_structure(outline_data):
    working_data = copy.deepcopy(outline_data)
    chapters = working_data.get('chapter_structure', [])
    
    # Build indexes
    id_map = {}
    title_to_id_map = {}
    
    for ch in chapters:
        # Compatibility handling: prioritize id, fallback to chapter_index
        uid = ch.get('id') or ch.get('chapter_id') or ch.get('chapter_index')
        if uid is None: continue
        uid = int(uid)
        
        # Force writeback standard ID
        ch['id'] = uid
        ch['chapter_index'] = uid 
        
        id_map[uid] = ch
        
        raw_title = ch.get('chapter_title')
        if raw_title:
            title_to_id_map[clean_title_strict(raw_title)] = uid

    # chapter_index -> id map (for entry_condition rescue)
    index_to_id = {
        int(ch.get('chapter_index', ch.get('id'))): int(ch.get('id'))
        for ch in chapters if ch.get('id') is not None
    }

    print(f"   - Smart connection repair ({len(id_map)} nodes total)...")
    
    # Connection statistics
    stats = {
        'total_connections_processed': 0,
        'connections_fixed': 0,
        'title_matches': 0,
        'branch_matches': 0,
        'id_resolutions': 0,
        'self_loops_prevented': 0,
        'direct_cycles_prevented': 0,
        'default_next_fixed': 0,
        # entry_condition rescue stats (new)
        'entry_rescue_added': 0,
        'entry_rescue_typeA': 0,
        'entry_rescue_typeB': 0,
        'entry_rescue_typeC': 0,
    }
    
    # Record all established connections (to prevent cycles)
    existing_connections = set()
    

    # Step 1: Repair option connections
    print("   - Step 1: Repairing option connections...")
    
    for parent_id, parent_node in id_map.items():
        decision = parent_node.get('decision_point') or parent_node.get('major_decision_point') or {}
        options = decision.get('options', [])
        
        for option_idx, option in enumerate(options):
            stats['total_connections_processed'] += 1
            
            # Priority search
            target_id, reason = find_target_by_priority(parent_id, option, id_map, existing_connections)
            
            if target_id:
                # Check for self-loop
                if target_id == parent_id:
                    stats['self_loops_prevented'] += 1
                    print(f"       Ch {parent_id} Option {option_idx}: Prevented self-loop")
                    option['target_chapter_id'] = -1
                    option['target_chapter_index'] = -1
                else:
                    # Check for direct cycle
                    if (target_id, parent_id) in existing_connections:
                        stats['direct_cycles_prevented'] += 1
                        print(f"       Ch {parent_id} -> Ch {target_id} (Option {option_idx}): Prevented direct cycle")
                        option['target_chapter_id'] = -1
                        option['target_chapter_index'] = -1
                    else:
                        # Apply repair
                        original_id = option.get('target_chapter_id') or option.get('target_chapter_index')
                        if str(original_id) != str(target_id):
                            option['target_chapter_id'] = target_id
                            option['target_chapter_index'] = target_id
                            stats['connections_fixed'] += 1
                            
                            # Log match type
                            if "Full title" in reason or "Cleaned title" in reason:
                                stats['title_matches'] += 1
                            elif "ID match" in reason:
                                stats['id_resolutions'] += 1
                            elif "Branch" in reason:
                                stats['branch_matches'] += 1
                            
                            print(f"      Ch {parent_id} Option {option_idx}: {original_id} -> {target_id} ({reason})")
                        
                        # Record connection
                        existing_connections.add((parent_id, target_id))
            else:
                # Target not found
                original_id = option.get('target_chapter_id') or option.get('target_chapter_index')
                if original_id and str(original_id) != "-1":
                    if reason != "Target ID is -1 (No target)":
                        print(f"      Ch {parent_id} Option {option_idx}: Target not found (Original: {original_id}, Reason: {reason})")
                    # Set to -1 to indicate no target
                    option['target_chapter_id'] = -1
                    option['target_chapter_index'] = -1
    

    # Step 2: Repair default connections
    print("   - Step 2: Repairing default connections...")
    
    for parent_id, parent_node in id_map.items():
        def_next = parent_node.get('default_next_chapter') or parent_node.get('default_next_chapter_id')
        
        # Special case: 0 should be treated as -1 (No next chapter)
        if def_next == 0:
            parent_node['default_next_chapter'] = -1
            if 'default_next_chapter_id' in parent_node:
                parent_node['default_next_chapter_id'] = -1
            stats['default_next_fixed'] += 1
            continue
        
        if def_next and str(def_next) != "-1":
            stats['total_connections_processed'] += 1
            
            # Create target info
            target_info = {
                'target_chapter_id': def_next,
                'target_chapter_index': def_next,
                'target_chapter_title': parent_node.get('default_next_chapter_title', ''),
                'target_branch': parent_node.get('default_next_branch', '')
            }
            
            # Priority search
            target_id, reason = find_target_by_priority(parent_id, target_info, id_map, existing_connections)
            
            if target_id:
                # Check for self-loop
                if target_id == parent_id:
                    stats['self_loops_prevented'] += 1
                    print(f"       Ch {parent_id} Default Next: Prevented self-loop")
                    parent_node['default_next_chapter'] = -1
                    parent_node['default_next_chapter_id'] = -1
                else:
                    # Check for direct cycle
                    if (target_id, parent_id) in existing_connections:
                        stats['direct_cycles_prevented'] += 1
                        print(f"       Ch {parent_id} -> Ch {target_id} (Default): Prevented direct cycle")
                        parent_node['default_next_chapter'] = -1
                        parent_node['default_next_chapter_id'] = -1
                    else:
                        # Apply repair
                        if str(def_next) != str(target_id):
                            parent_node['default_next_chapter'] = target_id
                            parent_node['default_next_chapter_id'] = target_id
                            stats['connections_fixed'] += 1
                            print(f"      Ch {parent_id} Default Next: {def_next} -> {target_id} ({reason})")
                        
                        # Record connection
                        existing_connections.add((parent_id, target_id))
            else:
                # Target not found
                if reason != "Target ID is -1 (No target)":
                    print(f"      Ch {parent_id} Default Next: Target not found (Original: {def_next}, Reason: {reason})")
                # Set to -1 to indicate no target
                parent_node['default_next_chapter'] = -1
                parent_node['default_next_chapter_id'] = -1
    

    # Step 3: Build connection graph
    print("   - Step 3: Building connection graph...")
    children_map = {}
    parent_map = {}
    
    # Initialize empty lists for all nodes
    for uid in id_map.keys():
        children_map[uid] = []
        parent_map[uid] = []
    
    # Apply existing connections
    for parent_id, child_id in existing_connections:
        if child_id in id_map:  # Ensure child exists
            if child_id not in children_map[parent_id]:
                children_map[parent_id].append(child_id)
            if parent_id not in parent_map[child_id]:
                parent_map[child_id].append(parent_id)
    

    # Step 4: Detect and break cycles
    print("   - Step 4: Detecting and breaking cycles...")
    children_map, cycles_broken, broken_details = break_cycles_intelligently(children_map, id_map)
    
    # Add cycle info to stats
    stats['cycles_broken'] = cycles_broken
    stats['broken_connections'] = broken_details
    
    # Rebuild parent_map (ensure all nodes have entries)
    parent_map = {}
    # Initialize all nodes first
    for uid in id_map.keys():
        parent_map[uid] = []
    # Add connections
    for parent, children in children_map.items():
        for child in children:
            if child not in parent_map:
                parent_map[child] = []
            if parent not in parent_map[child]:
                parent_map[child].append(parent)
    

    # Step 5: Determine starting node
    VALID_START_ID = 101
    if VALID_START_ID not in id_map:
        found_start = resolve_target_node(1, id_map)
        if found_start: 
            VALID_START_ID = found_start
        elif id_map:
            VALID_START_ID = min(id_map.keys())
    
    print(f"      Using start node: ID {VALID_START_ID}")
    
    # Find all paths
    raw_paths = find_all_paths(children_map, VALID_START_ID)
    
    valid_node_ids = set()
    clean_routes = []
    
    if raw_paths:
        print(f"      Found {len(raw_paths)} paths")
        for path in raw_paths:
            if path and path[0] == VALID_START_ID:
                for nid in path: 
                    valid_node_ids.add(nid)
                end_id = path[-1]
                branch = id_map[end_id].get('branch_designation', 'Unknown')
                clean_routes.append({
                    "end_id": end_id, 
                    "branch_name": branch, 
                    "path": path, 
                    "length": len(path)
                })
    else:
        if VALID_START_ID in id_map: 
            valid_node_ids.add(VALID_START_ID)
            clean_routes.append({
                "end_id": VALID_START_ID,
                "branch_name": id_map[VALID_START_ID].get('branch_designation', 'Unknown'),
                "path": [VALID_START_ID],
                "length": 1
            })
    

    # Step 6: Proper orphan node detection and removal
    print("   - Step 6: Detecting orphan nodes...")
    
    # Build set of all nodes that have a parent
    has_parent = set()
    for parent_id, child_id in existing_connections:
        has_parent.add(child_id)
    
    # True orphans are nodes with no parents that aren't the start node
    true_orphans = set()
    
    for uid in id_map.keys():
        if uid not in has_parent and uid != VALID_START_ID:
            true_orphans.add(uid)
    

    # Generalized Orphan Rescue (Replaces hardcoded logic)
    rescued_orphans = set()
    for orphan_id in list(true_orphans):
        for parent_id, parent_node in id_map.items():
            is_connected = False
            
            # 1. Check if implicit default_next_chapter points here
            def_next = parent_node.get('default_next_chapter') or parent_node.get('default_next_chapter_id')
            if def_next is not None and str(def_next) == str(orphan_id):
                is_connected = True
                
            # 2. Check options just in case it was missed by the priority heuristic
            if not is_connected:
                decision = parent_node.get('decision_point') or parent_node.get('major_decision_point') or {}
                for opt in decision.get('options', []):
                    opt_target = opt.get('target_chapter_id') or opt.get('target_chapter_index')
                    if opt_target is not None and str(opt_target) == str(orphan_id):
                        is_connected = True
                        break
                        
            if is_connected:
                print(f"      Rescue orphan: Implicit connection {parent_id} -> {orphan_id} recovered")
                # Ensure connection is recorded in all tracking sets
                if (parent_id, orphan_id) not in existing_connections:
                    existing_connections.add((parent_id, orphan_id))
                    has_parent.add(orphan_id)
                    # CRITICAL FIX: Explicitly update children_map so DFS traversal works
                    if orphan_id not in children_map.get(parent_id, []):
                        children_map.setdefault(parent_id, []).append(orphan_id)
                rescued_orphans.add(orphan_id)
                break  # Found at least one parent, move to the next orphan

    # Remove all successfully rescued nodes from the true_orphans set
    for ro in rescued_orphans:
        true_orphans.discard(ro)


    print("   - Step 6.5 (NEW): entry_condition-based orphan rescue...")

    rescue_added, rescue_log = rescue_orphans_by_entry_condition(
        chapters, id_map, index_to_id,
        children_map, existing_connections, VALID_START_ID
    )
    for line in rescue_log:
        print(f"      {line}")

    if rescue_added > 0:
        print(f"    entry_condition rescue: +{rescue_added} connection(s) added")
        stats['entry_rescue_added'] = rescue_added
        for line in rescue_log:
            if '[TypeA]' in line: stats['entry_rescue_typeA'] += 1
            elif '[TypeB]' in line: stats['entry_rescue_typeB'] += 1
            elif '[TypeC]' in line or '[TypeC-fallback]' in line: stats['entry_rescue_typeC'] += 1
    else:
        print(f"      No additional connections recovered.")


    # Step 6.5 may have connected nodes that were still in true_orphans;
    # rebuild has_parent from children_map (which was updated in-place) and
    # remove any newly-rescued nodes so the log below is accurate.
    has_parent = set()
    for _p, _clist in children_map.items():
        for _c in _clist:
            has_parent.add(_c)
    true_orphans -= has_parent  # drop nodes that now have a parent


    # (Step 4 ran before Step 6.5, so new edges were not checked)
    if rescue_added > 0:
        children_map, extra_cycles, extra_broken = break_cycles_intelligently(children_map, id_map)
        if extra_cycles > 0:
            stats['cycles_broken'] = stats.get('cycles_broken', 0) + extra_cycles
            print(f"    Post-rescue cycle check: broke {extra_cycles} additional cycle(s)")

    # Log orphan nodes
    if true_orphans:
        print(f"    Found {len(true_orphans)} true orphan node(s):")
        for oid in sorted(true_orphans):
            node_data = id_map[oid]
            title = node_data.get('chapter_title', 'Unknown')
            branch = node_data.get('branch_designation', 'Unknown')
            print(f"        Removed {oid}: {title} [{branch}]")
    else:
        print(f"      No orphan nodes found")
    
    # Step 7: Recalculate valid nodes (including all with parents)
    valid_node_ids = set()
    # Find all reachable nodes from start
    raw_paths = find_all_paths(children_map, VALID_START_ID)
    
    # FIX: Rebuild clean_routes here so route count reflects post-rescue topology
    clean_routes = []

    if raw_paths:
        for path in raw_paths:
            for nid in path:
                valid_node_ids.add(nid)
            if path and path[0] == VALID_START_ID:
                end_id = path[-1]
                branch = id_map[end_id].get('branch_designation', 'Unknown')
                clean_routes.append({
                    "end_id": end_id,
                    "branch_name": branch,
                    "path": path,
                    "length": len(path)
                })
    else:
        # Include at least start node if no paths
        valid_node_ids.add(VALID_START_ID)
        if VALID_START_ID in id_map:
            clean_routes.append({
                "end_id": VALID_START_ID,
                "branch_name": id_map[VALID_START_ID].get('branch_designation', 'Unknown'),
                "path": [VALID_START_ID],
                "length": 1
            })
    
    # Re-verify to ensure all nodes with parents are included
    for child_id in has_parent:
        if child_id in id_map and child_id not in valid_node_ids:
            # Node has parent but isn't in path (complex topology)
            # Add to valid nodes
            print(f"      Node {child_id} has parent but not in path, preserving")
            valid_node_ids.add(child_id)
    

    # Step 8: Clean graph, remove connections to orphans
    print("   - Step 8: Cleaning connection graph...")
    
    # Clean children_map, remove connections pointing to orphans
    for parent_id in list(children_map.keys()):
        # If parent is an orphan, remove entire entry
        if parent_id not in valid_node_ids:
            del children_map[parent_id]
        else:
            # Remove child nodes that are orphans
            children_map[parent_id] = [c for c in children_map.get(parent_id, []) if c in valid_node_ids]
    
    # Clean parent_map
    for child_id in list(parent_map.keys()):
        if child_id not in valid_node_ids:
            del parent_map[child_id]
        else:
            parent_map[child_id] = [p for p in parent_map.get(child_id, []) if p in valid_node_ids]
    
    # Rebuild parent_map (ensure all valid nodes have entries)
    parent_map = {}
    for uid in valid_node_ids:
        parent_map[uid] = []
    
    for parent, children in children_map.items():
        for child in children:
            if child in valid_node_ids and parent not in parent_map[child]:
                parent_map[child].append(parent)
    

    # Step 9: Recalculate topology
    print("   - Step 9: Recalculating topology...")
    
    # Ensure all valid nodes have entries in children_map and parent_map
    for uid in valid_node_ids:
        if uid not in children_map:
            children_map[uid] = []
        if uid not in parent_map:
            parent_map[uid] = []
    
    # Retain only valid connections
    for parent_id in list(children_map.keys()):
        if parent_id not in valid_node_ids:
            del children_map[parent_id]
        else:
            children_map[parent_id] = [c for c in children_map[parent_id] if c in valid_node_ids]
    
    # Rebuild parent_map again
    parent_map = {}
    for uid in valid_node_ids:
        parent_map[uid] = []
    
    for parent, children in children_map.items():
        for child in children:
            if child in valid_node_ids and parent not in parent_map[child]:
                parent_map[child].append(parent)
    

    # Step 10: Generate final result
    final_chapters = []
    for cid in sorted(list(valid_node_ids)):
        if cid in id_map:
            final_chapters.append(id_map[cid])

    working_data['chapter_structure'] = final_chapters
    working_data['_meta_correction_log'] = "Fixed by Structure Analyzer"
    working_data['generated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build clean_id_map for chart generation
    clean_id_map = {}
    for uid in valid_node_ids:
        clean_id_map[uid] = id_map[uid]

    # Build topology_result (matches provided example format)
    topology_result = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_chapters": len(clean_id_map),
        "total_valid_routes": len(clean_routes),
        "orphans_removed": len(id_map) - len(valid_node_ids),
        "routes": clean_routes,
        "chapter_topology": {},
        "connection_stats": stats  # FIX: was never written, making main() stats output dead code
    }

    # Build chapter_topology (id, title, branch, children_ids only)
    for uid in valid_node_ids:
        node_data = id_map[uid]
        # Keys remain integers (compatible with drawing functions)
        topology_result['chapter_topology'][uid] = {
            "id": uid,
            "title": node_data.get('chapter_title'),
            "branch": node_data.get('branch_designation'),
            "children_ids": [c for c in children_map.get(uid, []) if c in valid_node_ids]
        }

    # Return 3 values to maintain backwards compatibility
    return topology_result, clean_id_map, working_data


# 3. Visualization & Main Loop
def get_node_style(branch_name):
    b = str(branch_name).upper()
    if "SPINE" in b or "COMMON" in b: return "spine"
    return "limb"

def generate_mermaid(topology_data, id_map, output_path):

    lines = ["graph TD"]
    lines.append("    classDef spine fill:#fff3e0,stroke:#e65100,stroke-width:3px;")
    lines.append("    classDef limb fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;")
    
    # Ensure id_map nodes exist in topology_data
    for uid, data in id_map.items():
        if str(uid) in topology_data['chapter_topology']:
            topology_node = topology_data['chapter_topology'][str(uid)]
        elif uid in topology_data['chapter_topology']:
            topology_node = topology_data['chapter_topology'][uid]
        else:
            # Skip if not in topology
            continue
            
        title = data.get('chapter_title', 'Untitled')
        branch = data.get('branch_designation', 'Unknown')
        idx = data.get('chapter_index', uid)
        safe_title = title.replace('"', '').replace('\n', ' ')[:20]
        css = get_node_style(branch)
        lines.append(f"    {uid}(\"Ch {idx}<br/>{safe_title}<br/>[{branch}]\"):::{css}")

    # Add edges
    for uid in id_map.keys():
        # Attempt both key formats to access topology data
        if str(uid) in topology_data['chapter_topology']:
            children = topology_data['chapter_topology'][str(uid)]['children_ids']
        elif uid in topology_data['chapter_topology']:
            children = topology_data['chapter_topology'][uid]['children_ids']
        else:
            children = []
        
        decision = id_map[uid].get('decision_point') or id_map[uid].get('major_decision_point') or {}
        opts = decision.get('options', [])
        
        linked = set()
        for opt in opts:
            tid = opt.get('target_chapter_id')
            if tid and tid in children:
                label = opt.get('label', 'Choice')[:15].replace('"', '') + "..."
                lines.append(f"    {uid} -->|{label}| {tid}")
                linked.add(tid)
        
        # Add unmarked connections
        for child in children:
            if child not in linked:
                lines.append(f"    {uid} -.-> {child}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f" Mermaid Saved: {os.path.basename(output_path)}")

def generate_graphviz(topology_data, id_map, output_base):

    if not HAS_GRAPHVIZ: 
        return
    
    try:
        dot = Digraph(comment='S.T.A.R.', format='png')
        dot.attr(rankdir='TB')
        dot.attr('node', shape='rect', style='filled,rounded', fontname='Helvetica')
        
        # Add nodes
        for uid, data in id_map.items():
            idx = data.get('chapter_index', uid)
            title = data.get('chapter_title', '')
            branch = data.get('branch_designation', '')
            style = get_node_style(branch)
            colors = {'spine':('#fff3e0','#ef6c00'), 'limb':('#f3e5f5','#8e24aa')}
            fc, c = colors.get(style, ('#f5f5f5', '#999999'))
            label = f"Ch {idx}\n{title}\n[{branch}]"
            dot.node(str(uid), label=label, fillcolor=fc, color=c)
        
        # Add edges
        for uid in id_map.keys():
            # Attempt both key formats to access topology data
            if str(uid) in topology_data['chapter_topology']:
                children = topology_data['chapter_topology'][str(uid)]['children_ids']
            elif uid in topology_data['chapter_topology']:
                children = topology_data['chapter_topology'][uid]['children_ids']
            else:
                children = []
            
            for child in children:
                dot.edge(str(uid), str(child))
        
        out = dot.render(filename=output_base, cleanup=True)
        print(f" Graphviz Saved: {os.path.basename(out)}")
    except Exception as e:
        print(f" Graphviz Error: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--project_path", type=str)
    args = parser.parse_args()

    filepath = None
    if args.file: filepath = args.file
    elif args.project_path: filepath = get_latest_outline(args.project_path)
    else: filepath = get_latest_outline()

    if not filepath or not os.path.exists(filepath):
        print(" File not found.")
        return
        
    print(f" Analyzing: {os.path.basename(filepath)}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.loads(clean_json_text(f.read()))
    except Exception as e:
        print(f" Read Error: {e}")
        return

    try:
        pdir = os.path.dirname(filepath)
        
        # Execute smart analysis, returning 3 values
        topo, clean_id_map, corrected_outline = analyze_structure(data)
        
        # Save topology info
        with open(os.path.join(pdir, "project_topology.json"), 'w', encoding='utf-8') as f:
            json.dump(topo, f, indent=2, ensure_ascii=False)

        # Save corrected story outline
        base_name = os.path.basename(filepath)
        new_name = base_name if "_CORRECTED" in base_name else base_name.replace(".json", "_CORRECTED.json")
        with open(os.path.join(pdir, new_name), 'w', encoding='utf-8') as f:
            json.dump(corrected_outline, f, indent=2, ensure_ascii=False)
            
        print(f"\n Corrected Outline Saved: {new_name}")
        
        if topo['total_chapters'] == 0:
            print(" WARNING: Resulting structure is EMPTY. Check input JSON.")
        
        # Generate charts
        generate_mermaid(topo, clean_id_map, os.path.join(pdir, "project_structure.mmd"))
        generate_graphviz(topo, clean_id_map, os.path.join(pdir, "project_structure_graph"))
        
        print(f"\n Analysis Complete!")
        print(f"    Statistics:")
        print(f"     - Total Chapters: {topo['total_chapters']}")
        print(f"     - Valid Routes: {topo.get('total_valid_routes', 0)}")
        print(f"     - Orphans Removed: {topo['orphans_removed']}")
        
        # Extract connection stats from topology_result (if present)
        if 'connection_stats' in topo:
            conn_stats = topo['connection_stats']
            print(f"     - Connections Processed: {conn_stats.get('total_connections_processed', 0)}")
            print(f"     - Connections Fixed: {conn_stats.get('connections_fixed', 0)}")
            if conn_stats.get('title_matches', 0) > 0:
                print(f"     - Title Matches Repaired: {conn_stats.get('title_matches', 0)}")
            if conn_stats.get('self_loops_prevented', 0) > 0:
                print(f"     - Self-loops Prevented: {conn_stats.get('self_loops_prevented', 0)}")
            # entry_condition rescue stats (new)
            total_rescue = conn_stats.get('entry_rescue_added', 0)
            if total_rescue > 0:
                print(f"     - entry_condition Rescue: +{total_rescue} connection(s)")
                print(f"       TypeA (linear default_next=-1): {conn_stats.get('entry_rescue_typeA', 0)}")
                print(f"       TypeB (missing parent->start):  {conn_stats.get('entry_rescue_typeB', 0)}")
                print(f"       TypeC (option target=-1):       {conn_stats.get('entry_rescue_typeC', 0)}")
        
        if 'cycles_broken' in topo and topo.get('cycles_broken', 0) > 0:
            print(f"       Broken {topo['cycles_broken']} cycles")
        
    except Exception as e:
        print(f" Analysis Error: {e}")
        import traceback
        traceback.print_exc()
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()