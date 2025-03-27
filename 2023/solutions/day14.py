from general import Grid
from itertools import pairwise


def tilt(line,length,rev=False): #False for north-east, True for south-west 
    rocks=[-1]+[i for i,x in enumerate(line) if x=='#']+[length]
    new=[]
    for i,j in pairwise(rocks):
        x=line[i+1:j].count('O')
        m=1
        if j==length:
            m=0
        new+=['O']*x+['.']*(j-i-1-x)+['#']*m
    return new

def load_calc(grid):
    load=0
    for i,r in enumerate(grid):
        load+=r.count('O')*(grid.height-i)
    return load

def start_tilting(grid,part1=True):
    loads=[]
    for zz in range(1000000000):

        l=len(loads)       
        for i in range(l):
            if (l-i)%2==0 and loads[i:i+(l-i)//2]==loads[i+(l-i)//2:] and l-i>2:
                breakpoint=(1000000000-i)%((l-i)/2)
                return loads[int(breakpoint+i-1)]

        for c in range(grid.width):
            new=tilt(grid.col(c),grid.height)
            for j in range(grid.height):
                grid[j,c]=new[j]
        if part1:
            return load_calc(grid)
        
        for r in range(grid.height):
            new=tilt(grid.row(r),grid.width,rev=True)
            for j in range(grid.width):
                grid[r,j]=new[j]

        for c in range(grid.width):
            new=tilt(grid.col(c)[::-1],grid.height,rev=True)[::-1]
            for j in range(grid.height):
                grid[j,c]=new[j]

        for r in range(grid.height):
            new=tilt(grid.row(r)[::-1],grid.width)[::-1]
            for j in range(grid.width):
                grid[r,j]=new[j]

        loads.append(load_calc(grid))

def main(inp):
    grid=Grid.from_txt_file(inp)


    return start_tilting(grid,part1=True),start_tilting(grid,part1=False)



                    