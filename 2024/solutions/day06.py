from itertools import product

HEADINGS=[(-1,0),(0,1),(1,0),(0,-1)]

def in_bounds(grid,p):
    return 0<=p[0]<len(grid) and 0<=p[1]<len(grid[0])

def move(pos,heading,m):
    return (pos[0]+m*heading[0],pos[1]+m*heading[1])

def guard_walk(grid,pos,h,passed,part2=False,place_obstacle=True):
    i,j=pos
    heading=HEADINGS[h%4]
    path=set()


    loops=0

    while in_bounds(grid,(i,j)):
        if part2 and ((i,j),h%4) in passed:
            return None,1
        if grid[i][j]=='#':
            i,j=move((i,j),heading,-1)
            h+=1
            heading=HEADINGS[h%4]
            
        else:
            path.add((i,j))
            passed.add(((i,j),h%4))
            if part2 and place_obstacle and in_bounds(grid,(nxt:=move((i,j),heading,1))):
                
                a,b=nxt         
                if grid[a][b]!='#' and nxt not in path:
                    
                    grid[a][b]='#'
                    _,l=guard_walk(grid,(i,j),h+1,passed.copy(),part2=True,place_obstacle=False)
              
                    loops+=l
                    grid[a][b]='.'
            i,j=move((i,j),heading,1)

        
    return len(path),loops




def main(inp):
    grid=[list(i) for i in inp.splitlines()]
    for i,j in product(range(len(grid)),repeat=2):
        if grid[i][j]=='^':
            start=(i,j)
            break
    


    return guard_walk(grid.copy(),start,0,set())[0],guard_walk(grid.copy(),start,0,set(),part2=True)[1]
                    