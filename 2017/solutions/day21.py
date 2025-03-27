import numpy as np
from functools import cache

def flip_rorate(g):


    return [np.rot90(g,i) for i in range(4)]+[np.flip(g,1)]+[np.flip(g,0)]+[np.flip(np.rot90(g,i),1) for i in range(4)]+[np.flip(np.rot90(g,i),0) for i in range(4)]

@cache
def find_match(grid,s):
    grid=np.frombuffer(grid,dtype=np.int32).reshape(s,s)
    for o in range(len(origin)):

        if any(np.array_equal(grid,arr)for arr in origin[o]):


            return output[o]




def pixels(grid,origin,output,size):
    
    if size%2==0:
        s=2
        subgrids=grid.reshape(size//2,2,size//2,2).swapaxes(1, 2)
    else:
        s=3
        subgrids=grid.reshape(size//3,3,size//3,3).swapaxes(1, 2)
    subg=[]
    for i in range(size//s):
        sub=[]
        for j in range(size//s):
            gr=subgrids[i][j].tobytes()
            sub.append(find_match(gr,s))

        subg.append(np.concatenate(sub,axis=1))
      

    return np.concatenate(subg,axis=0)


def iterations(grid,times):
    size=len(grid)
    for _ in range(times):  #(or 5 for part 1)
        grid=pixels(grid,origin,output,size)
        size=len(grid)
    return np.count_nonzero(grid)

def main(inp):
    global origin,output
    initial='''.#.
..#
###'''
    origin=[]
    output=[]
    for r in inp.splitlines():
        r1,r2=r.split(' => ')
        a=np.array([[1 if i=='#' else 0 for i in j]for j in r1.split('/')])
        origin.append(flip_rorate(a))
        output.append(np.array([[1 if i=='#' else 0 for i in j]for j in r2.split('/')]))


    grid=np.array([[1 if i=='#' else 0 for i in j]for j in initial.splitlines()])


    


    return iterations(grid.copy(),5),iterations(grid,18)
                