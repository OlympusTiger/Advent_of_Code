import networkx as nx
from itertools import product,permutations


def main(inp):

    grid=[[i for i in j] for j in inp.splitlines()]
    G=nx.Graph()
    for i,j in product(range(len(grid)),range(len(grid[0]))):
        if grid[i][j]!='#':
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i+x][j+y]!='#':
                    G.add_edge((i,j),(i+x,j+y),weight=1)
   
    loc=[]
    for i in G.nodes:
        if grid[i[0]][i[1]]=='0':
            start=i
        if grid[i[0]][i[1]]!='.':
            loc.append(i)

  
    R=nx.Graph()
    for i,j in permutations(loc,2):
        p=nx.shortest_path_length(G,i,j)
        R.add_edge(i,j,weight=p)
 
    p=[]
    for i in R.nodes:
        for j in nx.all_simple_paths(R,start,i):
            if len(j)==len(R.nodes):
                p.append(nx.path_weight(R,j,weight='weight'))

    v=[]
    x=nx.simple_cycles(R)
    for j in x:
        if len(j)==len(R.nodes):
            j.append(j[0])
            v.append(nx.path_weight(R,j,weight='weight'))



    


    return min(p),min(v)


