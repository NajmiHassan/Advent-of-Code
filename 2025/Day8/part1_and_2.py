import math
from itertools import combinations
from collections import Counter

# Union-Find (Disjoint Set Union) data structure
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same circuit
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.num_components -= 1
        return True

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def solve_part1(filename):
    # Parse input
    with open(filename) as f:
        points = []
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(','))
                points.append((x, y, z))

    n = len(points)
    print(f"Number of junction boxes: {n}")

    # Calculate all pairwise distances
    distances = []
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(points[i], points[j])
        distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    print(f"Total pairs: {len(distances)}")
    print(f"Shortest distance: {distances[0][0]:.2f}")

    # Connect the 1000 closest pairs using Union-Find
    uf = UnionFind(n)
    connections_made = 0

    for dist, i, j in distances:
        if connections_made >= 1000:
            break
        uf.union(i, j)  # Connect regardless of whether already in same circuit
        connections_made += 1

    # Count circuit sizes
    circuit_sizes = Counter(uf.find(i) for i in range(n))

    # Get the three largest circuits
    largest = sorted(circuit_sizes.values(), reverse=True)[:3]

    print(f"Number of circuits: {len(circuit_sizes)}")
    print(f"Three largest circuits: {largest}")

    result = largest[0] * largest[1] * largest[2]
    print(f"Part 1 Answer: {result}")

    return result

def solve_part2(filename):
    # Parse input
    with open(filename) as f:
        points = []
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(','))
                points.append((x, y, z))

    n = len(points)

    # Calculate all pairwise distances
    distances = []
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(points[i], points[j])
        distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Connect pairs until all are in one circuit
    uf = UnionFind(n)
    last_i, last_j = None, None

    for dist, i, j in distances:
        # Only count connections that actually merge two different circuits
        if uf.union(i, j):
            last_i, last_j = i, j
            if uf.num_components == 1:
                break

    # Get the X coordinates of the last two junction boxes connected
    x1 = points[last_i][0]
    x2 = points[last_j][0]

    print(f"Last connection: {points[last_i]} and {points[last_j]}")
    print(f"X coordinates: {x1} and {x2}")

    result = x1 * x2
    print(f"Part 2 Answer: {result}")

    return result

if __name__ == "__main__":
    solve_part1("/content/sample_data/input.txt")
    print()
    solve_part2("/content/sample_data/input.txt")