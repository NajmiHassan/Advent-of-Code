from collections import deque

def count_timelines(grid):
    h = len(grid)
    w = len(grid[0])

    # Find starting position S
    start_row = start_col = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    if start_row is None:
        raise ValueError("No starting point 'S' found in the grid.")

    # dp[r][c] = number of timelines where the particle is currently at (r, c),
    # moving downward.
    dp = [[0] * w for _ in range(h)]
    dp[start_row][start_col] = 1

    total_timelines = 0

    # Process row by row, from S downwards
    for r in range(start_row, h):
        for c in range(w):
            count = dp[r][c]
            if count == 0:
                continue

            nr = r + 1  # next row

            # If we go beyond the last row, all these timelines exit the manifold
            if nr >= h:
                total_timelines += count
                continue

            cell_below = grid[nr][c]

            if cell_below == '^':
                # Splitter: each of the 'count' timelines splits into:
                #   - one going left
                #   - one going right
                # No timeline continues straight down.
                left = c - 1
                right = c + 1

                if left >= 0:
                    dp[nr][left] += count
                # If left is out of bounds, that branch effectively doesn't exist.

                if right < w:
                    dp[nr][right] += count
                # If right is out of bounds, that branch also doesn't exist.
            else:
                # Empty space: all timelines just continue straight down.
                dp[nr][c] += count

    return total_timelines


def main():
    # Per your instructions, we read from this path:
    input_path = "/content/sample_data/input.txt"

    with open(input_path, "r", encoding="utf-8") as f:
        # Remove completely empty lines, keep the exact grid characters
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]

    result = count_timelines(lines)
    print(result)


if __name__ == "__main__":
    main()