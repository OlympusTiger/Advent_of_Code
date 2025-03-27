def ribbon(b):
    b.sort()
    return 2*sum(b[:2])+b[0]*b[1]*b[2]

def sides(b):
    x,y,z=b
    return 2*(x*y+x*z+y*z)+min(x*y,x*z,y*z)

def main(inp):
    boxes=[list(map(int,i.split('x'))) for i in inp.splitlines()]
    order1=0
    order2=0
    for b in boxes: 
        order1+=sides(b)
        order2+=ribbon(b)

    return order1,order2