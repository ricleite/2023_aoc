
# https://adventofcode.com/2023/day/23
f = open('input1')

lines = [ line.rstrip() for line in f.readlines() ]

# in example and input, the start/end are always in these positions
start_x = 0
start_y = 1

end_x = len(lines) - 1
end_y = len(lines[0]) - 2

curr = [(start_x, start_y, set([(start_x, start_y)]))]
next = []

longest = 0

while len(curr) > 0:
    for (x, y, path) in curr:
        if x == end_x and y == end_y:
            longest = max(longest, len(path) - 1)
            continue

        for (next_x, next_y, symbol) in [(x + 1, y, 'v'), (x - 1, y, '^'), (x, y + 1, '>'), (x, y - 1, '<')]:
            # out of bounds
            if next_x < 0 or next_x >= len(lines) or next_y < 0 or next_y >= len(lines[0]):
                continue

            # not a path
            if lines[next_x][next_y] != '.' and lines[next_x][next_y] != symbol:
                continue

            if (next_x, next_y) in path:
                continue

            next.append((next_x, next_y, path.union([(next_x, next_y)])))

    curr = next
    next = []

print(longest)
