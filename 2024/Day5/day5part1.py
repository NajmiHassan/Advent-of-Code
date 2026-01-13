def parse_input(input_data):
    # Split input into rules and updates
    rules_section, updates_section = input_data.strip().split("\n\n")
    
    # Parse ordering rules
    rules = []
    for rule in rules_section.splitlines():
        x, y = map(int, rule.split('|'))
        rules.append((x, y))
    
    # Parse updates
    updates = []
    for update in updates_section.splitlines():
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def is_update_valid(update, rules):
    # Create a dictionary to store the index of each page in the update
    page_index = {page: i for i, page in enumerate(update)}
    
    # Check all rules that apply to this update
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] >= page_index[y]:
                return False  # Rule is violated
    return True

def find_middle_page(update):
    # Find the middle page number
    n = len(update)
    return update[n // 2]

def solve(input_data):
    # Parse input data
    rules, updates = parse_input(input_data)
    
    # Process each update and check if it's valid
    valid_updates = []
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
    
    # Find middle pages of valid updates and calculate their sum
    middle_pages_sum = sum(find_middle_page(update) for update in valid_updates)
    
    return middle_pages_sum

# Example input (replace this with your actual puzzle input)
input_data = """You Puzzle Input"""

# Solve the problem and print the result
result = solve(input_data)
print("Sum of middle pages:", result)
