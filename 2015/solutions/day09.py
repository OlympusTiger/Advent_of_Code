import networkx as nx


def main(inp):
    distances=[(i.replace(' to ',' = ').split(' = ')) for i in inp.splitlines()]
    
    distances=[(x[0],x[1],int(x[2])) for x in distances]
    
    G=nx.Graph()
    G.add_weighted_edges_from(distances)
    l=len(G.nodes)
    paths=[]
    for n in G.nodes:
        d=list(G.nodes)
        d.remove(n)
        for p in nx.all_simple_paths(G,source=n,target=d):


            
            if len(p)==l:
                paths.append(nx.path_weight(G,p,weight='weight'))


    return min(paths), max(paths)