

f = open('input')

lines = f.readlines()

max_i = len(lines)
max_j = max([len(line) for line in lines])

print("max_i: {}, max_j: {}".format(max_i, max_j))

# lazy way of defining a multi-dimensional array
# m = [[0 for j in range(max_j)] for i in range(max_i)]

# another way, as an object
m = [{} for i in range(max_i)]

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
# NOTE: now that I notice, this is stupid - could have verified whether there are symbols close to the numbers in the first pass, and count the numbers only in that case..
ids = set()
nums = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        # it is a symbol
        if not c.isdigit() and c != '.' and c != '\n':
            # check for neighbor numbers
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                try:
                    o = m[i+x][j+y]
                    # id() gives the same number for the same dictionary reference, so it works
                    # it is honestly quite ugly/fragile - but that's what the previous code forces me to do
                    if id(o) not in ids:
                        ids.add(id(o))
                        nums.append(o)

                except:
                    pass

s = sum([o['val'] for o in nums])

print("sum: {}".format(s))

# do not care about not closing `f`
