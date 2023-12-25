
# https://adventofcode.com/2023/day/10
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]
dists = [ ['I' for i in range(len(line))] for line in lines ]

# lines is already in a mildly-ok format to use
# find S
start_i = -1
start_j = -1
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            start_i = i
            start_j = j

assert(start_i >= 0 and start_j >= 0)

dists[start_i][start_j] = 1

directions = {
    'S': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '-' : [(0, -1), (0, 1)],
    '|' : [(-1, 0), (1, 0)],
    'L' : [(-1, 0), (0, 1)],
    'J' : [(-1, 0), (0, -1)],
    '7' : [(0, -1), (1, 0)],
    'F' : [(0, 1), (1, 0)]
}

# go through the matrix
curr_set = [(start_i, start_j)]

while len(curr_set) > 0:
    next_set = [] 

    for (curr_x, curr_y) in curr_set:
        for (x, y) in directions[lines[curr_x][curr_y]]:
            n_x = curr_x+x
            n_y = curr_y+y
            try:
                n = lines[n_x][n_y]
            except:
                continue

            # was already found
            if dists[n_x][n_y] == 'X':
                continue

            # check if it is connected
            if not n in directions:
                continue

            if not any([curr_x == n_x + x and curr_y == n_y + y for (x, y) in directions[n]]):
                continue

            dists[n_x][n_y] = 'X'
            next_set.append((n_x, n_y))

    curr_set = next_set

# by now, the loop is tagged with "1"
# everything else with "-1"

# build a "oversized" version of the tiles
oversized = [ [ 'I' for y in range(3 * len(line))] for x in range(3 * len(lines)) ]

# overlay loop onto oversized
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if dists[x][y] != 'X':
            continue

        x_coord = x * 3 + 1
        y_coord = y * 3 + 1
        oversized[x_coord][y_coord] = 'X'

        for (x_off, y_off) in directions[c]:
            oversized[x_coord+x_off][y_coord+y_off] = 'X'

# go through oversized, tag all edges as 0
# then move inside
curr_set = [(0, 0)]

while len(curr_set) > 0:
    next_set = [] 

    for (curr_x, curr_y) in curr_set:
        for (x, y) in directions['S']:
            n_x = curr_x+x
            n_y = curr_y+y
            try:
                # was already found
                n = oversized[n_x][n_y]
                if n == 'X' or n == 'O':
                    continue
            except:
                continue

            oversized[n_x][n_y] = 'O'
            next_set.append((n_x, n_y))

    curr_set = next_set

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        zero_count = 0
        for x_off in range(3):
            for y_off in range(3):
                if oversized[3*x+x_off][3*y+y_off] == 'O':
                    zero_count += 1

        if zero_count > 0 and dists[x][y] == 'I':
            dists[x][y] = 'O'

print(sum([sum([1 for x in dist if x == 'I']) for dist in dists]))

debugging = False
if debugging:
    for x, dist in enumerate(dists):
        for y, x in enumerate(dist):
            print(x, end='')
        print("")

    for x, dist in enumerate(oversized):
        for y, x in enumerate(dist):
            print(x, end='')
        print("")
