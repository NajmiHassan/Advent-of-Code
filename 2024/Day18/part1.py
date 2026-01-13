from collections import deque 

def dijkstra(data):
    open_set = deque([(0, complex(0, 0))])
    closed_set = set([complex(0, 0)])

    while open_set:
        score, target = open_set.popleft()

        if target == complex(70, 70):
            return score

        for d in [1j, -1j, 1, -1]:
            if target + d not in closed_set and target + d in data and data[target + d] != '#':
                open_set.append((score + 1, target + d))
                closed_set.add(target + d)

with open('input.txt') as f:
    data = f.read().splitlines()[:1024]
    byte = [ complex(int(x), int(y)) for l in data for x, y in [l.split(',')]]
    data = { complex(x, y): '#' if complex(x, y) in byte else '.' for y in range(71) for x in range(71) }

    print(dijkstra(data))