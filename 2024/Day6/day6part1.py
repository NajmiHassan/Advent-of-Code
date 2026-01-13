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
    """Simulate the guard's movement and track visited positions."""
    visited_positions = set()
    x, y = start_pos
    dx, dy = start_direction
    rows, cols = len(grid), len(grid[0])
    
    while 0 <= x < cols and 0 <= y < rows:
        visited_positions.add((x, y))
        
        # Check if there's an obstacle in front
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == '#':
            # Turn right
            dx, dy = turn_right((dx, dy))
        else:
            # Move forward
            x, y = nx, ny
    
    return visited_positions


def count_visited_positions(file_path):
    """Main function to count distinct positions visited by the guard."""
    with open(file_path, 'r') as f:
        input_map = [line.strip() for line in f.readlines()]
    
    grid, start_pos, start_direction = parse_map(input_map)
    visited_positions = simulate_guard(grid, start_pos, start_direction)
    return len(visited_positions)


# Example usage with the provided input file
file_path = 'input.txt'  # Replace with the actual path to your input file
result = count_visited_positions(file_path)
print("Distinct positions visited by the guard:", result)