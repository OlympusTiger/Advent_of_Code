

def in_bounds(grid,x,y):
    return 0<=x<len(grid) and 0<=y<len(grid[0])


def all_diagonals(grid):
    top_edge=[(0,i) for i in range(len(grid[0]))]
    right_edge=[(i,len(grid[0])-1)for i in range(len(grid)) if i!=0]
    left_edge=[(i,0) for i in range(len(grid)) if i!=0]
    slash_lines=[]
    for i,j in top_edge+right_edge:
        x=0
        temp=[]
        while in_bounds(grid,i+x,j-x):
            temp.append(grid[i+x][j-x])
            x+=1
        slash_lines.append(temp)
    
    backslash_lines=[]
    for i,j in top_edge+left_edge:
        x=0
        temp=[]
        while in_bounds(grid,i+x,j+x):
            temp.append(grid[i+x][j+x])
            x+=1
        backslash_lines.append(temp)
    
    return slash_lines+backslash_lines


def xmas_count(grid):
    total_xmas=0
    for line in grid:
        total_xmas+=line.count('XMAS')+line[::-1].count('XMAS')

    for line in zip(*grid):
        line=''.join(line)
        total_xmas+=line.count('XMAS')+line[::-1].count('XMAS')
    
    for line in all_diagonals(grid):
       line=''.join(line)
       total_xmas+=line.count('XMAS')+line[::-1].count('XMAS')


    return total_xmas
   

def big_diagonals(grid):
    diag1=[grid[i][i] for i in range(len(grid))]
    diag2=[grid[i][len(grid)-i-1] for i in range(len(grid))]
    return diag1,diag2


def x_mas_count(grid):
    match_cases=[['M','A','S'],['S','A','M']]
    total_xmas=0
    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            square3x3=[[grid[i+k][j+l] for l in range(3)] for k in range(3)]
            diag1,diag2=big_diagonals(square3x3)
            if diag1 in match_cases and diag2 in match_cases:
                total_xmas+=1
    return total_xmas


def main(inp):
    grid=[i for i in inp.splitlines()]
    

    return xmas_count(grid),x_mas_count(grid)
                    