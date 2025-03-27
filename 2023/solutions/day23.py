from collections import defaultdict
from general import Grid
from itertools import product
from collections import defaultdict

lst={(0,1):'>',(0,-1):'<',(1,0):'v',(-1,0):'^'}
cache={}
def get_neighbs(grid,pos):
    if pos in cache:
        return cache[pos]
    
    cac=list(grid.neighbours(pos,get_values=True,get_direction=True,filter_value=["#"]))
    cache[pos]=cac
    return cac

def get_nodes(grid,possible,start,d):
    nxt=grid.move(start,d)
    q=[(1,nxt)]
    
    seen={start}
    while q:
        s,p=q.pop()
        if p in possible:

            return start,p,s
        for n,_,d in get_neighbs(grid,p):
            if n not in seen:
                seen.add(n)
                q.append((s+1,n))



def dfs(start,end,adjency_map):
    q=[(0,start,{start})]
    longest=0
 
    while q:
        steps,p,seen=q.pop()
        if p==end:
            longest=max(longest,steps)
            continue
        for n,s in adjency_map[p]:
            if n not in seen:
                q.append((steps+s,n,seen|{n}))
    return longest
           
    



def hiking(grid,start,end,part2=False):
    possible=[start,end]
    for p in product(range(grid.height), range(grid.width)):
        if p==end:
            continue
        if grid[p]=='.':
            neighbs=get_neighbs(grid,p)
            l=len(neighbs)
            if l>2:
                possible.append(p)

    nodes=[]
    for p in possible:
        for n,v,d in get_neighbs(grid,p):
            if lst[d]==v or p==start:
                nodes.append(get_nodes(grid,possible,p,d))


    adjency_map=defaultdict(list)
    for n in nodes:
        adjency_map[n[0]].append((n[1],n[2]))
        if part2:
            adjency_map[n[1]].append((n[0],n[2]))

    

    return dfs(start,end,adjency_map)



    
            


def main(inp):
    grid=Grid.from_txt_file(inp)

    for i in range(grid.width):
        if grid[0,i]=='.':
            start=(0,i)
        if grid[grid.width-1,i]=='.':
            end=(grid.width-1,i)

    







    return hiking(grid,start,end),hiking(grid,start,end,part2=True)
                    