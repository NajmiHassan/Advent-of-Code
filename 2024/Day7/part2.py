from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate an expression given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            # Concatenate numbers as strings and convert back to integer
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_produce_target(target, numbers):
    """Check if any combination of +, *, and || can produce the target."""
    operator_combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)
    for ops in operator_combinations:
        if evaluate_expression(numbers, ops) == target:
            return True
    return False

def calculate_total_calibration(input_data):
    """Calculate the total calibration result."""
    total = 0
    for line in input_data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        
        if can_produce_target(target, numbers):
            total += target
    return total

# Read input data from file
with open("Path to your input file", "r") as file:
    input_data = file.read().strip().split("\n")

# Calculate and print the total calibration result
total_calibration_result = calculate_total_calibration(input_data)
print("Total Calibration Result:", total_calibration_result)