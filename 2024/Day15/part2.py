import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

newline_idx = lines.index('\n')
tilemap = {'.': ['.','.'], '@': ['@','.'], 'O': ['[',']'], '#': ['#','#']} 
tiles = [[char for pair in (tilemap[char] for char in line.strip()) for char in pair] for line in lines[:newline_idx]]
instructions = ''.join(line.strip() for line in lines[newline_idx+1:])
grid = np.array(tiles)
robot = np.argwhere(grid == '@')[0]
movemap = { '>': [1, 0], '<': [-1, 0], 'v': [0, 1], '^': [0,-1] }
moves = [movemap[instruction] for instruction in instructions]

def get_blocks_to_move(x, y, mx, my):
    next_tile = grid[y+my, x+mx]
    if next_tile == '#':
        return (False, [])
    elif next_tile == '.':
        return (True, [])
    elif next_tile in tilemap['O']:
        if my == 0:
            if mx > 0: 
                blocks_to_move = [[y,x+mx]]
            else: 
                blocks_to_move = [[y,x+mx-1]]
            x = x + mx*2
            (can_shift, next_blocks_to_move) = get_blocks_to_move(x, y, mx, my)
            blocks_to_move.extend(next_blocks_to_move)
            return (can_shift, blocks_to_move)
        y = y+my
        if next_tile == ']':
            x = x-1
        blocks_to_move = [[y,x]]
        (can_shift_1, next_blocks_to_move_1) = get_blocks_to_move(x, y, mx, my)
        blocks_to_move.extend(next_blocks_to_move_1)
        if can_shift_1:
            (can_shift_2, next_blocks_to_move_2) = get_blocks_to_move(x+1, y, mx, my)
            blocks_to_move.extend(next_blocks_to_move_2)
        return (can_shift_1 and can_shift_2, blocks_to_move)

for mx, my in moves:
    (can_shift, blocks_to_move) = get_blocks_to_move(robot[1], robot[0], mx, my)
    if not can_shift:
        continue
    for by, bx in blocks_to_move:
        grid[by,bx] = '.' 
        grid[by,bx+1] = '.' 
    for by, bx in blocks_to_move:
        grid[by+my,bx+mx] = '[' 
        grid[by+my,bx+mx+1] = ']' 
    grid[robot[0], robot[1]] = '.'
    robot = [robot[0]+my, robot[1]+mx]
    grid[robot[0], robot[1]] = '@'

boxes = np.argwhere(grid == '[')
total = sum([100*y+x for y, x in boxes])

print("Part 2 Result:", total)