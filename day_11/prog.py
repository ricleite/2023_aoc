
# https://adventofcode.com/2023/day/11
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

new_lines = []
# expand rows
for line in lines:
    new_lines.append([c for c in line])
    if all(c == '.' for c in line):
        new_lines.append([c for c in line])

# expand columns
# backwards to avoid silly indexing issues
for j in range(len(lines[0]) - 1, -1, -1): # do [len - 1, len -2, ..., 0]
    if all(line[j] == '.' for line in lines):
        for new_line in new_lines:
            new_line.insert(j, '.')

lines = new_lines

debugging = False
if debugging:
    for x, line in enumerate(lines):
        for y, x in enumerate(line):
            print(x, end='')
        print("")

# look for the galaxies
galaxies = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            galaxies.append((i, j))

dist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        (i_x, i_y) = galaxies[i]
        (j_x, j_y) = galaxies[j]
        dist += abs(i_x - j_x) + abs(i_y - j_y)

print(dist)
