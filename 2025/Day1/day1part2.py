def main():
    # Absolute path to your puzzle input file
    input_path = "/content/sample_data/input.txt"

    try:
        with open(input_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Input file not found at: {input_path}")
        return

    MOD = 100           # dial numbers: 0-99
    position = 50       # starting position
    zero_clicks = 0     # count of times dial points at 0 on any click

    for rotation in lines:
        direction = rotation[0]          # 'L' or 'R'
        distance = int(rotation[1:])     # number after L/R

        if direction == 'R':
            # Solve (position + i) ≡ 0 (mod 100)  ->  i ≡ -position (mod 100)
            first_hit = (100 - position) % 100
            if first_hit == 0:
                first_hit = 100  # next time around the circle
        elif direction == 'L':
            # Solve (position - i) ≡ 0 (mod 100)  ->  i ≡ position (mod 100)
            first_hit = position % 100
            if first_hit == 0:
                first_hit = 100
        else:
            # Ignore invalid lines just in case
            continue

        # Count hits if the first one is within the distance,
        # then every additional hit is 100 clicks later.
        if first_hit <= distance:
            zero_clicks += 1 + (distance - first_hit) // 100

        # Update the position after the whole rotation
        if direction == 'R':
            position = (position + distance) % MOD
        else:  # 'L'
            position = (position - distance) % MOD

    # Print the Part Two answer (password with method 0x434C49434B)
    print(zero_clicks)


if __name__ == "__main__":
    main()