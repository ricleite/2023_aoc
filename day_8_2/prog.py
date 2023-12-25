
# https://adventofcode.com/2023/day/8
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# ex: LLR
instructions = lines[0]

map = {}
for line in lines[2:]:
    # ex: ZZZ = (ZZZ, ZZZ)

    start = line[0:3]
    left = line[7:10]
    right = line[12:15]

    map[start] = (left, right)


curr = [s for s in map.keys() if s.endswith("A")]
# bit of an optimization: keep track of "when" each Z is caught
track = [0 for s in curr]

steps = 0
while not all(track):
    idx = steps % len(instructions)
    idx = 0 if instructions[idx] == 'L' else 1
    curr = [map[s][idx] for s in curr]
    steps += 1

    for i, s in enumerate(curr):
        if track[i] == 0 and s.endswith("Z"):
            track[i] = steps


print(track, steps)

# now that we have the "occurrences" of each one - just figure out the lowest common factor
# easy enough to do it in multiples
step_inc = steps
count = len([s for s in track if steps % s == 0])

while count < len(track):
    steps += step_inc

    new_count = len([s for s in track if steps % s == 0])
    if new_count > count:
        print(count, step_inc, steps)
        step_inc = steps
        count = new_count


print(step_inc)
print(steps)
