def read_input(file_path: str):
    
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f]

    # Split into ranges and IDs using the blank line
    try:
        blank_index = lines.index("")
    except ValueError:
        # If no blank line is found, treat all lines as ranges (fallback)
        blank_index = len(lines)

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1 :]

    ranges = []
    for line in range_lines:
        if not line:
            continue
        parts = line.split("-")
        if len(parts) != 2:
            continue  # or raise an error if input must be strict
        start, end = map(int, parts)
        if start > end:
            start, end = end, start  # normalize if reversed
        ranges.append((start, end))

    ids = [int(x) for x in id_lines if x]

    return ranges, ids


def merge_ranges(ranges):

    if not ranges:
        return []

    ranges.sort()  # sort by start, then end
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlapping or directly adjacent
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    # convert back to tuples for immutability
    return [tuple(r) for r in merged]


def is_fresh(ingredient_id: int, merged_ranges) -> bool:
    
    for start, end in merged_ranges:
        if ingredient_id < start:
            # Since ranges are sorted by start, no later range can contain it
            return False
        if start <= ingredient_id <= end:
            return True
    return False


def main():
    # Use the user-specified input path
    file_path = "/content/sample_data/input.txt"

    ranges, ids = read_input(file_path)
    merged_ranges = merge_ranges(ranges)

    fresh_count = sum(1 for ingredient_id in ids if is_fresh(ingredient_id, merged_ranges))

    # Print the result to the terminal
    print(fresh_count)


if __name__ == "__main__":
    main()