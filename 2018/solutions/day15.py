import networkx as nx
from collections import defaultdict
from itertools import product
from copy import deepcopy

def adjacent(grid,x,y,filt):
    for i,j in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]:
        if grid[i][j] not in filt:   
            yield i,j


def id(x,y,units):
    for z in units:
        if units[z]['p']==(x,y):
            return z

def if_reachable(grid,A,a,b):
    try:
        min_path_length=nx.shortest_path_length(A,a,b)
        for p in adjacent(grid,a[0],a[1],'#GE'):
            if (z:=nx.shortest_path_length(A,p,b))==min_path_length-1:
                return min_path_length,p
    except nx.NetworkXNoPath:
        return


def remove_dead(grid,units,foes,n,ind):
    foes.remove(units[n]['p'])
    v,b=units[n]['p']
    grid[v][b]='.'
    lst=list(units.keys())
    sd=lst.index(n)
    if sd>ind:
        ind+=1
    del units[n]

    return grid,units,foes,ind

def target_in_range(grid,units,n,foes):
    targets=[]
    for i,j in adjacent(grid,units[n]['p'][0],units[n]['p'][1],'#'):
        if (i,j) in foes:
            targets.append(id(i,j,units))
    return targets

def attack(grid,units,foes,targets,ind,ad=3):
    targets.sort(key=lambda x:(units[x]['hp'],units[x]['p']))
    target=targets[0]
    units[target]['hp']-=ad
    if units[target]['hp']<=0:
        grid,units,foes,ind=remove_dead(grid,units,foes,target,ind)
    else:
        ind+=1
    return grid,units,foes,ind


def move(grid,units,G,n,friends,foes,ind):
    
    sub=[i  for i in G.nodes if i==units[n]['p'] or i not in friends+foes]
    target_locations=[]
    T=nx.subgraph(G,sub)
    for i in foes:
        for j in adjacent(grid,i[0],i[1],'#EG'):
            exist_path=if_reachable(grid,T,units[n]['p'],j)
            if exist_path:
                length,p=exist_path
                target_locations.append([length,j,i,p])
    
    if not target_locations:
        return grid,units,friends,foes,ind+1
    
    m=min(target_locations)
    length,j,i,p=m
    l=p
    if length==1:
        ids=id(i[0],i[1],units)
        
        if units[ids]['hp']<=0:
            grid,units,foes,ind=remove_dead(grid,units,foes,ids,ind)
    else:
        ind+=1
    
    friends.remove(units[n]['p'])
    grid[units[n]['p'][0]][units[n]['p'][1]]='.'
    units[n]['p']=l
    grid[l[0]][l[1]]=n[0].upper()
    friends.append(l)

    return grid,units,friends,foes,ind

def rounds(grid,units,G,r,k):
    
    e_loc=list(map(lambda x:x[1]['p'],filter(lambda y:'e' in y[0],units.items())))
    g_loc=list(map(lambda x:x[1]['p'],filter(lambda y:'g' in y[0],units.items())))
   
    ind=0
    while ind<len(units):

        if not e_loc or not g_loc:
            return grid,G,units,False,r,len(e_loc)
        
        n=list(units.keys())[ind]
        
        if 'g' in n:
            targets=target_in_range(grid,units,n,e_loc)
            if targets:
                grid,units,e_loc,ind=attack(grid,units,e_loc,targets,ind)  
            else:
                grid,units,g_loc,e_loc,ind=move(grid,units,G,n,g_loc,e_loc,ind)   

        elif 'e' in n:
            targets=target_in_range(grid,units,n,g_loc)
            if targets:
                grid,units,g_loc,ind=attack(grid,units,g_loc,targets,ind,ad=k)
            else:
                grid,units,e_loc,g_loc,ind=move(grid,units,G,n,e_loc,g_loc,ind)
                
    r+=1
    if not g_loc or not e_loc: 
        return grid,G,units,False,r,len(e_loc)
    
    return grid,G,units,True,r,len(e_loc)


def main(inp):
    grid=[list(i) for i in inp.splitlines()]
    units=defaultdict(lambda:{'p':(0,0),'hp':200})
    e=0
    g=0
    G=nx.Graph()
    for i,j in product(range(len(grid)),range(len(grid[0]))):
            if grid[i][j]=='E':
                e+=1
                units[f'e{e}']['p']=(i,j)
                
            elif grid[i][j]=='G':
                g+=1
                units[f'g{g}']['p']=(i,j)
                
    units=dict(sorted(units.items(),key=lambda x: x[1]['p']))

    for i,j in product(range(len(grid)),range(len(grid[0]))):
         if grid[i][j]!='#':
              for x,y in adjacent(grid,i,j,'#'):
                    G.add_edge((i,j),(x,y))
    
    fight=True
    k=2
    elfs=0
    
    while elfs<e:
        k+=1
        r=0
        fight=True
       
        dgrid=deepcopy(grid)
        dunits=deepcopy(units)
        dG=deepcopy(G)
        while fight:
            
            dgrid,dG,dunits,fight,r,elfs=rounds(dgrid,dunits,dG,r,k)
            
            dunits=dict(sorted(dunits.items(),key=lambda x: x[1]['p']))

    res=r*sum(map(lambda x:dunits[x]['hp'],dunits))    
   
    return res,None
                    

