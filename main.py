from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        print("frontier", frontier)
        node = frontier.pop()
        print("visiting", node)
        result.add(node)
        for i in graph[node]:
          if i not in result:
            frontier.add(i) 
    return result





def connected(graph):
    nodes = len(graph)
    reach = reachable(graph, list(graph.keys())[0])
    return len(reach) == nodes



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    results = []
    visit = set(list(graph.keys()))
    while len(visit) > 0:
      node = visit.pop()
      results.append(node)
      visit -= reachable(graph, node)
    return len(results)

