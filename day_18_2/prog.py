
# https://adventofcode.com/2023/day/18
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# strategy: turn into a line-sweep problem

map = {}
map['R'] = (0, 1)
map[0] = (0, 1) # 'R'
map['D'] = (1, 0)
map[1] = (1, 0) # 'D'
map['L'] = (0, -1)
map[2] = (0, -1) # 'L'
map['U'] = (-1, 0)
map[3] = (-1, 0) # 'U'

coords = [(0, 0)]
# start off with the current point - so really 1 of area already
count = 1

for line in lines:
    # format: (#7a21e3)
    color = line.split()[2]
    color = color.replace('(#', '')
    color = color.replace(')', '')
    # now only have digits, first 5 are length
    length = int(color[:5], base=16) + 0
    # last is direction
    dir = int(color[5:], base=16)

    # add up length when moving right/down - otherwise these are not counted by the later line sweep
    # (to understand this, see graphical view of first example - notice how the Y axis has 7 '#', even though the movement is only of 6)
    if dir == 'R' or dir == 'D' or dir == 0 or dir == 1:
        count += length

    coords.append((coords[-1][0] + map[dir][0] * length, coords[-1][1] + map[dir][1] * length))

# get rid of initial point - it will be duplicate since path ends at start
coords = coords[1:]
# sort by x, then by y
coords.sort()

# now go through in line-sweep fashion
intersections = []
last_x = 0
i = 0
while i < len(coords):
    # observation: there must be 2 * N intersections, because it's a bunch of rectangles
    assert(len(intersections) % 2 == 0)

    curr_x = coords[i][0]
    # sort by y
    intersections.sort(key=lambda coord: coord[1])

    print(last_x, curr_x, intersections)

    j = 0
    while j < len(intersections):
        x1, y1 = intersections[j]
        x2, y2 = intersections[j + 1]
        assert(curr_x > last_x)
        assert(y2 > y1)
        count += (curr_x - last_x) * (y2 - y1)
        j += 2

    # accumulate current line
    while i < len(coords) and coords[i][0] == curr_x:
        # definitely not efficient, but it does not matter
        # (could use a.. indexed structure of some sort to speed this search up)

        match_idx = -1
        for idx, (x, y) in enumerate(intersections):
            if y == coords[i][1]:
                assert(match_idx == -1)
                match_idx = idx

        if match_idx >= 0:
            intersections.pop(match_idx)
        else:
            intersections.append(coords[i])

        i += 1

    last_x = curr_x

assert(len(intersections) == 0)

print(coords)
print(count)
