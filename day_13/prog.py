
# https://adventofcode.com/2023/day/13
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

patterns = [[]]

for line in lines:
    if len(line) == 0:
        if patterns[-1] != []:
            patterns.append([])

    else:
        patterns[-1].append(line)

sum = 0

for pattern in patterns:

    # rows
    for i in range(1, len(pattern)):
        valid = True
        left = [n for n in range(i - 1, -1, -1)]
        right = [n for n in range(i, len(pattern))]
        print("row", left, right)

        for j in range(min(len(left), len(right))):
            if pattern[left[j]] != pattern[right[j]]:
                valid = False
                break

        if valid:
            sum += i * 100

    # columns
    # transform the pattern and do the same thing
    transform = []
    for i in range(len(pattern[0])):
        transform.append([p[i] for p in pattern])

    for i in range(1, len(transform)):
        valid = True
        left = [n for n in range(i - 1, -1, -1)]
        right = [n for n in range(i, len(transform))]
        print("column", left, right)

        for j in range(min(len(left), len(right))):
            if transform[left[j]] != transform[right[j]]:
                valid = False
                break

        if valid:
            sum += i

print(sum)
