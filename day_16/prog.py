
# https://adventofcode.com/2023/day/16
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# character + direction => [direction]
map = {}

map['.'] = {}
map['.'][(0, 1)] = [(0, 1)]
map['.'][(0, -1)] = [(0, -1)]
map['.'][(1, 0)] = [(1, 0)]
map['.'][(-1, 0)] = [(-1, 0)]

map['-'] = {}
map['-'][(0, 1)] = [(0, 1)]
map['-'][(0, -1)] = [(0, -1)]
map['-'][(1, 0)] = [(0, 1), (0, -1)]
map['-'][(-1, 0)] = [(0, 1), (0, -1)]

map['|'] = {}
map['|'][(0, 1)] = [(1, 0), (-1, 0)]
map['|'][(0, -1)] = [(1, 0), (-1, 0)]
map['|'][(1, 0)] = [(1, 0)]
map['|'][(-1, 0)] = [(-1, 0)]

map['/'] = {}
map['/'][(0, 1)] = [(-1, 0)]
map['/'][(0, -1)] = [(1, 0)]
map['/'][(1, 0)] = [(0, -1)]
map['/'][(-1, 0)] = [(0, 1)]

map['\\'] = {}
map['\\'][(0, 1)] = [(1, 0)]
map['\\'][(0, -1)] = [(-1, 0)]
map['\\'][(1, 0)] = [(0, 1)]
map['\\'][(-1, 0)] = [(0, -1)]

# [((position), (direction))]
curr = [((0, 0), (0, 1))]
next = []
# already visited nodes/directions
visited = set()
visited_xy = set()

while len(curr) > 0:
    for ((x, y), (dir_x, dir_y)) in curr:
        # out of bounds
        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
            continue

        # already seen
        if ((x, y), (dir_x, dir_y)) in visited:
            continue

        visited.add(((x, y), (dir_x, dir_y)))
        visited_xy.add((x, y))

        c = lines[x][y]
        for (next_x, next_y) in map[c][(dir_x, dir_y)]:
            next.append(((x + next_x, y + next_y), (next_x, next_y)))

    curr = next
    next = []

print(len(visited_xy))

if False:
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if (x, y) in visited_xy:
                print('#', end='')
            else:
                print('.', end='')

        print("")
