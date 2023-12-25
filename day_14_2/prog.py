
# https://adventofcode.com/2023/day/14
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# transform the figure into something easier to work with
def transform(lines):
    trans = []
    for i in range(len(lines[0])):
        trans.append([line[i] for line in lines])

    return trans

# rotate clock-wise (e.g., N to W)
def rotate(lines):
    trans = []
    line_len = len(lines[0])
    for i in range(line_len):
        trans.append([line[line_len - 1 - i] for line in lines])

    return trans

def calc_load(lines):
    load = 0
    for line in lines:
        for i, c in enumerate(line):
            if c == 'O':
                load += len(line) - i

    return load

def update(lines):
    for line in lines:
        support_idx = 0
        for i, c in enumerate(line):
            if c == '#':
                support_idx = i + 1
            elif c == 'O':
                line[i] = '.'
                line[support_idx] = 'O'
                support_idx += 1


def print_lines(lines):
    for line in lines:
        print(''.join(line))

    print()

# initial: north
lines = transform(lines)

# expensive: keep a list of all last versions, in the hope we can quickly find a match
cache = [ lines ]

total_cycles = 1000000000
cycle = 0
while cycle < total_cycles:

    # perform the cycle
    # N/W/S/E
    for _ in range(4):
        update(lines)
        lines = rotate(lines)

    # check whether this has happened before
    if lines in cache:
        # now we can jump straight to the end, as we can figure out what should happen in the last cycle
        idx = cache.index(lines)
        period = len(cache) - idx

        print("Stable at cycle {}, idx {}, period {}".format(cycle, idx, period))

        offset = (total_cycles - (cycle + 1)) % period
        print(calc_load(cache[idx + offset]))
        break

    else:
        # add a copy
        cache.append(transform(transform(lines)))

    cycle += 1


