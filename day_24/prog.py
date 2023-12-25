
# https://adventofcode.com/2023/day/24
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

hailstones = []

for line in lines:
    # format: "19, 13, 30 @ -2, 1, -2"
    ss = line.split('@')
    pos = [int(s) for s in ss[0].split(',')]
    vel = [int(s) for s in ss[1].split(',')]
    hailstones.append(((pos[0], pos[1], pos[2]), (vel[0], vel[1], vel[2])))

interval_min = 200000000000000
interval_max = 400000000000000

# compute intersections only in x/y
count = 0

for i, h1 in enumerate(hailstones[:-1]):
    for h2 in hailstones[i+1:]:
        # transform h1/h2 into a line equations
        # ax + by + c = 0
        a1 = -h1[1][1]
        b1 = h1[1][0]
        c1 = h1[0][0] * h1[1][1] - h1[1][0] * h1[0][1]

        a2 = -h2[1][1]
        b2 = h2[1][0]
        c2 = h2[0][0] * h2[1][1] - h2[1][0] * h2[0][1]

        # then calculate the intersection
        try:
            x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
            y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
        except:
            continue

        # need to ensure t >= 0
        # so that the intersection is in the future
        t1 = (x - h1[0][0]) / h1[1][0]
        t2 = (y - h2[0][1]) / h2[1][1]
        if t1 < 0 or t2 < 0:
            continue

        # check if it's in the interval
        if x >= interval_min and x <= interval_max and y >= interval_min and y <= interval_max:
            print(h1, h2)
            print(f"({x}, {y}), {t1}, {t2}")
            count += 1

print(count)
