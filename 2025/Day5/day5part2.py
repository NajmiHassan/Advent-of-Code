def read_ranges(file_path: str):
   
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f]

    # Find blank line that separates ranges and available IDs
    try:
        blank_index = lines.index("")
    except ValueError:
        # If there is no blank line, treat all lines as ranges
        blank_index = len(lines)

    range_lines = lines[:blank_index]

    ranges = []
    for line in range_lines:
        if not line:
            continue
        parts = line.split("-")
        if len(parts) != 2:
            continue  # skip malformed lines if any
        start, end = map(int, parts)
        if start > end:
            start, end = end, start  # normalize if reversed
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    
    if not ranges:
        return []

    # Sort by start, then end
    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlapping or directly adjacent
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return [tuple(r) for r in merged]


def count_fresh_ids(merged_ranges):
    
    total = 0
    for start, end in merged_ranges:
        total += (end - start + 1)
    return total


def main():
    # Use your specific input path
    file_path = "/content/sample_data/input.txt"

    ranges = read_ranges(file_path)
    merged_ranges = merge_ranges(ranges)
    result = count_fresh_ids(merged_ranges)

    # Print the result to the terminal
    print(result)


if __name__ == "__main__":
    main()