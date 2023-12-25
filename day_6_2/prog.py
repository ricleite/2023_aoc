
# https://adventofcode.com/2023/day/6/input

f = open('input')

lines = [line.rstrip() for line in f.readlines()]

# format:
# Time:        47     84     74     67
# Distance:   207   1394   1209   1014

time = int(''.join(lines[0].split(":")[1].split()))
distance = int(''.join(lines[1].split(":")[1].split()))

def compute_distance(hold_time, time_limit):
    # distance for given hold time, within the time limit

    assert(hold_time < time_limit)
    return (time_limit - hold_time) * hold_time

def find_first_win(time, distance):
    # assuming a parabola
    # find first winning time; simple binary search
    begin = 0
    end = time
    while True:
        mid = int(begin + (end - begin) / 2)
        d1 = compute_distance(mid, time)
        d2 = compute_distance(mid + 1, time)
        if d1 <= distance and d2 > distance:
            break

        # going down the parabola; go back
        if d1 >= d2:
            end = mid
        # going up the parabola but still winning; go back
        elif d2 > distance:
            end = mid
        # going up the parabola but losing; go forward
        else:
            begin = mid + 1

    return mid + 1

def find_last_win(time, distance):
    begin = 0
    end = time
    while True:
        mid = int(begin + (end - begin) / 2)
        d1 = compute_distance(mid, time)
        d2 = compute_distance(mid + 1, time)
        if d1 > distance and d2 <= distance:
            break

        # going up the parabola; go forward
        if d1 <= d2:
            begin = mid + 1
        # going down the parabola but winning; go forward
        elif d1 > distance:
            begin = mid + 1
        # going down the parabola but losing; go back
        else:
            end = mid

    return mid


print(find_last_win(time, distance) - find_first_win(time, distance) + 1)
