def find(x, parents):
    return find(parents[x], parents) if parents[x] != x else x

def union(x, y, parents):
    parents[find(y, parents)] = find(x, parents)

def add_parent(x, parents):
    parents[x] = x
    for d in [1j, -1j, 1, -1]:
        if x + d in parents:
            union(x, x + d, parents)

def traverse(data):
    parents = {}
    for k, v in data.items():
        if v == '.' and k not in parents:
            add_parent(k, parents)
    return parents

with open('input.txt') as f:
    data = f.read().splitlines()
    byte = [ complex(int(x), int(y)) for l in data for x, y in [l.split(',')]]
    data = { complex(x, y): '#' if complex(x, y) in byte else '.' for y in range(71) for x in range(71) }

    parents = traverse(data)
    for b in reversed(byte):
        data[b] = '.'
        add_parent(b, parents)
        if find(complex(0, 0), parents) == find(complex(70, 70), parents):
            print(b)
            break