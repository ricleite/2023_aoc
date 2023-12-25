
# https://adventofcode.com/2023/day/20
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

modules = {}

# format: <source> -> <dest1>, <dest2>, ...
# example: broadcaster -> a, b, c
# example: %a -> b
for line in lines:
    ss = line.split(' -> ')
    source = ss[0]
    dests = ss[1].split(', ')

    type = ''
    state = 0
    if source.startswith('%'):
        type = 'flip-flop'
        source = source[1:]
        state = 0 # off
    elif source.startswith('&'):
        type = 'conjunction'
        source = source[1:]
        state = {} # map with a value for each input, filled later

    modules[source] = {}
    modules[source]['type'] = type
    modules[source]['dests'] = dests
    modules[source]['state'] = state

assert('broadcaster' in modules)
assert(modules['broadcaster']['type'] == '')

# fill state of conjunction modules
for module in modules.keys():
    for dest in modules[module]['dests']:
        if dest not in modules or modules[dest]['type'] != 'conjunction':
            continue

        modules[dest]['state'][module] = 0 # off


# strategy: there are 4 key modules to inspect, that lead to `rx`:
# qf, rc, ll, gv
# (to see why, look at `input.dot` in dot/graphviz)
# figure out how long it takes until each emits `low`

periods = {}
periods['qf'] = -1
periods['rc'] = -1
periods['ll'] = -1
periods['gv'] = -1

pushes = 0

while any([period < 0 for period in periods.values()]):
    pushes += 1

    rx_pushes = []

    # broadcast sends "off" to all inputs
    curr = [('broadcaster', 0)]
    while len(curr) > 0:
        next = []

        for (module_name, pulse) in curr:
            # found one of the key modules
            if module_name in periods and pulse == 0:
                if periods[module_name] == -1:
                    periods[module_name] = -pushes
                else:
                    # confirm that it is periodical
                    assert((pushes % abs(periods[module_name])) == 0)
                    # then update with the period
                    periods[module_name] = abs(periods[module_name])

            for dest in modules[module_name]['dests']:
                # some are not in modules at all - for example, "output", "rx"
                if dest not in modules:
                    continue

                if modules[dest]['type'] == 'flip-flop':
                    # flip-flop modules ignore high pulses
                    if pulse == 1:
                        continue

                    # flip-flop modules flip between on and off
                    if modules[dest]['state'] == 0:
                        modules[dest]['state'] = 1
                        next.append((dest, 1))
                    else:
                        modules[dest]['state'] = 0
                        next.append((dest, 0))

                elif modules[dest]['type'] == 'conjunction':
                    # conjunction modules remember the type of the most recent pulse received from each of their connected input modules
                    modules[dest]['state'][module_name] = pulse

                    # if they're both on, sends a low pulse to the output module
                    if all([modules[dest]['state'][input] == 1 for input in modules[dest]['state'].keys()]):
                        next.append((dest, 0))
                    else:
                        next.append((dest, 1))

        curr = next

    if 0 in rx_pushes:
        print(pushes)
        break

# now we have all of the periods - need to find the common factor to see when they'd repeat
# experimentally it's all numbers < 10000, so nothing fancy is needed
factors = set()
for period in periods.values():
    for i in range(1, 10000):
        if period % i == 0:
            factors.add(i)

count = 1
for factor in factors:
    count *= factor

print(periods)
print(factors)
print(count)
