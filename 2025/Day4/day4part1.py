def count_accessible_rolls(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])

    # 8-directional neighbors (Moore neighborhood)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbor_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_rolls += 1

            if neighbor_rolls < 4:
                accessible += 1

    return accessible


def main():
    # Read from the specified input file path
    file_path = "/content/sample_data/input.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        # Strip newline characters but keep full row width
        grid = [line.rstrip("\n") for line in f if line.strip() != ""]

    result = count_accessible_rolls(grid)
    print(result)


if __name__ == "__main__":
    main()