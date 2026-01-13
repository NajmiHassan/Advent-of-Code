import sys

# Increase recursion depth just in case the path is very long
sys.setrecursionlimit(10000)

def solve():
    graph = {}

    # 1. Parse the input file
    try:
        with open("/content/input.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please make sure the file is in the same directory.")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Parse lines in the format "aaa: bbb ccc ddd"
        if ":" in line:
            parts = line.split(":")
            source_node = parts[0].strip()
            # The destinations are space-separated after the colon
            destinations = parts[1].strip().split()
            graph[source_node] = destinations

    # 2. Define DFS with Memoization
    memo = {}

    def count_paths(current_node):
        # Base Case: We reached the target
        if current_node == 'out':
            return 1

        # Check Cache: If we already calculated paths from this node, return it
        if current_node in memo:
            return memo[current_node]

        # Recursive Step: Sum paths from all neighbors
        path_count = 0

        # If the node has outgoing connections defined in the graph
        if current_node in graph:
            for neighbor in graph[current_node]:
                path_count += count_paths(neighbor)

        # Store result in cache and return
        memo[current_node] = path_count
        return path_count

    # 3. Calculate and Print Result
    # We start counting from the node labeled 'you'
    if 'you' not in graph:
        print("Error: Start node 'you' not found in input.")
    else:
        total_paths = count_paths('you')
        print(f"Total paths from 'you' to 'out': {total_paths}")

if __name__ == "__main__":
    solve()