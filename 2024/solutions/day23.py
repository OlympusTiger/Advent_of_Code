import networkx as nx

def main(input_data):
    edge_pairs = [line.split('-') for line in input_data.splitlines()]

    graph = nx.Graph()
    graph.add_edges_from(edge_pairs)
    for node in graph.nodes:
        graph.nodes[node]['weight'] = 1

    triad_count = 0
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3 and any(node.startswith('t') for node in clique):
            triad_count += 1
        if len(clique) > 3:
            break

    max_clique_nodes, _ = nx.max_weight_clique(graph)
    max_clique_sorted = ','.join(sorted(max_clique_nodes))

    return triad_count, max_clique_sorted
