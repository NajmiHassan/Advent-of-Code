def max_two_digit_from_bank(bank: str) -> int:
    """
    Given a string of digits (a battery bank), find the maximum 2-digit number
    that can be formed by choosing two digits in order (i < j).
    """
    bank = bank.strip()
    if len(bank) < 2:
        # Not expected per problem statement, but safe guard
        return 0

    digits = [int(ch) for ch in bank]

    # Initialize with the first digit as the best "first battery" so far
    max_first = digits[0]
    max_two_digit = -1

    # For each possible second position, combine with the best first digit seen so far
    for j in range(1, len(digits)):
        second = digits[j]
        candidate = 10 * max_first + second
        if candidate > max_two_digit:
            max_two_digit = candidate

        # Update the best possible first digit for future positions
        if second > max_first:
            max_first = second

    return max_two_digit


def main():
    # Use the full path as requested
    file_path = "/content/sample_data/input.txt"

    total_joltage = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines just in case
            total_joltage += max_two_digit_from_bank(line)

    print(total_joltage)


if __name__ == "__main__":
    main()