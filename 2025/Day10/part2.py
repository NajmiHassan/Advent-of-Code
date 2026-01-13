import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def parse_and_solve_part2(file_path):
    try:
        with open(file_path, 'r') as f:
            raw_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return

    # --- Preprocessing ---
    # 1. Remove tags using the correct regex
    cleaned_content = re.sub(r'"', "", raw_content)

    # 2. Normalize whitespace (remove newlines)
    cleaned_content = cleaned_content.replace("\n", " ")

    # 3. Split into machine segments.
    # In the input, machines end with the joltage block {....}.
    # We split by '}' to isolate each machine.
    segments = cleaned_content.split('}')

    total_presses = 0
    machine_count = 0

    for segment in segments:
        if not segment.strip():
            continue

        # --- Parse Target Joltages ---
        # Look for the curly braces {3,5,4,7}
        joltage_match = re.search(r"\{([\d,]+)\}", segment + "}") # Add } back for regex matching if needed
        
        joltage_match = re.search(r"\{([\d,]+)", segment)

        if not joltage_match:
            continue

        joltage_strs = joltage_match.group(1).split(',')
        target_vector = np.array([int(x) for x in joltage_strs if x.strip()])
        num_counters = len(target_vector)

        # --- Parse Buttons ---
        # Find all (0,1,2) patterns
        button_matches = re.findall(r"\(([\d,]+)\)", segment)

        if not button_matches:
            continue

        # Build the constraint matrix A
        # Rows = counters, Cols = buttons
        num_buttons = len(button_matches)
        A = np.zeros((num_counters, num_buttons))

        for col_idx, btn_str in enumerate(button_matches):
            indices = [int(x) for x in btn_str.split(',') if x.strip()]
            for row_idx in indices:
                if row_idx < num_counters:
                    A[row_idx, col_idx] = 1

        # --- Solve ILP ---
        min_presses = solve_ilp(A, target_vector)

        if min_presses is not None:
            total_presses += min_presses
            machine_count += 1
        else:
            print(f"Warning: No solution found for machine {machine_count+1}")

    print(f"Processed {machine_count} machines.")
    print(f"Total fewest button presses required: {int(total_presses)}")

def solve_ilp(A, target):
    
    n_vars = A.shape[1]
    c = np.ones(n_vars) # Objective: minimize sum of variables

    # Constraints: A @ x == target
    # In milp, equality is defined by setting lower_bound == upper_bound
    constraints = LinearConstraint(A, target, target)

    # Integrality: 1 means integer constraint
    integrality = np.ones(n_vars)

    # Bounds: x >= 0
    bounds = Bounds(0, np.inf)

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    if res.success:
        # Round to nearest integer to avoid floating point drift
        return int(round(res.fun))
    else:
        return None

if __name__ == "__main__":
    parse_and_solve_part2("/content/input.txt.txt")