
# https://adventofcode.com/2023/day/5

f = open('input')

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
    for o in map:
        if num >= o['src'] and num < o['src'] + o['len']:
            return o['dst'] + num - o['src']

    return num

def seed2location(seed):
    c = compute
    return c(c(c(c(c(c(c(seed, seed2soil), soil2fertilizer), fertilizer2water), water2light), light2temperature), temperature2humidity), humidity2location)

res = min([seed2location(seed) for seed in seeds])

print(res)
