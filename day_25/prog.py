
# https://adventofcode.com/2023/day/25
f = open('input')

lines = [ line.rstrip() for line in f.readlines() ]

graph = {}
edges = []
for line in lines:
    # example: rhn: xhk bvb hfx
    ss = line.split(': ')
    node = ss[0]
    neighbors = ss[1].split(' ')
    if node not in graph:
        graph[node] = set()

    for neighbor in neighbors:
        if neighbor not in graph:
            graph[neighbor] = set()

        graph[node].add(neighbor)
        graph[neighbor].add(node)
        edges.append((node, neighbor))

# strategy: start with a random node, build up a network of neighbors that are tightly connected
# once we find that the number of edges between our network and the remaining network <= 3, we're good

edges_to_cut = 3

# I *think* we need to try with several nodes, since the "head start" might have one of the 3 edges we need to cut
for start in graph.keys():

    # build up a network of neighbors
    network = set([start])
    edges = [(start, neighbor) for neighbor in graph[start]]

    while len(edges) > edges_to_cut:
        # find the most "heavily connected" node to the network
        edges.sort(key=lambda edge: len([node for node in graph[edge[1]] if node in network]), reverse=True)

        network.add(edges[0][1])

        for neighbor in graph[edges[0][1]]:
            edges.append((edges[0][1], neighbor))

        # remove all edges that connect to the network
        edges = [edge for edge in edges if edge[1] not in network]

    if len(edges) == edges_to_cut:
        # we're done
        print(len(network) * (len(graph) - len(network)))
        break
