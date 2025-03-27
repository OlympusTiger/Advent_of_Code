from itertools import product
from collections import defaultdict,deque
#____________________
#
#   ~1hour for part2
#
#____________________
headings=[(-1,0),(0,1),(1,0),(0,-1)]

def in_bounds(grid,p):
    return 0<=p[0]<len(grid) and 0<=p[1]<len(grid[0])

def move(pos,heading):
    return pos[0]+heading[0],pos[1]+heading[1]

def main(inp):
    grid=[list(i) for i in inp.splitlines()]
    for i,j in product(range(len(grid)),repeat=2):
        if grid[i][j]=='S':
            start=(i,j)
        elif grid[i][j]=='E':            
            end=(i,j)

    
    q=deque([(0,start)])
    seen=set()
    prev={}
    while q:
        steps,p=q.popleft()
        if p==end:   
            maxs=steps
            break
        seen.add(p)
        x,y=p
        for d in headings:
            i,j=move(p,d)
            if in_bounds(grid,(i,j)):
                if grid[i][j]!='#' and (i,j) not in seen:
                    prev[(i,j)]=p
                    q.append((steps+1,(i,j)))
    path=[end]
    a=end
    while a!=start:
        path.append(prev[a])
        a=prev[a]
    max_path=path[::-1]
    

    q=deque([(0,start,(True,None,None))])
    seen=set()
    times=[]
    while q: 
        steps,p,collision=q.popleft()
        b,c1,c2=collision
        if steps>maxs:
            continue
        b,c1,c2=collision
        if p==end:
            times.append(steps)
            continue
        if (p,collision) in seen:
            continue
        seen.add((p,(b,c1,c2)))
        for d in headings:
            i,j=move(p,d)
            if in_bounds(grid,(i,j)):
                if grid[i][j]!='#':
                    c=c2                 
                    if b==False:
                        if (i,j) in path and steps+1>max_path.index((i,j)):
                            continue
                        if c2==None:
                            c=(i,j)
                        remain=maxs-max_path.index((i,j))+1
                        times.append(steps+remain)
                        seen.add((p,(b,c1,c)))
                        continue
                    q.append((steps+1,(i,j),(True,None,None)))
                if b:
                    if grid[i][j]=='#':
                        q.append((steps+1,(i,j),(False,p,None)))

    save1=0
    for i in times:
            if maxs-i>=100:
                save1+=1

    #part2
    exit_walls=[]
    for i,j in path:
        for d in headings:
            x,y=move((i,j),d)
            if in_bounds(grid,(x,y)) and grid[x][y]=='#':
                exit_walls.append(((x,y),(i,j)))


    def manhattan(p1,p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


    dist=defaultdict(lambda :float('inf'))
    for p1, ex in product(path,exit_walls):
        _,p2=ex
        l=manhattan(p1,p2)
        if l>20:
            continue
        if path.index(p1)>path.index(p2):
            total=l+maxs-path.index(p1)+path.index(p2)
            if total>maxs:
                continue
            if total<dist[(p1,p2)]:
                dist[(p1,p2)]=total
        else:
            total=l+maxs-path.index(p2)+path.index(p1)
            if total>maxs:
                continue
            if total<dist[(p2,p1)]:
                dist[(p2,p1)]=total
        
    save2=0
    times=list(dist.values())
    for i in times:
        if maxs-i>=100:
            save2+=1

    print(save1,save2)
    return save1,save2
                    