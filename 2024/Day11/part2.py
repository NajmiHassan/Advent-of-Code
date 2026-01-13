from collections import Counter

def read_input_file(file_path):
    """Reads the input file and parses the initial arrangement of stones."""
    with open(file_path, 'r') as file:
        stones = list(map(int, file.readline().strip().split()))
    return stones

def simulate_blink_optimized(stones, blinks):
    """
    Optimized simulation using a Counter to track stone counts instead of processing each stone individually.
    """
    stone_counts = Counter(stones)  # Count occurrences of each stone

    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                # Rule 1: Replace 0 with 1
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split even-digit numbers into two stones
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                # Rule 3: Multiply odd-digit numbers by 2024
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    return sum(stone_counts.values())


if __name__ == "__main__":
    file_path = 'Your Puzzle Input File Path'  # Replace with the actual input file path
    initial_stones = read_input_file(file_path)
    blinks = 75
    result = simulate_blink_optimized(initial_stones, blinks)
    print(f"Number of stones after {blinks} blinks: {result}")
