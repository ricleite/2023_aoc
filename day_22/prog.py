
# https://adventofcode.com/2023/day/22
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# format: [((x, y, z), (x, y, z))]
bricks = []
bricks_by_id = {}
for i, line in enumerate(lines):
    # example input:
    # "1,0,1~1,2,1"
    ss = line.split('~')
    start = [int(s) for s in ss[0].split(',')]
    end = [int(s) for s in ss[1].split(',')]

    # use "start" as the lower coordinate
    if start[2] > end[2]:
        start, end = end, start

    brick = {}
    brick['id'] = i
    brick['start'] = (start[0], start[1], start[2])
    brick['end'] = (end[0], end[1], end[2])
    brick['area'] = 1 + abs(end[0] - start[0]) + abs(end[1] - start[1])
    brick['supports'] = []
    brick['supported_by'] = []

    bricks.append(brick)
    bricks_by_id[brick['id']] = brick


# in the input, no coordinate goes above 300
# so at most the grid is 300x300x300 = 27M pos

# anyway calculate it, takes no effort, makes things faster
max_xy = max([max(brick['start'][0], brick['start'][1], brick['end'][0], brick['end'][1]) for brick in bricks]) + 1

print(f"max_xy: {max_xy}")

# keep a record of what is "lowest" in each position as we sweep through the bricks
# (height, brick_id)
floor = [[(1, -1) for y in range(max_xy)] for x in range(max_xy)]

# sort by z
bricks.sort(key=lambda brick: brick['start'][2])

for brick in bricks:
    # find highest - this is the collision point
    highest = 0
    for x in range(brick['start'][0], brick['end'][0] + 1):
        for y in range(brick['start'][1], brick['end'][1] + 1):
            highest = max(highest, floor[x][y][0])

    # should be impossible - a brick cannot "float up"
    assert(highest <= brick['start'][2])

    # update brick
    diff = brick['start'][2] - highest
    brick['start'] = (brick['start'][0], brick['start'][1], brick['start'][2] - diff)
    brick['end'] = (brick['end'][0], brick['end'][1], brick['end'][2] - diff)

    # update floor
    for x in range(brick['start'][0], brick['end'][0] + 1):
        for y in range(brick['start'][1], brick['end'][1] + 1):
            # there is a brick here, that now supports our brick
            if floor[x][y][0] == brick['start'][2] and floor[x][y][1] >= 0:
                old_brick = floor[x][y][1]
                bricks_by_id[old_brick]['supports'].append(brick['id'])
                brick['supported_by'].append(old_brick)

            floor[x][y] = (brick['end'][2] + 1, brick['id'])

bricks_to_disintegrate = set()

for brick in bricks:
    can_disintegrate = True
    for top_brick_id in brick['supports']:
        top_brick = bricks_by_id[top_brick_id]
        if not any([support_id != brick['id'] for support_id in top_brick['supported_by']]):
            can_disintegrate = False
            break

    if can_disintegrate:
        bricks_to_disintegrate.add(brick['id'])

print(len(bricks_to_disintegrate))
