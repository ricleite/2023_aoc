
# https://adventofcode.com/2023/day/14
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# transform the figure into something easier to work with
transform = []
for i in range(len(lines[0])):
    transform.append([line[i] for line in lines])

load = 0
# then it is quite easy to see where each rock should stay
for line in transform:
    support_idx = 0
    for i, c in enumerate(line):
        if c == '#':
            support_idx = i + 1
        elif c == 'O':
            load += len(line) - support_idx
            support_idx += 1

print(load)
