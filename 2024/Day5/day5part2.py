from collections import defaultdict, deque

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

def reorder_update(update, rules):
    # Build a graph and calculate in-degrees based on the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Only consider pages present in the current update
    pages_in_update = set(update)
    
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform topological sort using Kahn's algorithm
    queue = deque([node for node in pages_in_update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def solve(input_data):
    # Parse input data
    rules, updates = parse_input(input_data)
    
    # Process each update to identify invalid ones and reorder them
    reordered_updates = []
    
    for update in updates:
        if not is_update_valid(update, rules):
            reordered_updates.append(reorder_update(update, rules))
    
    # Find middle pages of reordered updates and calculate their sum
    middle_pages_sum = sum(find_middle_page(update) for update in reordered_updates)
    
    return middle_pages_sum

# Example input (replace this with your actual puzzle input)
input_data = """You Puzzle Input""" 

# Solve the problem and print the result for Part Two
result = solve(input_data)
print("Sum of middle pages after reordering:", result)
