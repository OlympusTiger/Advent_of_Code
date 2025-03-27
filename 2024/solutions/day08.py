from itertools import product,combinations
from collections import defaultdict

def in_bounds(grid,x,y):
    return 0<=x<len(grid) and 0<=y<len(grid[0])

def part1(grid,a,b,dx,dy):
    valid=[]

    p1=(a[0]+dx,a[1]+dy)
    if in_bounds(grid,p1[0],p1[1]):
        valid.append(p1)
    p2=(b[0]-dx,b[1]-dy)
    if in_bounds(grid,p2[0],p2[1]):
        valid.append(p2)
    return valid

def part2(grid,a,b,dx,dy):
    valid=[]
    d1=d2=True
    m=0
    while d1 or d2:
        p1=(a[0]+m*dx,a[1]+m*dy)
        if d1:=in_bounds(grid,p1[0],p1[1]):
            valid.append(p1)
        p2=(a[0]-m*dx,a[1]-m*dy)
        if d2:=in_bounds(grid,p2[0],p2[1]):
            valid.append(p2)
        m+=1

    return valid

    

def main(inp):
    grid=[list(i) for i in inp.splitlines()]
    antennas=defaultdict(list)
    for i,j in product(range(len(grid)),repeat=2):
        if grid[i][j]!='.':
            antennas[grid[i][j]].append((i,j))
    antinodes1=set()
    antinodes2=set()
    for antenna in antennas:
        for i,j in combinations(antennas[antenna],2):
            dx=i[0]-j[0]
            dy=i[1]-j[1]
            antinodes1.update(part1(grid,i,j,dx,dy))
            antinodes2.update(part2(grid,i,j,dx,dy))
            


    return len(antinodes1),len(antinodes2)
                    