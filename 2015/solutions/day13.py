import re
import networkx as nx



def graph_with_me(G):
    for n in list(G.nodes()):
        G.add_weighted_edges_from([('me',n,0),(n,'me',0)])
    paths=[]
    c=nx.simple_cycles(G)
    for i in c:
        if len(i)==len(G.nodes):
            i.append(i[0])
            paths.append(nx.path_weight(G,i,weight='weight')+nx.path_weight(G,i[::-1],weight='weight'))
    
    return max(paths)
def graph(G):
    paths=[]

    c=nx.simple_cycles(G)
    for i in c:
        if len(i)==len(G.nodes):
            i.append(i[0])
            paths.append(nx.path_weight(G,i,weight='weight')+nx.path_weight(G,i[::-1],weight='weight'))
    
    return max(paths)

def main(inp):
    connections=[re.sub('lose ','-',x)for x in inp.splitlines()]
    connections=[re.findall('^\w+|\w+(?=\.)|-?\d+',x) for x in connections]
    G=nx.MultiDiGraph()
    G.add_weighted_edges_from(list(map(lambda x:(x[0],x[2],int(x[1])),connections)))


    return graph(G),graph_with_me(G)