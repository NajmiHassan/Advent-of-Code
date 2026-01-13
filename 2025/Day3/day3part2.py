def max_joltage_from_bank(bank: str, k: int = 12) -> int:
    """
    Given a string of digits `bank`, choose exactly k digits in order
    (a subsequence) to form the largest possible k-digit number.
    Returns that number as an int.
    """
    bank = bank.strip()
    if len(bank) < k:
        # Not expected per problem statement, but safe guard
        return 0

    n = len(bank)
    remove = n - k  # how many digits we are allowed to discard
    stack = []

    for ch in bank:
        # ch is a digit character
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # If we didn't remove enough, trim from the end
    if len(stack) > k:
        stack = stack[:k]

    return int("".join(stack))


def main():
    file_path = "/content/sample_data/input.txt"

    total_joltage = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            total_joltage += max_joltage_from_bank(line, k=12)

    print(total_joltage)


if __name__ == "__main__":
    main()