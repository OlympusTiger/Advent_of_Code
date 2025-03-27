from itertools import product
import networkx as nx

def add_doors(grid,current,d):
    
    if d=='N':  
        grid[current[0]-1][current[1]]='-'
        grid[current[0]-2][current[1]]='.'
        current=(current[0]-2,current[1])
    elif d=='S':  
        grid[current[0]+1][current[1]]='-'
        grid[current[0]+2][current[1]]='.'
        current=(current[0]+2,current[1])
    elif d=='E': 
        grid[current[0]][current[1]+1]='|'
        grid[current[0]][current[1]+2]='.'
        current=(current[0],current[1]+2)
    elif d=='W':  
        grid[current[0]][current[1]-1]='|'
        grid[current[0]][current[1]-2]='.'
        current=(current[0],current[1]-2)
    return grid,current

def find_options(grid,current,i,directions):
    c=1
    while directions[i:c+i].count('(')!=directions[i:c+i].count(')'):
        c+=1
    options=directions[i+1:i+c-1]
    or_loc=[i for i in range(len(options)) if options[i]=='|']
    x=0
    k=0
    routes=[]
    while x<len(or_loc):
        o=or_loc[x]
        if options[k:o].count('(')==options[k:o].count(')'):
            routes.append(options[k:o])
            k=o+1
        x+=1
    routes.append(options[k:])
    
    for r in routes:
        if r:
            grid=travel(grid,r,current)
    i=i+c
    return grid,current,i


def travel(grid,directions,current):
    i=0
    while i<len(directions):
        d=directions[i]
        if d=='(':
            grid,current,i=find_options(grid,current,i,directions)
        else:
            grid,current=add_doors(grid,current,d)
            i+=1
    
    return grid

def main(inp):
    directions=inp[1:-1]
    #directions='WNE'
    #directions='ENWWW(NEEE|SSE(EE|N))'
    #directions='ENNWSWWNEWSSSSEENWNSEEESWENNNN'
    #directions='ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN'
    #directions='ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))'
    #directions='WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))'

    n=directions.count('N')
    s=directions.count('S')
    e=directions.count('E')
    w=directions.count('W')
    h=2*(s+n)
    w=2*(w+e)
    grid=[['?'for _ in range(w)]for _ in range(h)]
    start=(h//2,w//2) 
    grid[start[0]][start[1]]='x'
    current=start
    grid=travel(grid,directions,current)
    
    G=nx.Graph()
    for p in product(range(h),range(w)):
        if grid[p[0]][p[1]] in '.|-':
            for k in [(-1,0),(1,0),(0,-1),(0,1)]:
                try:
                    if grid[p[0]+k[0]][p[1]+k[1]]!='?':
                        G.add_edge(p,(p[0]+k[0],p[1]+k[1]))
                except IndexError:
                    pass

    s=nx.single_source_shortest_path_length(G,start)
    
    p=(max(s.items(),key=lambda x: x[1]))
    print(p)
    f=0
    for i in s.values():
        if i%2==0 and i/2>=1000:
            f+=1
  
    return p[1]/2,f
