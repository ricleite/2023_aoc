
# https://adventofcode.com/2023/day/19
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

# parse workflows
workflows = {}
line_idx = 0
while len(lines[line_idx]) > 0:
    line = lines[line_idx]
    line_idx += 1

    # input example: px{a<2006:qkq,m>2090:A,rfg}
    ss = line.split('{')
    rule_name = ss[0]
    rules = ss[1].replace('}', '').split(',')

    workflows[rule_name] = rules

# skip empty line
assert(len(lines[line_idx]) == 0)
line_idx += 1

# parse parts
parts = []
while line_idx < len(lines):
    line = lines[line_idx]
    line_idx += 1

    # input example:
    # {x=787,m=2655,a=1222,s=2876}
    part = {}
    for attr in line.replace('{', '').replace('}', '').split(','):
        ss = attr.split('=')
        category = ss[0]
        value = int(ss[1])
        part[category] = value

    parts.append(part)

accepted = []
for part in parts:
    # start with workflow """in"""
    state = "in"

    while state in workflows:
        rules = workflows[state]
        for rule in rules:
            # rule examples:
            # - "a<2006:qkq"
            # - "rfg"
            # - "A"

            # slightly more complex rule
            if ':' in rule:
                ss = rule.split(':')
                condition = ss[0]
                dest = ss[1]

                if '<' in condition:
                    # condition example: a<2006
                    ss = condition.split('<')
                    category = ss[0]
                    value = int(ss[1])

                    if part[category] < value:
                        state = dest
                        break
                elif '>' in condition:
                    # condition example: a>2006
                    ss = condition.split('>')
                    category = ss[0]
                    value = int(ss[1])

                    if part[category] > value:
                        state = dest
                        break
                else:
                    print(condition)
                    assert(False)
            else:
                state = rule
                break

    if state == 'A':
        accepted.append(part)

count = 0
for part in accepted:
    for key in part.keys():
        count += part[key]

print(count)
