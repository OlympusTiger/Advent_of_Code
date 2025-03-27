import networkx as nx


def main(inp):
    orbits = inp.splitlines()
    G = nx.DiGraph()
    H = nx.Graph()
    pairs = set()

    for orbit in orbits:
        a,b = orbit.split(')')
        G.add_edge(a,b)
        H.add_edge(a,b)
        if b == 'YOU':
            s = a
        if b == 'SAN':
            t = a
    for n in G.nodes:
        for i in list(nx.dfs_postorder_nodes(G,n))[:-1]:
            pairs.add((n,i))


    return len(pairs),nx.shortest_path_length(H,s,t)
                    