import networkx as nx
import  matplotlib.pyplot as plt


def main(inp):
    dic={}
    weights={}
    for i in inp.splitlines():
        if '->' in i:
            
            a,b=i.split(' -> ')
            x,y=a.split()
            weights[x]=int(y[1:-1])
            dic[tuple(a.split())]=b.split(', ')
        else:
            x,y=i.split()
            weights[x]=int(y[1:-1])
 
    G=nx.Graph()
    for i in dic:
        for j in dic[i]:

            G.add_edge(i[0],j)
    centr=nx.betweenness_centrality(G)
    root=max(centr,key=lambda x:centr[x])

    # ro='tknk'
    for i in G.nodes:
        G.nodes[i]['weight']=weights[i]

    T=nx.dfs_tree(G,root)
    connections=nx.dfs_successors(T)
    starting=weights.copy()
    sums={}
    for c in  list(connections.keys())[::-1]:
        s=[weights[i] for i in connections[c]]
        if all(x==s[0] for x in s):
            weights[c]+=sum(s)
        else:

            d=min(connections[c],key=lambda x:s.count(weights[x]))
            diff=max(s,key=lambda x:s.count(x))-min(s,key=lambda x:s.count(x))
            print(d)
            break
    


    return root,starting[d]+diff
                