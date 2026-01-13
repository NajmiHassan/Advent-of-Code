from sympy import symbols, Eq, solve

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

            # Parse Prize and adjust by adding 10000000000000
            if "Prize" not in prize_line or "X=" not in prize_line or "Y=" not in prize_line:
                raise ValueError(f"Invalid format for Prize line: {prize_line}")
            prize_x = int(prize_line.split('X=')[1].split(',')[0]) + 10000000000000
            prize_y = int(prize_line.split('Y=')[1]) + 10000000000000

            machines.append({'A': (a_x, a_y), 'B': (b_x, b_y), 'prize': (prize_x, prize_y)})

    except Exception as e:
        print(f"Error reading input file: {e}")
        return []

    return machines

def calculate_min_tokens(updated_machines):
    total_tokens = 0
    prizes_won = 0

    for machine in updated_machines:
        a_x, a_y = machine['A']
        b_x, b_y = machine['B']
        prize_x, prize_y = machine['prize']

        # Define symbols for the number of presses
        a_presses, b_presses = symbols('a_presses b_presses', integer=True, nonnegative=True)

        # Define equations for X and Y alignment
        eq1 = Eq(a_presses * a_x + b_presses * b_x, prize_x)
        eq2 = Eq(a_presses * a_y + b_presses * b_y, prize_y)

        # Solve the system of equations
        solution = solve((eq1, eq2), (a_presses, b_presses), dict=True)

        # Find the minimum tokens if a solution exists
        min_tokens = float('inf')
        for sol in solution:
            a_p = sol[a_presses]
            b_p = sol[b_presses]
            if a_p is not None and b_p is not None:
                tokens = a_p * 3 + b_p * 1
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
































# from sympy import symbols, Eq, solve

# # Define the original machines with their button configurations and prize locations
# machines = [
#     {'A': (94, 34), 'B': (22, 67), 'prize': (8400, 5400)},
#     {'A': (26, 66), 'B': (67, 21), 'prize': (12748, 12176)},
#     {'A': (17, 86), 'B': (84, 37), 'prize': (7870, 6450)},
#     {'A': (69, 23), 'B': (27, 71), 'prize': (18641, 10279)}
# ]

# # Update the prize coordinates by adding 10000000000000 to both X and Y positions
# updated_machines = []
# for machine in machines:
#     updated_prize_x = machine['prize'][0] + 10000000000000
#     updated_prize_y = machine['prize'][1] + 10000000000000
#     updated_machines.append({
#         'A': machine['A'],
#         'B': machine['B'],
#         'prize': (updated_prize_x, updated_prize_y)
#     })

# def calculate_min_tokens(updated_machines):
#     total_tokens = 0
#     prizes_won = 0

#     for machine in updated_machines:
#         a_x, a_y = machine['A']
#         b_x, b_y = machine['B']
#         prize_x, prize_y = machine['prize']

#         # Define symbols for the number of presses
#         a_presses, b_presses = symbols('a_presses b_presses', integer=True, nonnegative=True)

#         # Define equations for X and Y alignment
#         eq1 = Eq(a_presses * a_x + b_presses * b_x, prize_x)
#         eq2 = Eq(a_presses * a_y + b_presses * b_y, prize_y)

#         # Solve the system of equations
#         solution = solve((eq1, eq2), (a_presses, b_presses), dict=True)

#         # Find the minimum tokens if a solution exists
#         min_tokens = float('inf')
#         for sol in solution:
#             a_p = sol[a_presses]
#             b_p = sol[b_presses]
#             if a_p is not None and b_p is not None:
#                 tokens = a_p * 3 + b_p * 1
#                 if tokens < min_tokens:
#                     min_tokens = tokens

#         if min_tokens != float('inf'):
#             total_tokens += min_tokens
#             prizes_won += 1

#     return prizes_won, total_tokens

# # Calculate the result
# prizes_won, total_tokens = calculate_min_tokens(updated_machines)
# print(f"Prizes won: {prizes_won}, Total tokens: {total_tokens}")
















# # from sympy import symbols, Eq, solve

# # def read_and_update_input(file_path):
# #     try:
# #         with open(file_path, 'r') as file:
# #             lines = [line.strip() for line in file if line.strip()]  # Remove blank lines

# #         machines = []
# #         for i in range(0, len(lines), 3):
# #             a_line = lines[i].split(', ')
# #             b_line = lines[i+1].split(', ')
# #             prize_line = lines[i+2].split(', ')

# #             # Parse Button A
# #             a_x = int(a_line[0].split('+')[1])
# #             a_y = int(a_line[1].split('+')[1])

# #             # Parse Button B
# #             b_x = int(b_line[0].split('+')[1])
# #             b_y = int(b_line[1].split('+')[1])

# #             # Parse Prize and add 10000000000000 to each coordinate
# #             prize_x = int(prize_line[0].split('=')[1]) + 10000000000000
# #             prize_y = int(prize_line[1].split('=')[1]) + 10000000000000

# #             machines.append({'A': (a_x, a_y), 'B': (b_x, b_y), 'prize': (prize_x, prize_y)})

# #         return machines
# #     except FileNotFoundError:
# #         print("The specified input file was not found.")
# #         return []

# # def calculate_min_tokens(updated_machines):
# #     total_tokens = 0
# #     prizes_won = 0

# #     for machine in updated_machines:
# #         a_x, a_y = machine['A']
# #         b_x, b_y = machine['B']
# #         prize_x, prize_y = machine['prize']

# #         # Define symbols for the number of presses
# #         a_presses, b_presses = symbols('a_presses b_presses', integer=True, nonnegative=True)

# #         # Define equations for X and Y alignment
# #         eq1 = Eq(a_presses * a_x + b_presses * b_x, prize_x)
# #         eq2 = Eq(a_presses * a_y + b_presses * b_y, prize_y)

# #         # Solve the system of equations
# #         solution = solve((eq1, eq2), (a_presses, b_presses), dict=True)

# #         # Find the minimum tokens if a solution exists
# #         min_tokens = float('inf')
# #         for sol in solution:
# #             a_p = sol[a_presses]
# #             b_p = sol[b_presses]
# #             if a_p is not None and b_p is not None and isinstance(a_p, int) and isinstance(b_p, int):
# #                 tokens = a_p * 3 + b_p * 1
# #                 if tokens < min_tokens:
# #                     min_tokens = tokens

# #         if min_tokens != float('inf'):
# #             total_tokens += min_tokens
# #             prizes_won += 1

# #     return prizes_won, total_tokens

# # # Example usage
# # file_path = 'C:/Users/786/Advent of Code/Day13/input.txt'  # Replace with your actual input file path
# # updated_machines = read_and_update_input(file_path)
# # if updated_machines:
# #     prizes_won, total_tokens = calculate_min_tokens(updated_machines)
# #     print(f"Prizes won: {prizes_won}, Total tokens: {total_tokens}")
# # else:
# #     print("No valid machines found.")
