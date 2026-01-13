def parse_ranges(line: str):
    """
    Parse a single line of comma-separated ranges like '11-22,95-115,...'
    into a list of (start, end) integer tuples.
    """
    ranges = []
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        start = int(start_str)
        end = int(end_str)
        if start > end:
            start, end = end, start  # just in case
        ranges.append((start, end))
    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping or adjacent ranges.
    Input: list of (start, end)
    Output: list of disjoint, merged (start, end) sorted by start
    """
    if not ranges:
        return []

    ranges.sort()
    merged = [list(ranges[0])]

    for s, e in ranges[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e + 1:  # overlap or directly adjacent
            merged[-1][1] = max(last_e, e)
        else:
            merged.append([s, e])

    return [(s, e) for s, e in merged]


def generate_repeated_double_numbers(min_val: int, max_val: int):
    """
    Generate all numbers between min_val and max_val (inclusive)
    that are composed of some sequence of digits repeated twice.
    e.g., 11 (1+1), 6464 (64+64), 123123 (123+123).
    """
    if max_val < 0:
        return  # no positive IDs

    # IDs have no leading zeros, so we only consider positive lengths.
    max_digits = len(str(max_val))
    if max_digits < 2:
        return  # can't have repeated-twice with fewer than 2 digits

    # We will generate candidates by choosing the "half" pattern,
    # then repeating it twice, e.g. base='123' -> candidate='123123'.
    for total_len in range(2, max_digits + 1, 2):  # only even lengths
        half_len = total_len // 2
        start_base = 10 ** (half_len - 1)  # first digit cannot be 0
        end_base = 10 ** half_len

        for base in range(start_base, end_base):
            s = str(base)
            candidate = int(s + s)
            if candidate > max_val:
                # Since bases increase, further candidates will also be too big
                break
            if candidate >= min_val:
                yield candidate


def sum_invalid_ids(ranges):
    """
    Given a list of (start, end) ranges, compute the sum of all invalid IDs
    (numbers made of some sequence of digits repeated twice) appearing
    in the ranges (counting each ID once, even if in overlapping ranges).
    """
    if not ranges:
        return 0

    merged = merge_ranges(ranges)
    global_min = merged[0][0]
    global_max = merged[-1][1]

    total_sum = 0
    interval_index = 0
    num_intervals = len(merged)

    for candidate in sorted(generate_repeated_double_numbers(global_min, global_max)):
        # Advance the interval pointer so that merged[interval_index] might contain candidate
        while interval_index < num_intervals and candidate > merged[interval_index][1]:
            interval_index += 1
        if interval_index == num_intervals:
            break  # no more intervals to check
        start, end = merged[interval_index]
        if start <= candidate <= end:
            total_sum += candidate

    return total_sum


def main():
    # Read from the specified input file path
    input_path = "/content/sample_data/input.txt"

    with open(input_path, "r") as f:
        data = f.read().strip()

    if not data:
        print(0)
        return

    # In the puzzle, ranges are on a single long line, but we’ll be robust
    # and just use the first non-empty line if multiple lines exist.
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    line = lines[0]

    ranges = parse_ranges(line)
    result = sum_invalid_ids(ranges)
    print(result)


if __name__ == "__main__":
    main()