import sys
import numpy as np
from heapq import *

def turn_right(card_dir):
    if card_dir == 'N': return 'E'
    if card_dir == 'E': return 'S'
    if card_dir == 'S': return 'W'
    if card_dir == 'W': return 'N'

def turn_left(card_dir):
    if card_dir == 'N': return 'W'
    if card_dir == 'W': return 'S'
    if card_dir == 'S': return 'E'
    if card_dir == 'E': return 'N'

with open('input.txt') as f:
    lines = f.readlines()

tiles = [[char for char in line.strip()] for line in lines]
grid = np.array(tiles)
start = np.argwhere(grid == 'S')[0]
end = np.argwhere(grid == 'E')[0]
dir_dict = { 'E': [0,1], 'S': [1,0], 'W': [0,-1], 'N': [-1,0]}
q = [(0, start, 'E')]
visited = {}
min_cost = sys.maxsize

while q:
    (cost, [y, x], card_dir) = heappop(q)
    if ((y, x), card_dir) in visited and visited[((y, x), card_dir)] < cost:
        continue
    visited[((y, x), card_dir)] = cost

    vector = dir_dict[card_dir]
    next_symbol = grid[y+vector[0], x+vector[1]]
    if next_symbol == '.':
        heappush(q, (cost+1, [y+vector[0], x+vector[1]], card_dir))
    elif next_symbol == 'E':
        min_cost = min(min_cost, cost+1)
        continue

    left_dir = turn_left(card_dir)
    left_vector = dir_dict[left_dir]
    if grid[y+left_vector[0], x+left_vector[1]] == '.':
        heappush(q, (cost+1000, [y, x], left_dir))

    right_dir = turn_right(card_dir)
    right_vector = dir_dict[right_dir]
    if grid[y+right_vector[0], x+right_vector[1]] == '.':
        heappush(q, (cost+1000, [y, x], turn_right(card_dir)))    

print("Part 1 Result:", min_cost)