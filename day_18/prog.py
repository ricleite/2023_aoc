
# https://adventofcode.com/2023/day/18
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# strategy: be lazy, turn into a matrix

map = {}
map['U'] = (-1, 0)
map['D'] = (1, 0)
map['L'] = (0, -1)
map['R'] = (0, 1)

# first pass
min_x, max_x = (0, 0)
min_y, max_y = (0, 0)
curr_x = 0
curr_y = 0
for line in lines:
    ss = line.split()
    dir = ss[0]
    length = int(ss[1])
    color = ss[2]

    dir_x, dir_y = map[dir]
    curr_x += dir_x * length
    curr_y += dir_y * length

    min_x = min(min_x, curr_x)
    max_x = max(max_x, curr_x)
    min_y = min(min_y, curr_y)
    max_y = max(max_y, curr_y)

# fix coordinates, build field
# and make field "one larger" in every direction (see +1/+2 in end)
curr_x = min_x * -1 + 1
curr_y = min_y * -1 + 1 
max_x = max_x - min_x + 2
max_y = max_y - min_y + 2
min_x = 0
min_y = 0

print(f"max_x: {max_x}, max_y: {max_y}")

field = [[ '.' for y in range(max_y) ] for x in range(max_x)]

# second pass
for line in lines:
    ss = line.split()
    dir = ss[0]
    length = int(ss[1])
    color = ss[2]

    dir_x, dir_y = map[dir]
    for _ in range(length):
        field[curr_x][curr_y] = '#'
        curr_x += dir_x
        curr_y += dir_y

# do coloring
curr = [(0, 0)]
next = []
field[0][0] = 'O'
while len(curr) > 0:
    print(len(curr))
    for x, y in curr:
        for (off_x, off_y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + off_x
            new_y = y + off_y
            try:
                c = field[new_x][new_y]
                if c != '.':
                    continue
            except:
                continue

            field[new_x][new_y] = 'O'
            next.append((new_x, new_y))

    curr = next
    next = []

count = 0
# finally, get whatever is not colored
for x in range(max_x):
    for y in range(max_y):
        c = field[x][y]
        if c == '#' or c == '.':
            count += 1

print(count)
