
# https://adventofcode.com/2023/day/12
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]


# format: .??..??...?##. 1,1,3
springs = []
groups = []

for line in lines:
    ss = line.split(" ")
    assert(len(ss) == 2)

    spring = ss[0]
    group = ss[1]

    # part 2: expand

    for _ in range(4):
        spring = spring + "?" + ss[0]
        group = group + "," + ss[1]

    # micro-optimization: ensure spring ends with "."
    spring = spring + "."
    # micro-optimization: don't care about rows of "."
    while spring != spring.replace("..", "."):
        spring = spring.replace("..", ".")

    group = [ int(g) for g in group.split(",") ]

    springs.append(spring)
    groups.append(group)

map = {}
def count_combos(spring, group, spring_idx, group_idx):
    if (spring_idx, group_idx) in map:
        return map[(spring_idx, group_idx)]

    # skip spaces
    while spring_idx < len(spring) and spring[spring_idx] == '.':
        spring_idx += 1

    # base case(s)
    if group_idx >= len(group):
        if all([s == '.' or s == '?' for s in spring[spring_idx:]]):
            return 1

        # prune
        return 0

    if spring_idx >= len(spring):
        return 0

    # iterative case
    combos = 0
    # assume ? = #
    if spring_idx + group[group_idx] < len(spring):
        subspring = spring[spring_idx:spring_idx + group[group_idx]]
        subspring_last = spring[spring_idx + group[group_idx]]
        if all([s == '?' or s == '#' for s in subspring]) and (subspring_last == '.' or subspring_last == '?'):
            combos += count_combos(spring, group, spring_idx + group[group_idx] + 1, group_idx + 1)

    # assume ? = .
    if spring[spring_idx] == '?':
        combos += count_combos(spring, group, spring_idx + 1, group_idx)

    map[(spring_idx, group_idx)] = combos
    return combos

combos = 0
for i, spring in enumerate(springs):
    print(i, combos)
    # reset map
    map = {}
    combos += count_combos(springs[i], groups[i], 0, 0)

print(combos)
