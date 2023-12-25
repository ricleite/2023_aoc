
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

def accepted_parts(state, part):
    if state == 'A':
        return [part]
    elif state == 'R':
        return []

    final_parts = []

    for rule in workflows[state]:
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

                value_min, value_max = part[category]
                # can satisfy
                if value_min < value:
                    # for the example: (value_min, min(value_max, 2006))
                    new_part = part.copy()
                    new_part[category] = (value_min, min(value_max, value))
                    final_parts = final_parts + accepted_parts(dest, new_part)

                # in case it "does not pass"
                # for the example: (max(value_min, 2006), value_max
                part[category] = (max(value_min, value), value_max)

            elif '>' in condition:
                # condition example: a>2006
                ss = condition.split('>')
                category = ss[0]
                value = int(ss[1])

                value_min, value_max = part[category]
                # can satisfy
                if value_max > value:
                    new_part = part.copy()
                    new_part[category] = (max(value_min, value + 1), value_max)
                    final_parts = final_parts + accepted_parts(dest, new_part)

                # in case it "does not pass"
                part[category] = (value_min, min(value_max, value + 1))

            else:
                print(condition)
                assert(False)
        else:
            final_parts = final_parts + accepted_parts(rule, part)
            break

    return final_parts

# default part - goes through the entire range
part = {}
part['x'] = (1, 4001)
part['m'] = (1, 4001)
part['a'] = (1, 4001)
part['s'] = (1, 4001)

accepted = accepted_parts('in', part)

count = 0
for part in accepted:
    part_count = 1
    for key in part.keys():
        part_count *= part[key][1] - part[key][0]

    count += part_count

print(count)
