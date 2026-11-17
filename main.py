
from collections import defaultdict


def make_undirected_graph(edge_list):
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    result = {start_node}
    frontier = {start_node}

    while frontier:
        node = frontier.pop()

        for neighbor in graph.get(node, set()):
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)

    return result


def connected(graph):
    if not graph:
        return True

    start_node = next(iter(graph))
    return len(reachable(graph, start_node)) == len(graph)


def n_components(graph):
    unvisited = set(graph.keys())
    count = 0

    while unvisited:
        start_node = next(iter(unvisited))
        component = reachable(graph, start_node)
        unvisited -= component
        count += 1

    return count

