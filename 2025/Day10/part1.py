import re
from collections import deque

def parse_and_solve(file_path):
    try:
        with open(file_path, 'r') as f:
            raw_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return

    cleaned_content = re.sub(r'"', "", raw_content)

    cleaned_content = cleaned_content.replace("\n", " ")

    segments = cleaned_content.split('}')

    total_presses = 0
    machine_count = 0

    for segment in segments:
        if not segment.strip():
            continue


        pattern_match = re.search(r"\[([.#]+)\]", segment)
        if not pattern_match:
            continue

        pattern_str = pattern_match.group(1)

        button_matches = re.findall(r"\(([\d,]+)\)", segment)

        if not button_matches:
            continue

        target_mask = 0
        for i, char in enumerate(pattern_str):
            if char == '#':
                target_mask |= (1 << i)

        buttons = []
        for btn_str in button_matches:
            btn_mask = 0
            indices = [int(x) for x in btn_str.split(',') if x.strip()]
            for idx in indices:
                btn_mask |= (1 << idx)
            buttons.append(btn_mask)

        # --- BFS for Shortest Path ---
        # Find fewest presses to transform 0 (all off) -> target_mask
        min_steps = bfs_solve(target_mask, buttons)

        total_presses += min_steps
        machine_count += 1

    print(f"Processed {machine_count} machines.")
    print(f"Total fewest button presses required: {total_presses}")

def bfs_solve(target, buttons):
    if target == 0:
        return 0

    # Queue stores: (current_state_mask, number_of_presses)
    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        current_state, steps = queue.popleft()

        if current_state == target:
            return steps

        for btn_mask in buttons:
            next_state = current_state ^ btn_mask # XOR to toggle lights

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))

    return 0

if __name__ == "__main__":
    parse_and_solve("/content/input.txt.txt")