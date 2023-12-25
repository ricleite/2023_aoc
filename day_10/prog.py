
# https://adventofcode.com/2023/day/10
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]
dists = [ [-1 for i in range(len(line))] for line in lines ]

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

dists[start_i][start_j] = 0

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
            if dists[n_x][n_y] >= 0:
                continue

            # check if it is connected
            if not n in directions:
                continue

            if not any([curr_x == n_x + x and curr_y == n_y + y for (x, y) in directions[n]]):
                continue

            dists[n_x][n_y] = dists[curr_x][curr_y] + 1
            next_set.append((n_x, n_y))

    curr_set = next_set

print(max([max(x) for x in dists]))
