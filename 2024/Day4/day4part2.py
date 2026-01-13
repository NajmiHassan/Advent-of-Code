fileContents = open("puzzle.txt")
arr = fileContents.read().split("\n")

word_search: dict[tuple[int, int], str] = dict()

for row, line in enumerate(arr):
    for col, char in enumerate(line):
        word_search[(row, col)] = char

words = ["ASMSM", "AMSMS", "AMSSM", "ASMMS"]

x_shape = [(0, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]


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
    if get_word(p, x_shape) in words:
        total += 1
print(total)
