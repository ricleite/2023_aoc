
# https://adventofcode.com/2023/day/15
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

def hash(ss):
    h = 0
    for s in ss:
        h = ((h + ord(s)) * 17) % 256

    return h

map = {}
for i in range(256):
    map[i] = []

sum = 0
for line in lines:
    for code in line.split(","):
        # example: "pc-"
        if '-' in code:
            code = code.split("-")[0]
            # remove "code" from box
            idx = hash(code)
            map[idx] = [(c, l) for (c, l) in map[idx] if c != code]
        elif '=' in code:
            ss = code.split("=")
            code = ss[0]
            lens = int(ss[1])
            idx = hash(code)
            pos = -1
            for i, (c, l) in enumerate(map[idx]):
                if c == code:
                    pos = i
                    break

            if pos >= 0:
                # replace old lens
                map[idx][pos] = (code, lens)
            else:
                # insert new lens
                map[idx].append((code, lens))

        else:
            assert(False)

sum = 0
for i in range(256):
    for j, (c, l) in enumerate(map[i]):
        print(f"Box {i + 1}, Slot {j + 1}, Code {c}, Lens {l}")
        sum += (i + 1) * (j + 1) * l

print(sum)
