
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

high_pulse_count = 0
low_pulse_count = 0

# push button 1000 times
for _ in range(1000):
    # button sends "low" to broadcaster
    low_pulse_count += 1
    # broadcast sends "off" to all inputs
    curr = [('broadcaster', 0)]

    while len(curr) > 0:
        next = []

        for (module_name, pulse) in curr:
            for dest in modules[module_name]['dests']:
                if pulse == 1:
                    high_pulse_count += 1
                else:
                    low_pulse_count += 1 

                # some are not in modules at all - for example, "output"
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

print(low_pulse_count, high_pulse_count)
print(low_pulse_count * high_pulse_count)
