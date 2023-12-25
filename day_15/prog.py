
# https://adventofcode.com/2023/day/15
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

def hash(ss):
    h = 0
    for s in ss:
        h = ((h + ord(s)) * 17) % 256

    return h

sum = 0
for line in lines:
    ls = line.split(",")

    for ss in ls:
        sum += hash(ss)

print(sum)
