from collections import deque
from typing import Dict, List, Tuple

def parse_input(input_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) for c in line.strip()] for line in input_str.strip().split('\n')]

def get_neighbors(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """Get valid neighboring positions (up, down, left, right)."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    return [(x + dx, y + dy) for dx, dy in directions 
            if 0 <= x + dx < rows and 0 <= y + dy < cols]

# Part 2: Counting distinct trails
def count_distinct_trails(grid: List[List[int]], start_x: int, start_y: int) -> int:
    """Count number of distinct hiking trails from a trailhead."""
    rows, cols = len(grid), len(grid[0])
    memo: Dict[Tuple[int, int, int], int] = {}

    def dfs(x: int, y: int, height: int) -> int:
        state = (x, y, height)
        if state in memo:
            return memo[state]

        if grid[x][y] == 9:
            return 1

        trails = 0
        for next_x, next_y in get_neighbors(x, y, rows, cols):
            next_height = grid[next_x][next_y]
            if next_height == height + 1:
                trails += dfs(next_x, next_y, next_height)

        memo[state] = trails
        return trails

    return dfs(start_x, start_y, 0)

def solve_part2(grid: List[List[int]]) -> int:
    """Solve Part 2 of the puzzle."""
    rows, cols = len(grid), len(grid[0])
    total_trails = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                total_trails += count_distinct_trails(grid, i, j)

    return total_trails

input_str = """Your Puzzle Input Here"""

grid = parse_input(input_str)

part2_result = solve_part2(grid)
print(f"Part 2 Result: {part2_result}")
