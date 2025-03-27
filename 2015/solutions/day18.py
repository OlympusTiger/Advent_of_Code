from itertools import product


def adjent(a,b,grid,n):
	s=0
	for i,j in product([-1,0,1],repeat=2):
		if (i,j)!=(0,0) and 0<=a+i<n and 0<=b+j<n:			
			s+=grid[a+i][b+j]				
	return s

def switch(grid,n,steps,part2):
    
    if part2:
        corners=[(0,0),(0,n-1),(n-1,0),(n-1,n-1)]
        for s in corners:
            grid[s[0]][s[1]]=1
        
    while steps>0:
        new=[[0 for _ in range(n)]for _ in range(n)]
        for i,j in product(range(n),repeat=2):	
            if part2 and (i,j) in corners:
                new[i][j]=1
                continue

            match grid[i][j]:
                 
                case 1 if adjent(i,j,grid,n)in [2,3]:
                    new[i][j]=1

                case 0 if adjent(i,j,grid,n)==3:
                    new[i][j]=1

        grid=new.copy()
        steps-=1
        
        
    return sum(map(sum,grid))
	



def main(inp):
    grid=[[0 if x=='.'else 1 for x in l.strip('\n')]for l in inp.splitlines()]
    n=100
    steps=100
    return switch(grid,n,steps,False),switch(grid,n,steps,True)