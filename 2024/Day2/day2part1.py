def is_safe_report(report):
    # Check if the report is strictly increasing or decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    # Check if differences are within the allowed range
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return (increasing or decreasing) and valid_differences

def count_safe_reports(data):
    safe_count = 0
    for line in data.strip().split('\n'):
        report = list(map(int, line.split()))
        if is_safe_report(report):
            safe_count += 1
    return safe_count

# Example usage with provided data
puzzle_input = """
3 6 7 9 11 8
21 24 25 26 29 30 32 32
29 32 33 34 35 37 38 42
54 55 57 58 60 61 63 70
59 61 60 63 65 68 71
"list continues"
""" # Add the rest of your puzzle input here

safe_reports = count_safe_reports(puzzle_input)
print(safe_reports)