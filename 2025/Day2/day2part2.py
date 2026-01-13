from bisect import bisect_right

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
            start, end = end, start  # normalize just in case
        ranges.append((start, end))
    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping or adjacent ranges.
    Input: list of (start, end)
    Output: list of disjoint, merged (start, end) sorted by start.
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


def sum_invalid_ids_repeated_any(ranges):
    """
    Given a list of (start, end) ranges, compute the sum of all invalid IDs
    (numbers made of some sequence of digits repeated at least twice) appearing
    in the ranges (counting each ID once, even if in overlapping ranges).
    """
    if not ranges:
        return 0

    merged = merge_ranges(ranges)
    global_min = merged[0][0]
    global_max = merged[-1][1]

    # Precompute starts for fast membership checks via binary search
    starts = [s for (s, _) in merged]

    def in_any_range(x: int) -> bool:
        """Check if x lies in any of the merged ranges using binary search."""
        idx = bisect_right(starts, x) - 1
        if idx < 0:
            return False
        s, e = merged[idx]
        return s <= x <= e

    seen = set()
    total_sum = 0

    max_digits = len(str(global_max))
    if max_digits < 2:
        return 0  # can't form repeated patterns with fewer than 2 digits

    # Generate all numbers whose decimal representation is some pattern
    # of digits repeated k times, where k >= 2.
    for total_len in range(2, max_digits + 1):
        # total_len is the total number of digits of the final ID.
        # base_len is the length of the repeating pattern.
        for base_len in range(1, total_len):
            if total_len % base_len != 0:
                continue
            k = total_len // base_len
            if k < 2:  # must be repeated at least twice
                continue

            start_base = 10 ** (base_len - 1)  # no leading zeros
            end_base = 10 ** base_len

            for base in range(start_base, end_base):
                s = str(base)
                candidate = int(s * k)  # repeat pattern k times

                if candidate > global_max:
                    # For fixed total_len, base_len, k, increasing base
                    # makes candidate increase; we can stop this base loop.
                    break
                if candidate < global_min:
                    continue

                if candidate in seen:
                    continue

                if in_any_range(candidate):
                    seen.add(candidate)
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

    # Ranges are on a single long line in the puzzle input.
    # We'll just take the first non-empty line to be safe.
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    line = lines[0]

    ranges = parse_ranges(line)
    result = sum_invalid_ids_repeated_any(ranges)
    print(result)


if __name__ == "__main__":
    main()