
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

res = 0
for line in lines:
    # ex: 0 3 6 9 12 15
    seq = [int(s) for s in line.split()]

    seqs = [ seq ]
    # need to compute the diffs, recursively, until we are all lefts with 0s
    while any(seqs[-1]): # does the last sequence have any non-0?
        seq = [ seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1]) - 1)]
        seqs.append(seq)

    # now do extrapolation
    seqs[:-1].append(0)

    for i in range(1, len(seqs)):
        diff = seqs[-i][-1]
        seqs[-(i+1)].append(seqs[-(i+1)][-1] + diff)

    res += seqs[0][-1]

print(res)
