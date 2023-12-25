
# https://adventofcode.com/2023/day/23
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

max_x = len(lines)
max_y = len(lines[0])

# in example and input, the start/end are always in these positions
start_x = 0
start_y = 1

end_x = max_x - 1
end_y = max_y - 2

# observation: the input is a map with lots of paths, with few branches
# so it's better to represent it as a fully-connected graph than a 2d grid, and faster to go through as well

nodes = [{ 'coords': (start_x, start_y) }, { 'coords': (end_x, end_y) }]

# find all of the nodes in the graph (besides start/end)
for x in range(1, max_x - 1):
    for y in range(1, max_y - 1):
        if lines[x][y] == '#':
            continue

        count = 0
        for (next_x, next_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if lines[next_x][next_y] != '#':
                count += 1

        if count > 2:
            node = {}
            node['coords'] = (x, y)
            nodes.append(node)

# prepopulate a few properties
nodes_by_pos = {}
for i, node in enumerate(nodes):
    node['id'] = i
    # list of (id, distance)
    node['neighbors'] = []

    nodes_by_pos[node['coords']] = node

# now find what nodes connect to what nodes
for node in nodes:
    curr = [(node['coords'][0], node['coords'][1], 0)]
    next = []

    visited = set([(node['coords'][0], node['coords'][1])])
    while len(curr) > 0:
        for (x, y, dist) in curr:
            for (next_x, next_y) in [(x + 1, y), (x - 1, y,), (x, y + 1), (x, y - 1)]:
                # out of bounds
                if next_x < 0 or next_x >= len(lines) or next_y < 0 or next_y >= len(lines[0]):
                    continue

                # not a path
                if lines[next_x][next_y] == '#':
                    continue

                if (next_x, next_y) in visited:
                    continue

                if (next_x, next_y) in nodes_by_pos:
                    neighbor = nodes_by_pos[(next_x, next_y)]
                    node['neighbors'].append((neighbor['coords'][0], neighbor['coords'][1], dist + 1))
                    continue

                next.append((next_x, next_y, dist + 1))
                visited.add((x, y))

        curr = next
        next = []

# finally have a graph to work with - go through it
curr = [(start_x, start_y, 0, [(start_x, start_y)])]
next = []

longest = 0
longest_path = None

print(f"number of nodes: {len(nodes)}")

length = 0
while len(curr) > 0:
    print(len(curr), length)
    length += 1
    for (x, y, dist, path) in curr:
        if x == end_x and y == end_y:
            longest = max(longest, dist)
            longest_path = path
            continue

        node = nodes_by_pos[(x, y)]
        for (neighbor_x, neighbor_y, neighbor_dist) in node['neighbors']:
            if (neighbor_x, neighbor_y) in path:
                continue

            next.append((neighbor_x, neighbor_y, dist + neighbor_dist, path + [(neighbor_x, neighbor_y)]))

    curr = next
    next = []

print(longest)
