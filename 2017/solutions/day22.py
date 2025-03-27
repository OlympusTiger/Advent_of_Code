from copy import deepcopy


    
def travel2(grid,current):

    infected=0
    headings=[(-1,0),(0,1),(1,0),(0,-1)]
    heading=(-1,0)
    for _ in range(10000000):     # 0:clean,  2:weakened, 1:infected, 3:flagged
        if grid[current[0]][current[1]]==0:

            heading=headings[(headings.index(heading)-1)%4]
            grid[current[0]][current[1]]=2

        elif grid[current[0]][current[1]]==2:
            grid[current[0]][current[1]]=1
            infected+=1
        elif grid[current[0]][current[1]]==1:
            heading=headings[(headings.index(heading)+1)%4]
            grid[current[0]][current[1]]=3
        else:
            heading=(-heading[0],-heading[1])
            grid[current[0]][current[1]]=0

        current=(current[0]+heading[0],current[1]+heading[1])
        if current[0]<0:
            grid.insert(0,[0 for i in range(len(grid[0]))])
            current=(0,current[1])
        if current[0]>=len(grid):
            grid.append([0 for i in range(len(grid[0]))])
            current=(len(grid)-1,current[1])
        if current[1]<0:
            for i in range(len(grid)):
                grid[i].insert(0,0)
            current=(current[0],0)
        if current[1]>=len(grid[0]):
            for i in range(len(grid)):
                grid[i].append(0)
            current=(current[0],len(grid[0])-1)


    return infected
def travel(grid,current):
  
    infected=0
    headings=[(-1,0),(0,1),(1,0),(0,-1)]
    heading=(-1,0)
    for _ in range(10000):
        
        if grid[current[0]][current[1]]==1:
       
            heading=headings[(headings.index(heading)+1)%4]
           
            grid[current[0]][current[1]]=0
        else:
            heading=headings[(headings.index(heading)-1)%4]
            grid[current[0]][current[1]]=1
            infected+=1

        current=(current[0]+heading[0],current[1]+heading[1])

        if current[0]<0:
            grid.insert(0,[0 for i in range(len(grid[0]))])
            current=(0,current[1])
        if current[0]>=len(grid):
            grid.append([0 for i in range(len(grid[0]))])
            current=(len(grid)-1,current[1])
        if current[1]<0:
            for i in range(len(grid)):
                grid[i].insert(0,0)
            current=(current[0],0)
        if current[1]>=len(grid[0]):
            for i in range(len(grid)):
                grid[i].append(0)
            current=(current[0],len(grid[0])-1)

    
    return infected

def main(inp):
    grid=[[1 if i=='#' else 0 for i in j] for j in inp.splitlines()]
    center=(len(grid)//2,len(grid[0])//2)
    grid2=deepcopy(grid)
        


    return travel(grid,center),travel2(grid2,center)
                