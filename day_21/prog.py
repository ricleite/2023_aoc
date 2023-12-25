
# https://adventofcode.com/2023/day/21
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

start_x = 0
start_y = 0
# find start
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == 'S':
            start_x, start_y = (x, y)
            break

cache = {}
def garden_plots(steps, x, y):
    if steps == 0:
        return set([(x, y)])

    if (steps, x, y) in cache:
        return cache[(steps, x, y)]

    count = set()
    for (next_x, next_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        # out of bounds
        if next_x < 0 or next_x >= len(lines) or next_y < 0 or next_y >= len(lines[0]):
            continue

        if lines[next_x][next_y] == '.' or lines[next_x][next_y] == 'S':
            count = count.union(garden_plots(steps - 1, next_x, next_y))

    cache[(steps, x, y)] = count
    return count

print(len(garden_plots(64, start_x, start_y)))
