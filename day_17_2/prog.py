
# https://adventofcode.com/2023/day/17
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# Dijiskra-like approach
# except there's no sorting of the current nodes, so it's definitely much worse
# (and this also means that there is a solution for *every* destination node, not just the goal)

# direction => [((direction), is-same-dir)]
map = {}
map[(0, 1)] = [((0, 1), 1), ((1, 0), 0), ((-1, 0), 0)]
map[(0, -1)] = [((0, -1), 1), ((1, 0), 0), ((-1, 0), 0)]
map[(1, 0)] = [((1, 0), 1), ((0, 1), 0), ((0, -1), 0)]
map[(-1, 0)] = [((-1, 0), 1), ((0, 1), 0), ((0, -1), 0)]

# [((x, y), heat-loss, (dir_x, dir_y), same-dir))]
curr = [((0, 0), 0, (1, 0), 0)]
next = []
# visited nodes
# ((x, y), (dir_y, dir_y), same_dir) => heat-loss
visited = {}

while len(curr) > 0:
    print(len(curr))
    for ((x, y), heat_loss, (dir_x, dir_y), same_dir) in curr:
        key = ((x, y), (dir_x, dir_y), same_dir)
        if key in visited and heat_loss >= visited[key]:
            # already have a better path - skip this
            continue
        else:
            visited[key] = heat_loss

        for ((next_x, next_y), is_same_dir) in map[(dir_x, dir_y)]:
            new_x = x + next_x
            new_y = y + next_y
            # out of bounds
            if new_x < 0 or new_x >= len(lines) or new_y < 0 or new_y >= len(lines[0]):
                continue

            new_heat_loss = heat_loss + int(lines[new_x][new_y])
            new_same_dir = same_dir + 1 if is_same_dir else 1
            # new rules: go in same direction between 4-10 times
            if is_same_dir and new_same_dir > 10:
                continue
            if not is_same_dir and same_dir > 0 and same_dir < 4:
                continue

            next.append(((new_x, new_y), new_heat_loss, (next_x, next_y), new_same_dir))

    curr = next
    next = []

final_x = len(lines) - 1
final_y = len(lines[0]) - 1
min_heat = 1000000000
for ((x, y), (dir_x, dir_y), same_dir) in visited:
    key = ((x, y), (dir_x, dir_y), same_dir)
    if x == final_x and y == final_y and same_dir >= 4 and same_dir <= 10:
        min_heat = min(min_heat, visited[key])

print(min_heat)
