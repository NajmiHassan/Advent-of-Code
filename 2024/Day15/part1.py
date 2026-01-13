import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

newline_idx = lines.index('\n')
tiles = [[char for char in line.strip()] for line in lines[:newline_idx]]
instructions = ''.join(line.strip() for line in lines[newline_idx+1:])
grid = np.array(tiles)
robot = np.argwhere(grid == '@')[0]
movemap = { '>': [1, 0], '<': [-1, 0], 'v': [0, 1], '^': [0,-1] }
moves = [movemap[instruction] for instruction in instructions]

def in_grid(x,y): return 0 <= x <= len(grid[0])-1 and 0 <= y <= len(grid)-1

for mx, my in moves:
    can_shift = True
    shift_len = 1
    while can_shift and in_grid(robot[1]+mx*shift_len, robot[0]+my*shift_len):
        next_tile = grid[robot[0]+my*shift_len, robot[1]+mx*shift_len]
        if next_tile == '#':
            can_shift = False
        elif next_tile == 'O':
            shift_len += 1
        elif next_tile == '.':
            break
    if can_shift:
        previous_tile = '.'
        for i in range(shift_len+1):
            this_tile = grid[robot[0]+my*i, robot[1]+mx*i]
            grid[robot[0]+my*i, robot[1]+mx*i] = previous_tile
            previous_tile = this_tile
        robot = [robot[0]+my, robot[1]+mx]

boxes = np.argwhere(grid == 'O')
total = sum([100*y+x for y, x in boxes])

print("Part 1 Result:", total)