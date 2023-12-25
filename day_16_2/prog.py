
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

def energized(curr):
    # [((position), (direction))]
    curr = [curr]
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

    return len(visited_xy)

max_energized = 0
for x, line in enumerate(lines):
    max_energized = max(max_energized, energized(((x, 0), (0, 1))), energized(((x, len(line) - 1), (0, -1))))
for y, c in enumerate(lines[0]):
    max_energized = max(max_energized, energized(((0, y), (1, 0))), energized(((len(lines) -1, y), (-1, 0))))

print(max_energized)
