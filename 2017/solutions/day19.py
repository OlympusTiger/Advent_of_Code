

def next_in_line(i, j, heading, grid):
    if grid[i + heading[0]][j + heading[1]] != ' ':
        return (i + heading[0], j + heading[1], (i, j))
    return


def change_heading(i, j, prev, grid):
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and \
           grid[i + x][j + y] != ' ' and (i + x, j + y) != prev:
            return (x, y)


def traverse(grid):
    for j in range(len(grid[0])):
        if grid[0][j] != ' ':
            i, j = 0, j
            break
    heading = (1, 0)
    word = ''
    steps = 1
    while next_in_line(i, j, heading, grid):
        steps += 1
        i, j, prev = next_in_line(i, j, heading, grid)
        if grid[i][j].isalpha():
            word += grid[i][j]
        elif grid[i][j] == '+':
            heading = change_heading(i, j, prev, grid)

    return word, steps


def main(inp):
    grid = [[i for i in j] for j in inp.splitlines()]
    p1, p2 = traverse(grid)
    return p1, p2

def next_in_line(i,j,heading,grid):
    if grid[i+heading[0]][j+heading[1]]!=' ':
        return i+heading[0],j+heading[1],(i,j)
    return

def change_heading(i,j,prev,grid):
    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i+x][j+y]!=' ' and (i+x,j+y)!=prev:
            return (x,y)

def traverse(grid):
    for j in range(len(grid[0])):
        if grid[0][j]!=' ':
            (i,j)=(0,j)
            break
    heading=(1,0)
    word=''
    steps=1
    while next_in_line(i,j,heading,grid):
        steps+=1
        i,j,prev=next_in_line(i,j,heading,grid)
        if grid[i][j].isalpha():
            word+=grid[i][j]
        elif grid[i][j]=='+':
            heading=change_heading(i,j,prev,grid)

    return word,steps

def main(inp):
    
    grid=[[i for i in j] for j in inp.splitlines()]
    p1,p2=traverse(grid)
    return p1,p2
 