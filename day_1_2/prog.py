

numbers = {
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}

with open("input") as f:
    sum = 0
    for line in f:
        first = None
        last = None
        for idx, c in enumerate(line):
            digit = None
            if c.isdigit():
                digit = c
            else:
                # idea: split the line in order to catch written numbers
                # would be a lot easier in a native language..
                s = line[idx:]
                for n in numbers.keys():
                    if s.startswith(n):
                        digit = numbers[n]

            if digit is not None:
                if first is None:
                    first = digit
                last = digit

        
        if first is not None:
            sum += int(first) * 10 + int(last)

    print(sum)
