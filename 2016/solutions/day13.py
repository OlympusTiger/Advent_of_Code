import networkx as nx
from itertools import product
from functools import cache
from networkx.algorithms import dijkstra_path_length,single_source_shortest_path

@cache
def cell(x,y):
    s=x**2+3*x+2*x*y+y+y**2
    s+=1352
    return bin(s)[2:].count('1')%2==0





def main(inp):
    G=nx.Graph()
    for i,j in product(range(50),repeat=2):
        if cell(i,j):
            if cell(i-1,j) and i-1>=0:
                G.add_edge((i,j),(i-1,j))
            if cell(i+1,j):
                G.add_edge((i,j),(i+1,j))
            if cell(i,j-1) and j-1>=0:
                G.add_edge((i,j),(i,j-1))
            if cell(i,j+1):
                G.add_edge((i,j),(i,j+1))
    

    return dijkstra_path_length(G,(1,1),(31,39)),len(single_source_shortest_path(G,(1,1),cutoff=50))