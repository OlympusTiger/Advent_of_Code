from general import Grid
from collections import deque


def walk(raw_grid,expand=1,max_steps=64):

    raw_grid = '\n'.join(('\n'.join(x*expand for x in raw_grid.splitlines()))for _ in range(expand))  #expansion(or initial) grid
    grid = Grid.from_txt_file(raw_grid)
    start = grid._find('S')[expand**2//2]  #get the mid starting point

    locs = 0
    q = deque([(0,start)])
    seen = {start}
    while q:
        steps,p=q.popleft()
        if steps%2==max_steps%2:
            locs+=1
        if steps == 131*(expand//2)+max_steps:  # max steps to reach the edge
            continue      
        for n in grid.neighbours(p,filter_value=['#']):
            if n[0] not in seen:
                seen.add(n[0])
                q.append((steps+1,n[0]))

    return locs


def part2(raw_grid):
    max_steps=26501365
    first_values=[]
    for i in [1,3,5]:#expansion multipliers (1 for start, 3 for the next 3*3 grid ...)
        first_values.append(walk(raw_grid,expand=i,max_steps=65))  # possible positions for its expansion
    expansion_table=[4,8]
    mul1=(first_values[1]-first_values[0])/expansion_table[0]  #the 2 constant alternating multipliers
    mul2=(first_values[2]-first_values[1])/expansion_table[1]

    infinite_grid_limit=(max_steps-65)//131
    for i in range(infinite_grid_limit+1):
        if i==0:
            res=first_values[0]
        elif i%2==1:
            res+=mul1*(i*4)
        else:
            res+=mul2*(i*4)
    return int(res)


def main(inp):      

        

    return walk(inp),part2(inp)
                   