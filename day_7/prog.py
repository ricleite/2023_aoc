
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

def kind(hand):
    s = list(set(hand))

    off = 0x100000
    # five of a kind
    if len(s) == 1:
        return off * 0xA
    # four of a kind
    if len(s) == 2 and (hand.count(s[0]) == 1 or hand.count(s[0]) == 4):
        return off * 0x9
    # full house
    if len(s) == 2 and (hand.count(s[0]) == 2 or hand.count(s[0]) == 3):
        return off * 0x8
    # three of a kind
    if len(s) == 3 and len([x for x in s if hand.count(x) == 3]) == 1:
        return off * 0x7
    # two pair
    if len(s) == 3 and len([x for x in s if hand.count(x) == 2]) == 2:
        return off * 0x6
    # one pair
    if len(s) == 4:
        return off * 0x5

    # high card
    assert(len(s) == 5)
    return off * 0x4

def number(hand):
    assert(len(hand) == 5)

    res = 0
    for (i, h) in enumerate(hand):
        n = 0
        if h.isdigit():
            n = int(h)
        elif h == 'T':
            n = 0xA
        elif h == 'J':
            n = 0xB
        elif h == 'Q':
            n = 0xC
        elif h == 'K':
            n = 0xD
        elif h == 'A':
            n = 0xE
        else:
            assert(false)

        res += (n * 0x10 ** (4 - i))

    return res

entries = []
for line in lines:
    ss = line.split()
    assert(len(ss) == 2)

    o = {}
    o['hand'] = ss[0]
    o['bid'] = int(ss[1])
    o['value'] = kind(ss[0]) + number(ss[0])

    entries.append(o)


entries.sort(key = lambda o: o['value'])

res = 0
for i, o in enumerate(entries):
    res += o['bid'] * (i + 1)

print(res)
