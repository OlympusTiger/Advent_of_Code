from general import Grid 
from heapq import heappush,heappop


def crucible(grid,start,end,maxim=3,minim=0):
    state=(0,start,None,0)
    q=[state]
    seen=set()
    while q:
        loss,pos,dir,consecutive=heappop(q)
        if pos==end:
            return loss
        if (pos,dir,consecutive) in seen:
            continue
        seen.add((pos,dir,consecutive))
        for nxt,v,d in grid.neighbours(pos,get_values=True,get_direction=True,filter_dir=[(-dir[0],-dir[1])] if dir else []):
            if d==dir or dir is None:
                if consecutive==maxim:
                    continue
                heappush(q,(loss+int(v),nxt,d,consecutive+1))
            else:
                if consecutive>=minim:
                    heappush(q,(loss+int(v),nxt,d,1))

def main(inp):
    grid=Grid.from_txt_file(inp)
    start = (0,0)
    end = (grid.height-1,grid.width-1)

    return crucible(grid,start,end),crucible(grid,start,end,minim=4,maxim=10)
                    