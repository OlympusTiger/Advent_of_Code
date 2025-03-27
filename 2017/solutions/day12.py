import networkx as nx

def main(inp):
    pipes={int(i.split(' <-> ')[0]):list(map(int,i.split(' <-> ')[1].split(', '))) for i in inp.splitlines()}
    G=nx.Graph(pipes)
    p1=nx.node_connected_component(G,0)
    p2=list(nx.connected_components(G) ) 


    return len(p1),len(p2)
                