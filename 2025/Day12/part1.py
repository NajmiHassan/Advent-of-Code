import re

def solve_christmas_tree_farm():
    with open('/content/input.txt', 'r') as f:
        content = f.read()

    content_clean = re.sub(r"'", ' ', content)

    shapes = {}
    shape_area = {}

    shape_matches = re.findall(r'(\d+):\s*\n((?:[.#]+\s*\n)+)', content_clean)

    for shape_id, shape_grid in shape_matches:
        area = shape_grid.count('#')
        shape_area[int(shape_id)] = area

    expected_areas = {0:7, 1:7, 2:7, 3:6, 4:5, 5:7}
    for i in range(6):
        if i not in shape_area:
            shape_area[i] = expected_areas[i]

    region_pattern = re.compile(r'(\d+)x(\d+):')

    matches = list(region_pattern.finditer(content_clean))

    valid_regions = 0

    for i, match in enumerate(matches):
        width = int(match.group(1))
        height = int(match.group(2))
        region_area = width * height

        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(content_clean)

        segment = content_clean[start_idx:end_idx]

        
        numbers = [int(n) for n in re.findall(r'\d+', segment)]

        if len(numbers) >= 6:
            counts = numbers[:6]

            total_present_area = 0
            for shape_idx, count in enumerate(counts):
                total_present_area += count * shape_area.get(shape_idx, 0)

            if total_present_area <= region_area:
                valid_regions += 1
            else:
                pass
        else:
            print(f"Warning: Could not find 6 counts for region {match.group(0)}")

    return valid_regions

print(solve_christmas_tree_farm())