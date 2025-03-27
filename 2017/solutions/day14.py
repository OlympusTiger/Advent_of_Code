import sys
sys.path.append('2017\solutions')
from day10 import knot_hash

from itertools import product
import networkx as nx
from time import sleep

def adjacent(x,y,grid):
    if x-1>=0:
        yield x-1,y
    if x+1<len(grid):
        yield x+1,y
    if y-1>=0:
        yield x,y-1
    if y+1<len(grid[0]):
        yield x,y+1


# def blocks(grid):
#     k=1
#     for i,j in product(range(len(grid)),repeat=2):
#         if grid[i][j]=='#':
#             for x,y in adjacent(i,j,grid):
#                 if grid[x][y]=='#':
                  


def blocks(grid):
    G=nx.Graph()
    alone=0
    for i,j in product(range(128),repeat=2):
        is_alone=True
        if grid[i][j]=='#':
            for x,y in adjacent(i,j,grid):
                if grid[x][y]=='#':
                    is_alone=False
                    G.add_edge((i,j),(x,y))
            if is_alone:
                alone+=1
    
    return nx.number_connected_components(G)+alone



def main(inp):

    grid=[]
    s=0
    for i in range(128):
        conv=map(lambda x:bin(int(x,16))[2:].zfill(4),knot_hash(inp+'-'+str(i)))
        row=''.join(conv)
        s+=row.count('1')
        grid.append(list(map(lambda x:'#' if x=='1' else '.',row)))
    

        


    return s,blocks(grid)
                