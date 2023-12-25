
# https://adventofcode.com/2023/day/11
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

expansion_x = []
expansion_y = []
# expand rows
for x, line in enumerate(lines):
    if all(c == '.' for c in line):
        expansion_x.append(x)

# expand columns
for y in range(0, len(lines[0])):
    if all(line[y] == '.' for line in lines):
        expansion_y.append(y)

debugging = False
if debugging:
    for x, line in enumerate(lines):
        for y, x in enumerate(line):
            print(x, end='')
        print("")

# look for the galaxies
galaxies = []

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '#':
            galaxies.append((x, y))

dist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        (i_x, i_y) = galaxies[i]
        (j_x, j_y) = galaxies[j]
        x_plus = sum([ 1 for x in expansion_x if x > min(i_x, j_x) and x < max(i_x, j_x)])
        y_plus = sum([ 1 for y in expansion_y if y > min(i_y, j_y) and y < max(i_y, j_y)])
        dist += abs(i_x - j_x) + abs(i_y - j_y) + (x_plus + y_plus) * 999999    

print(expansion_x)
print(expansion_y)
print(dist)
