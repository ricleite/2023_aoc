

f = open('input')

lines = f.readlines()

# another way, as an object
m = [{} for i in range(len(lines))]

# first pass - setup all numerical positions
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        
        if c.isdigit():
            # get/set an object that contains an integer, that is shared for all positions where the integer sits
            o = { 'val' : 0 }
            if j > 0 and j - 1 in m[i]:
                o = m[i][j - 1]

            o['val'] = o['val'] * 10 + int(c)

            m[i][j] = o

# second pass - find numbers near symbols
s = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        # it is a symbol
        if not c.isdigit() and c != '.' and c != '\n':
            ids = set()
            nums = []
            # check for neighbor numbers
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                try:
                    o = m[i+x][j+y]
                    if id(o) not in ids:
                        ids.add(id(o))
                        nums.append(o)
                except:
                    pass

            # exactly 2 numbers => see gear ratio
            if len(nums) == 2:
                s += nums[0]['val'] * nums[1]['val']

print("sum: {}".format(s))

# do not care about not closing `f`
