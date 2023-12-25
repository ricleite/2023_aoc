
# https://adventofcode.com/2023/day/5

f = open('input1')

lines = [line.rstrip() for line in  f.readlines()]

# compute sections - besides the header, each will have a map
sections = [idx for idx, line in enumerate(lines) if len(line) == 0]

seeds = [ int(n) for n in lines[0].split(": ")[1].split(" ")]


def fillMap(lines):
    # first line is an empty line
    # second line is a header
    print(lines[1])

    ls = []

    for line in lines[2:]:
        ss = line.split(' ')
        o = {}
        o['dst'] = int(ss[0])
        o['src'] = int(ss[1])
        o['len'] = int(ss[2])

        ls.append(o)

    return ls

seed2soil = fillMap(lines[sections[0]:sections[1]])
soil2fertilizer = fillMap(lines[sections[1]:sections[2]])
fertilizer2water = fillMap(lines[sections[2]:sections[3]])
water2light = fillMap(lines[sections[3]:sections[4]])
light2temperature = fillMap(lines[sections[4]:sections[5]])
temperature2humidity = fillMap(lines[sections[5]:sections[6]])
humidity2location = fillMap(lines[sections[6]:])

def compute(num, map):
    # large enough that it does not matter if it is wrong
    # (anyhow a "performance optimization")
    dist = 1000000000
    for o in map:
        start = o['src']
        end = o['src'] + o['len']
        dist = min(dist,
            start - num if start > num else dist,
            end - num if end > num else dist)
        if num >= start and num < end:
            res = o['dst'] + num - start
            return (res, dist)

    return (num, dist)

def seed2location(seed):
    fns = [ seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location ]

    # large enough that it does not matter if it is wrong
    # (anyhow a "performance optimization")
    dist = 1000000000
    for fn in fns:
        seed, new_dist = compute(seed, fn)
        dist = min(dist, new_dist)

    return seed, dist

m, _ = seed2location(seeds[0])

for i in range(int(len(seeds) / 2)):
    seed = seeds[i*2]
    len = seeds[i*2+1]

    s = seed
    while s < seed+len:
        location, dist = seed2location(s)
        m = min(m, location)
        s += max(min(dist - 1, (seed+len)-s-1), 1)

print(m)
