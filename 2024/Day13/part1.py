from itertools import product

def read_input_file(file_path):
    machines = []
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]  # Remove blank lines

        # Ensure lines are grouped in sets of three
        if len(lines) % 3 != 0:
            raise ValueError("Input file format is incorrect. Each machine should have exactly 3 lines.")

        for i in range(0, len(lines), 3):
            a_line = lines[i]
            b_line = lines[i + 1]
            prize_line = lines[i + 2]

            # Parse Button A
            if "Button A" not in a_line or "X+" not in a_line or "Y+" not in a_line:
                raise ValueError(f"Invalid format for Button A line: {a_line}")
            a_x = int(a_line.split('X+')[1].split(',')[0])
            a_y = int(a_line.split('Y+')[1])

            # Parse Button B
            if "Button B" not in b_line or "X+" not in b_line or "Y+" not in b_line:
                raise ValueError(f"Invalid format for Button B line: {b_line}")
            b_x = int(b_line.split('X+')[1].split(',')[0])
            b_y = int(b_line.split('Y+')[1])

            # Parse Prize
            if "Prize" not in prize_line or "X=" not in prize_line or "Y=" not in prize_line:
                raise ValueError(f"Invalid format for Prize line: {prize_line}")
            prize_x = int(prize_line.split('X=')[1].split(',')[0])
            prize_y = int(prize_line.split('Y=')[1])

            machines.append({'A': (a_x, a_y), 'B': (b_x, b_y), 'prize': (prize_x, prize_y)})

    except Exception as e:
        print(f"Error reading input file: {e}")
        return []

    return machines

def calculate_min_tokens(machines):
    max_presses = 100
    total_tokens = 0
    prizes_won = 0

    for machine in machines:
        a_x, a_y = machine['A']
        b_x, b_y = machine['B']
        prize_x, prize_y = machine['prize']
        min_tokens = float('inf')

        # Try all combinations of A and B presses
        for a_presses, b_presses in product(range(max_presses + 1), repeat=2):
            if (a_presses * a_x + b_presses * b_x == prize_x and
                a_presses * a_y + b_presses * b_y == prize_y):
                tokens = a_presses * 3 + b_presses * 1
                if tokens < min_tokens:
                    min_tokens = tokens

        if min_tokens != float('inf'):
            total_tokens += min_tokens
            prizes_won += 1

    return prizes_won, total_tokens

# Example usage
file_path = 'input.txt'  # Replace with your actual input file path
machines = read_input_file(file_path)
if machines:
    prizes_won, total_tokens = calculate_min_tokens(machines)
    print(f"Prizes won: {prizes_won}, Total tokens: {total_tokens}")
else:
    print("No valid machines found.")
