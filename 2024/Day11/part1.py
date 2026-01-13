def read_input_file(file_path):
    """Reads the input file and parses the initial arrangement of stones."""
    with open(file_path, 'r') as file:
        stones = list(map(int, file.readline().strip().split()))
    return stones

def simulate_blink(stones, blinks):
    """Simulates the blinking process for a given number of blinks."""
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                # Rule 1: Replace 0 with 1
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split even-digit numbers into two stones
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                # Rule 3: Multiply odd-digit numbers by 2024
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

def count_stones_after_blinks(initial_stones, blinks):
    """Counts the number of stones after a given number of blinks."""
    final_stones = simulate_blink(initial_stones, blinks)
    return len(final_stones)


if __name__ == "__main__":
    file_path = 'Your Puzzle Input File Path'  # Replace with the actual input file path
    initial_stones = read_input_file(file_path)
    blinks = 25
    result = count_stones_after_blinks(initial_stones, blinks)
    print(f"Number of stones after {blinks} blinks: {result}")
