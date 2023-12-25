
# https://adventofcode.com/2023/day/6/input

f = open('input')

lines = [line.rstrip() for line in f.readlines()]

# format:
# Time:        47     84     74     67
# Distance:   207   1394   1209   1014

times = [int(time) for time in lines[0].split(":")[1].split()]
distances = [int(distance) for distance in lines[1].split(":")[1].split()]

assert(len(times) == len(distances))

def compute_distance(hold_time, time_limit):
    # distance for given hold time, within the time limit

    assert(hold_time < time_limit)
    return (time_limit - hold_time) * hold_time

res = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    wins = len([1 for hold_time in range(time) if compute_distance(hold_time, time) > distance])
    res *= wins

print(res)
