
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


curr = "AAA"
steps = 0
while curr != "ZZZ":
    idx = steps % len(instructions)
    curr = map[curr][0] if instructions[idx] == 'L' else map[curr][1]
    steps += 1

print(steps)
