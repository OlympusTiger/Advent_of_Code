from more_itertools import distribute
def nxt(d,p):
    return(d[0]+p[0],d[1]+p[1])
def Part1(inp,dir):
    houses={(0,0)}
    p=(0,0)
    for d in inp:
        p=nxt(dir[d],p)
        houses.add(p)
    return len(houses)


def Part2(inp,dir):
    houses={(0,0)}
    for x in distribute(2,inp):
        p=(0,0)
        for d in x:
            
            p=nxt(dir[d],p)
            houses.add(p)
    return len(houses)

    

def main(inp):
    dir={'>':(0,1),'^':(-1,0),'<':(0,-1),'v':(1,0)}


    return Part1(inp,dir),Part2(inp,dir)
