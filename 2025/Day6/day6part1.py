from math import prod

def main():
    # Use the requested absolute path
    input_path = "/content/sample_data/input.txt"

    # Read all lines and strip trailing newlines only
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        print(0)
        return

    # Pad all lines to the same width
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    rows = len(grid)
    bottom_row_index = rows - 1

    # Identify contiguous column blocks (problems),
    # separated by columns that are ALL spaces.
    non_empty_columns = [any(grid[r][c] != " " for r in range(rows))
                         for c in range(width)]

    blocks = []
    in_block = False
    start = 0

    for c in range(width):
        if non_empty_columns[c]:
            if not in_block:
                in_block = True
                start = c
        else:
            if in_block:
                blocks.append((start, c - 1))
                in_block = False
    if in_block:
        blocks.append((start, width - 1))

    grand_total = 0

    for c_start, c_end in blocks:
        # Collect numbers from all rows except the bottom (operator row)
        numbers = []
        for r in range(bottom_row_index):
            segment = grid[r][c_start:c_end + 1]
            stripped = segment.strip()
            if stripped:  # if there's something here, it should be a number
                numbers.append(int(stripped))

        # Find operator in the bottom row within this block
        op_segment = grid[bottom_row_index][c_start:c_end + 1]
        op = None
        if "+" in op_segment:
            op = "+"
        if "*" in op_segment:
            # If both somehow exist (shouldn't happen), it would be ambiguous;
            # but AoC-style input will have only one operator per problem.
            if op is not None and op != "*":
                raise ValueError("Block has both '+' and '*', invalid input.")
            op = "*"

        if op is None:
            # No operator found in this block; skip or raise error.
            # For safety, raise an error to detect bad input.
            raise ValueError(f"No operator found in block columns {c_start}-{c_end}")

        if not numbers:
            # A problem with no numbers doesn't make sense
            raise ValueError(f"No numbers found in block columns {c_start}-{c_end}")

        # Compute the result for this problem
        if op == "+":
            value = sum(numbers)
        else:  # op == "*"
            value = prod(numbers)

        grand_total += value

    print(grand_total)


if __name__ == "__main__":
    main()