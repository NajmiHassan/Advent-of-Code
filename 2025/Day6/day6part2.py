from math import prod

def main():
    # Use the requested absolute path
    input_path = "/content/sample_data/input.txt"

    # Read all lines and strip only trailing newlines
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
    non_empty_columns = [
        any(grid[r][c] != " " for r in range(rows))
        for c in range(width)
    ]

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
        # Find operator in the bottom row within this block
        op_segment = grid[bottom_row_index][c_start:c_end + 1]
        op = None
        if "+" in op_segment:
            op = "+"
        if "*" in op_segment:
            if op is not None and op != "*":
                raise ValueError("Block has both '+' and '*', invalid input.")
            op = "*"

        if op is None:
            raise ValueError(f"No operator found in block columns {c_start}-{c_end}")

        # Cephalopod numbers: one per column, digits stacked top-to-bottom,
        # most significant at the top, least significant just above the operator row.
        numbers = []
        for c in range(c_start, c_end + 1):
            digits = []
            for r in range(bottom_row_index):  # exclude operator row
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                numbers.append(int("".join(digits)))

        if not numbers:
            raise ValueError(f"No numbers found in block columns {c_start}-{c_end}")

        # Math is read right-to-left: columns from rightmost to leftmost
        numbers = list(reversed(numbers))

        if op == "+":
            value = sum(numbers)
        else:  # op == "*"
            value = prod(numbers)

        grand_total += value

    print(grand_total)


if __name__ == "__main__":
    main()