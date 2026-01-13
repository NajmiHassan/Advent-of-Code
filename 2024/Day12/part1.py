from collections import deque

def parse_map(input_map):
    return [list(row) for row in input_map.strip().split("\n")]

def calculate_area_and_perimeter(grid, visited, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    plant_type = grid[start_row][start_col]
    area = 0
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # BFS or DFS to explore the region
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == plant_type:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                else:
                    # Adjacent cell is a different type; contributes to perimeter
                    perimeter += 1
            else:
                # Out of bounds; contributes to perimeter
                perimeter += 1

    return area, perimeter

def calculate_total_price(input_map):
    grid = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Calculate area and perimeter for each region
                area, perimeter = calculate_area_and_perimeter(grid, visited, r, c)
                total_price += area * perimeter

    return total_price

input_map = """Your Puzzle Input Here"""

print(calculate_total_price(input_map))
