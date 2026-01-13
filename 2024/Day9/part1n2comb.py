from Day9.part1n2comb import compact_disk

def parse_disk_map(disk_map):
    """Convert disk map string into list of files and spaces"""
    result = []
    is_file = True  # Alternates between file and space
    for char in disk_map:
        length = int(char)
        result.append((length, is_file))
        is_file = not is_file
    return result

def create_block_representation(parsed_map):
    """Create a list where each element represents one block on disk"""
    blocks = []
    file_id = 0
    
    for length, is_file in parsed_map:
        if is_file:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(['.'] * length)
    
    return blocks

def get_file_positions(blocks):
    """Get the start position and length of each file in the blocks"""
    file_positions = {}  # {file_id: (start_pos, length)}
    current_file = None
    start_pos = None
    length = 0
    
    for pos, block in enumerate(blocks):
        if block != '.':  # It's a file block
            if current_file != block:  # Start of new file
                if current_file is not None:
                    file_positions[current_file] = (start_pos, length)
                current_file = block
                start_pos = pos
                length = 1
            else:  # Continuation of current file
                length += 1
        elif current_file is not None:  # End of file
            file_positions[current_file] = (start_pos, length)
            current_file = None
            length = 0
    
    # Handle last file if it ends at the end of blocks
    if current_file is not None:
        file_positions[current_file] = (start_pos, length)
    
    return file_positions

def find_leftmost_space(blocks, required_length, min_position=0):
    """Find the leftmost contiguous free space of required length"""
    current_length = 0
    start_pos = None
    
    for pos in range(min_position, len(blocks)):
        if blocks[pos] == '.':
            if start_pos is None:
                start_pos = pos
            current_length += 1
            if current_length >= required_length:
                return start_pos
        else:
            start_pos = None
            current_length = 0
    
    return None

def compact_disk_whole_files(blocks):
    """Move whole files from right to left, starting with highest file ID"""
    result = blocks.copy()
    file_positions = get_file_positions(result)
    
    # Sort file IDs in descending order
    file_ids = sorted(file_positions.keys(), reverse=True)
    
    for file_id in file_ids:
        start_pos, length = file_positions[file_id]
        # Find leftmost space that can fit this file
        new_pos = find_leftmost_space(result, length)
        
        if new_pos is not None and new_pos < start_pos:
            # Move the file
            file_blocks = [file_id] * length
            # Clear old position
            for i in range(start_pos, start_pos + length):
                result[i] = '.'
            # Place in new position
            for i in range(new_pos, new_pos + length):
                result[i] = file_id
    
    return result

def calculate_checksum(blocks):
    """Calculate checksum by multiplying position by file ID"""
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * block
    return checksum

def solve_disk_fragmenter(disk_map, use_whole_files=False):
    """Main function to solve the puzzle"""
    # Parse the input
    parsed_map = parse_disk_map(disk_map)
    
    # Create initial block representation
    blocks = create_block_representation(parsed_map)
    
    # Compact the disk using specified method
    if use_whole_files:
        compacted_blocks = compact_disk_whole_files(blocks)
    else:
        compacted_blocks = compact_disk(blocks)
    
    # Calculate and return checksum
    return calculate_checksum(compacted_blocks)

# Read input from file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

# Main execution
if __name__ == "__main__":
    # Read the input file
    input_data = read_input_file('input.txt') #You Input File
    
    # Solve Part 1
    result_part1 = solve_disk_fragmenter(input_data, use_whole_files=False)
    print(f"Part 1 - Filesystem checksum: {result_part1}")
    
    # Solve Part 2
    result_part2 = solve_disk_fragmenter(input_data, use_whole_files=True)
    print(f"Part 2 - Filesystem checksum: {result_part2}")
