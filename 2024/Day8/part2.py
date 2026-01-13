def count_unique_antinode_locations_part_two(antenna_map):
    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antinodes = set()

    # Iterate over all pairs of antennas
    for r1 in range(rows):
        for c1 in range(cols):
            if antenna_map[r1][c1] != '.':  # Check if it's an antenna
                for r2 in range(rows):
                    for c2 in range(cols):
                        if (r1, c1) != (r2, c2) and antenna_map[r1][c1] == antenna_map[r2][c2]:
                            # Calculate all positions along the line between antennas
                            dr = r2 - r1
                            dc = c2 - c1
                            gcd = abs(dr) if dc == 0 else abs(dr) if dr == 0 else abs(__import__('math').gcd(dr, dc))
                            step_r, step_c = dr // gcd, dc // gcd

                            # Add all positions along this line to antinodes
                            current_r, current_c = r1, c1
                            while 0 <= current_r < rows and 0 <= current_c < cols:
                                antinodes.add((current_r, current_c))
                                current_r += step_r
                                current_c += step_c

    return len(antinodes)

# Read input from file
with open("Path to your input file", "r") as file:
    antenna_map = [line.strip() for line in file]

# Calculate the result for Part Two
result = count_unique_antinode_locations_part_two(antenna_map)
print(result)