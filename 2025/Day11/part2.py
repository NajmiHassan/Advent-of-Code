import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(10000)

def solve():
    graph = {}

    # 1. Parse the input file
    try:
        with open("/content/input.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if ":" in line:
            parts = line.split(":")
            source = parts[0].strip()
            # Destinations are space-separated
            dests = parts[1].strip().split()
            graph[source] = dests

    # 2. Define a generic path counter with memoization
    # We use a cache dictionary where keys are (start_node, end_node)
    memo = {}

    def count_paths(current_node, target_node):
        # Base Case: Reached the specific target
        if current_node == target_node:
            return 1

        # Check Cache
        if (current_node, target_node) in memo:
            return memo[(current_node, target_node)]

        # Recursive Step
        total = 0
        if current_node in graph:
            for neighbor in graph[current_node]:
                # Optimization: In a DAG, if we are strictly looking for a path TO target,
                # we just sum the paths from neighbors to target.
                total += count_paths(neighbor, target_node)

        memo[(current_node, target_node)] = total
        return total

    # 3. Verify nodes exist
    # [cite_start]Based on input data, we look for 'svr' [cite: 9][cite_start], 'dac' [cite: 3][cite_start], 'fft'[cite: 8], and 'out'
    required_nodes = ['svr', 'dac', 'fft', 'out']
    for node in required_nodes:
        # Note: 'out' might not be a key in 'graph' if it has no children, so we check keys mostly for start points
        # but the recursive function handles missing keys gracefully (returns 0)
        pass

    print("Calculating paths...")

    # 4. Calculate segments for Sequence A: svr -> dac -> fft -> out
    svr_to_dac = count_paths('svr', 'dac')
    dac_to_fft = count_paths('dac', 'fft')
    fft_to_out = count_paths('fft', 'out')

    paths_sequence_a = svr_to_dac * dac_to_fft * fft_to_out

    # 5. Calculate segments for Sequence B: svr -> fft -> dac -> out
    svr_to_fft = count_paths('svr', 'fft')
    fft_to_dac = count_paths('fft', 'dac')
    dac_to_out = count_paths('dac', 'out')

    paths_sequence_b = svr_to_fft * fft_to_dac * dac_to_out

    # 6. Total
    total_paths = paths_sequence_a + paths_sequence_b

    print(f"--- Results ---")
    print(f"Sequence A (svr->dac->fft->out): {paths_sequence_a}")
    print(f"Sequence B (svr->fft->dac->out): {paths_sequence_b}")
    print(f"Total paths visiting both: {total_paths}")

if __name__ == "__main__":
    solve()