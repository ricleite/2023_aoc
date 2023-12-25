
# https://adventofcode.com/2023/day/2

f = open('input')

lines = f.readlines()
sum = 0

for line in lines:
    line = line.rstrip()

    # format: "Game X: Y color, Z color; A color, Y color; ..."
    ss = line.split(': ')
    assert(len(ss) == 2)

    # format: "Game X"
    game = int(ss[0].replace("Game ", ""))
    # format: "Y color, Z color; A color, Y color; ..."
    sets = ss[1].split('; ')

    # whether this game is still eligible
    maxes = {}
    for s in sets:
        # format : "Y color, Z color, ..."
        colors = s.split(', ')

        for c in colors:
            # format: "Y color"
            c = c.split(' ')
            assert(len(c) == 2)

            num = int(c[0])
            color = c[1]

            try:
                maxes[color] = max(maxes[color], num)
            except:
                maxes[color] = num

    n = 1
    for _, m in maxes.items():
        n *= m

    sum += n

print(sum)

    