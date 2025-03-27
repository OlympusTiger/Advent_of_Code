from itertools import product
from collections import Counter
from copy import deepcopy
from more_itertools import flatten
from general import Neighbor, DeepIndex


# def adjacent(grid,p):
#     for i in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
#         if 0<=p[0]+i[0]<len(grid) and 0<=p[1]+i[1]<len(grid[0]):
#             yield grid[p[0]+i[0]][p[1]+i[1]]



def main(inp):
    # grid=[list(i) for i in inp.splitlines()]
    # print(len(grid),len(grid[0]))
    # for _ in range(10):
    #     grid_temp=deepcopy(grid)
    #     for p in product(range(len(grid)),range(len(grid[0]))):
    #         count=Counter(adjacent(grid_temp,p))
    #         if grid_temp[p[0]][p[1]]=='.':
    #             if count['|']>=3:
    #                 grid[p[0]][p[1]]='|'
    #         elif grid_temp[p[0]][p[1]]=='|':
    #             if count['#']>=3:
    #                 grid[p[0]][p[1]]='#'
    #         elif grid_temp[p[0]][p[1]]=='#':
    #             if count['#']<1 or count['|']<1:
    #                 grid[p[0]][p[1]]='.'
    
    # t=Counter(flatten(grid))['|']
    # l=Counter(flatten(grid))['#']
    # print(t,l)

    grid=[list(i) for i in inp.splitlines()]
    grid=DeepIndex(grid)
    passed=[]
    for i in range(1000000000):
        grid_temp=deepcopy(grid)
        
        for p in product(range(grid.length[0]),range(grid.length[1])):
            count=Counter(Neighbor(grid_temp,p,diagonal=True).neighbors())
           
            if grid_temp(p[0],p[1])=='.':
                if count['|']>=3:
                    grid.set_value('|',p[0],p[1])
            elif grid_temp(p[0],p[1])=='|':
                if count['#']>=3:
                    grid.set_value('#',p[0],p[1])
            elif grid_temp(p[0],p[1])=='#':
                if count['#']<1 or count['|']<1:
                    grid.set_value('.',p[0],p[1])
        
        s=Counter(flatten(grid.d))['|']*Counter(flatten(grid.d))['#']

        if s in passed:
            ind=passed.index(s)
            if passed[ind-1]==passed[i-1]:
                period=i-ind
                start=i-period-1
                break
        passed.append(s)
    p=passed[ind-1:i-1]
    c=(1000000000-start-1)%period



    return p[c],None
                    