def parse_map(input_map):
    """Parse the input map into a grid and find the guard's starting position and direction."""
    grid = []
    guard_pos = None
    direction = None
    direction_map = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    
    for y, line in enumerate(input_map):
        row = []
        for x, char in enumerate(line):
            if char in direction_map:
                guard_pos = (x, y)
                direction = direction_map[char]
                row.append('.')
            else:
                row.append(char)
        grid.append(row)
    
    return grid, guard_pos, direction


def turn_right(direction):
    """Turn the guard 90 degrees to the right."""
    dx, dy = direction
    return (-dy, dx)


def simulate_guard(grid, start_pos, start_direction):
    """Simulate the guard's movement and track visited positions with directions."""
    visited_positions = set()
    x, y = start_pos
    dx, dy = start_direction
    rows, cols = len(grid), len(grid[0])
    
    while 0 <= x < cols and 0 <= y < rows:
        # Track position with direction to detect loops
        state = (x, y, dx, dy)
        if state in visited_positions:
            return True  # Loop detected
        visited_positions.add(state)
        
        # Check if there's an obstacle in front
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == '#':
            # Turn right
            dx, dy = turn_right((dx, dy))
        else:
            # Move forward
            x, y = nx, ny
    
    return False  # No loop detected


def find_obstruction_positions(file_path):
    """Find all positions where an obstruction can cause a loop."""
    with open(file_path, 'r') as f:
        input_map = [line.strip() for line in f.readlines()]
    
    grid, start_pos, start_direction = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    
    valid_positions = set()
    
    for y in range(rows):
        for x in range(cols):
            # Skip non-empty cells and the guard's starting position
            if grid[y][x] != '.' or (x, y) == start_pos:
                continue
            
            # Place a hypothetical obstruction and test for a loop
            grid[y][x] = '#'
            if simulate_guard(grid, start_pos, start_direction):
                valid_positions.add((x, y))
            grid[y][x] = '.'  # Remove obstruction
    
    return len(valid_positions)


# Example usage with the provided input file
file_path = 'input.txt' # Replace with the actual path to your input file
result = find_obstruction_positions(file_path)
print("Number of positions where an obstruction causes a loop:", result)