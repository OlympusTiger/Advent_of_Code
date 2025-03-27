from itertools import combinations
from collections import defaultdict
import networkx as nx
def main(inp):
    points=[tuple(map(int,i.split(',')))for i in inp.splitlines()]
    connections=defaultdict(list)
    for a,b in combinations(points,2):
        if sum([abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]),abs(a[3]-b[3])])<=3:
            connections[a].append(b)
        else:
            connections[a]
    
    G=nx.Graph(connections)


      


    return nx.number_connected_components(G),None
                    