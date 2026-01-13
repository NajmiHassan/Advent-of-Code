# ⚠️ Note: Part 2 answer with this code is not correct.

def solve():
    # Read the red tile coordinates
    red_tiles = []
    with open("/content/sample_data/input.txt", "r") as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            red_tiles.append((x, y))

    # Part 1: Find the largest rectangle using any two red tiles as opposite corners
    max_area = 0
    n = len(red_tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area

    print(f"Part 1: {max_area}")

    # Part 2: Rectangle must only contain red or green tiles
    # Build horizontal and vertical segments from consecutive red tiles
    h_segments = []  # (y, x_min, x_max)
    v_segments = []  # (x, y_min, y_max)

    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        if y1 == y2:  # horizontal segment
            h_segments.append((y1, min(x1, x2), max(x1, x2)))
        else:  # vertical segment (x1 == x2)
            v_segments.append((x1, min(y1, y2), max(y1, y2)))

    # For a rectangle to be valid, all four edges must not cross a polygon boundary
    # except at the corners (red tiles)

    # An edge at y from x1 to x2 is invalid if there's a vertical segment at some x
    # where x1 < x < x2 and the segment spans y
    # Similarly for vertical edges

    # Pre-process: for each y value, get all vertical segments that cross it
    from collections import defaultdict
    import bisect

    # Build sorted lists for efficient range queries
    v_by_y = defaultdict(list)  # y -> sorted list of x values of vertical segments crossing y
    for x, y_min, y_max in v_segments:
        # This vertical segment crosses all y in (y_min, y_max)
        # We need to record it for range queries
        pass

    h_by_x = defaultdict(list)  # x -> sorted list of y values of horizontal segments crossing x
    for y, x_min, x_max in h_segments:
        pass

    # More efficient: for each rectangle check, look for blocking segments
    def h_edge_blocked(x_start, x_end, y):
        """Check if horizontal edge at y from x_start to x_end is blocked by a vertical segment"""
        for x, y_min, y_max in v_segments:
            if x_start < x < x_end and y_min < y < y_max:
                return True
        return False

    def v_edge_blocked(x, y_start, y_end):
        """Check if vertical edge at x from y_start to y_end is blocked by a horizontal segment"""
        for y, x_min, x_max in h_segments:
            if y_start < y < y_end and x_min < x < x_max:
                return True
        return False

    # Check if corners are inside the polygon (excluding red tile corners)
    def point_inside(px, py):
        # Check if on a horizontal boundary
        for y, x_min, x_max in h_segments:
            if y == py and x_min <= px <= x_max:
                return True
        # Check if on a vertical boundary
        for x, y_min, y_max in v_segments:
            if x == px and y_min <= py <= y_max:
                return True

        # Ray casting - count vertical segment crossings to the right
        crossings = 0
        for x, y_min, y_max in v_segments:
            if x > px and y_min < py < y_max:
                crossings += 1
        return crossings % 2 == 1

    def rect_valid(min_x, max_x, min_y, max_y):
        # Check the two corners that are not the red tiles (we need them to be inside)
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        for cx, cy in corners:
            if not point_inside(cx, cy):
                return False

        # Check that no polygon edge cuts through the rectangle edges
        # Top edge: y = min_y
        if h_edge_blocked(min_x, max_x, min_y):
            return False
        # Bottom edge: y = max_y
        if h_edge_blocked(min_x, max_x, max_y):
            return False
        # Left edge: x = min_x
        if v_edge_blocked(min_x, min_y, max_y):
            return False
        # Right edge: x = max_x
        if v_edge_blocked(max_x, min_y, max_y):
            return False

        return True

    max_area_2 = 0
    best_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            width = max_x - min_x + 1
            height = max_y - min_y + 1
            area = width * height

            if area <= max_area_2:
                continue

            if rect_valid(min_x, max_x, min_y, max_y):
                max_area_2 = area
                best_pair = ((x1, y1), (x2, y2))

    print(f"Part 2: {max_area_2}")
    if best_pair:
        print(f"Best pair: {best_pair}")
    return max_area, max_area_2

if __name__ == "__main__":
    solve()