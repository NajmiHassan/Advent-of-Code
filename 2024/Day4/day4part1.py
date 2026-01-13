fileContents = open("puzzle.txt")
arr = fileContents.read().split("\n")

word_search: dict[tuple[int, int], str] = dict()

for row, line in enumerate(arr):
    for col, char in enumerate(line):
        word_search[(row, col)] = char


forward = [(0, 0), (0, 1), (0, 2), (0, 3)]
down = [(0, 0), (1, 0), (2, 0), (3, 0)]
backward = [(0, 0), (0, -1), (0, -2), (0, -3)]
up = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
diagonal_right_down = [(0, 0), (1, 1), (2, 2), (3, 3)]
diagonal_left_up = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
diagonal_left_down = [(0, 0), (1, -1), (2, -2), (3, -3)]
diagonal_right_up = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]

dirs = [
    forward,
    down,
    backward,
    up,
    diagonal_right_down,
    diagonal_left_up,
    diagonal_left_down,
    diagonal_right_up,
]


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def get_word(pos: tuple[int, int], dir: list[tuple[int, int]]):
    word = ""
    for character in dir:
        coord = add_pts(character, pos)
        if coord not in word_search:
            return ""
        word += word_search[coord]
    return word


total = 0
for p in word_search:
    for dir in dirs:
        if get_word(p, dir) == "XMAS":
            total += 1
print(total)
