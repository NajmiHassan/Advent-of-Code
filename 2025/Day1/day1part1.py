def main():
    # Absolute path to your puzzle input file
    input_path = "/content/sample_data/input.txt"

    try:
        with open(input_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Input file not found at: {input_path}")
        return

    # Dial settings
    dial = 50        # starting position
    MOD = 100        # dial has numbers 0-99
    count_zero = 0   # how many times dial lands on 0

    for rotation in lines:
        direction = rotation[0]          # 'L' or 'R'
        distance = int(rotation[1:])     # number after L/R

        if direction == 'L':
            dial = (dial - distance) % MOD
        elif direction == 'R':
            dial = (dial + distance) % MOD
        else:
            # In case of invalid line (not expected in valid input)
            continue

        if dial == 0:
            count_zero += 1

    # Print the final answer (password) to the terminal
    print(count_zero)


if __name__ == "__main__":
    main()