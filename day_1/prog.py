

with open("input") as f:
    sum = 0
    for line in f:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        
        if first is not None:
            sum += int(first) * 10 + int(last)

    print(sum)
