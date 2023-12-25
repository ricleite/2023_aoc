
# https://adventofcode.com/2023/day/4

f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]
sum = 0

# format: Card X: W1 W2 W3 ... | N1 N2 N3 N4
for line in lines:
    # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
    line = ' '.join(line.split())

    ss = line.split(": ")
    assert(len(ss) == 2)

    card = int(ss[0].split(' ')[1])
    rest = ss[1]

    ss = rest.split(' | ')
    winnings = set([ int(n) for n in ss[0].split(' ')])
    numbers = [ int(n) for n in ss[1].split(' ')]

    val = 0;
    for num in numbers:
        if num in winnings:
            val = 1 if val == 0 else val * 2

    sum += val

print(sum)
