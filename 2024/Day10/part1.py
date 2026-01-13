from collections import deque
from typing import List, Tuple


def parse_input(input_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) for c in line.strip()] for line in input_str.strip().split('\n')]

def get_neighbors(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """Get valid neighboring positions (up, down, left, right)."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    return [(x + dx, y + dy) for dx, dy in directions 
            if 0 <= x + dx < rows and 0 <= y + dy < cols]

# Part 1: Finding reachable nines
def find_reachable_nines(grid: List[List[int]], start_x: int, start_y: int) -> int:
    """Find number of height-9 positions reachable from a trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    reachable_nines = set()
    queue = deque([(start_x, start_y, 0)])
    visited.add((start_x, start_y, 0))

    while queue:
        x, y, height = queue.popleft()
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for next_x, next_y in get_neighbors(x, y, rows, cols):
            next_height = grid[next_x][next_y]
            if next_height == height + 1 and (next_x, next_y, next_height) not in visited:
                visited.add((next_x, next_y, next_height))
                queue.append((next_x, next_y, next_height))

    return len(reachable_nines)

def solve_part1(grid: List[List[int]]) -> int:
    """Solve Part 1 of the puzzle."""
    rows, cols = len(grid), len(grid[0])
    total_reachable_nines = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                total_reachable_nines += find_reachable_nines(grid, i, j)

    return total_reachable_nines

input_str = """Your Puzzle Input Here"""
grid = parse_input(input_str)

part1_result = solve_part1(grid)
print(f"Part 1 Result: {part1_result}")
