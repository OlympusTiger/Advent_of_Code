from math import sqrt


def neighbors(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
    ]


def circle(n, c, x=0, y=0, i=1, sq={(0, 0): 1}):
    if max(sq.values()) > n:
        return max(sq.values())

    if c == 'r':
        if x + 1 <= i:
            exist = set(neighbors(x + 1, y)).intersection(sq)
            sq[(x + 1, y)] = sum(sq[e] for e in exist)
            return circle(n, 'r', x + 1, y, i, sq)
        elif (x, y + 1) in sq:
            return circle(n, 'r', x, y, i + 1, sq)
        else:
            return circle(n, 'u', x, y, i, sq)

    if c == 'u':
        if y + 1 <= i:
            exist = set(neighbors(x, y + 1)).intersection(sq)
            sq[(x, y + 1)] = sum(sq[e] for e in exist)
            return circle(n, 'u', x, y + 1, i, sq)
        else:
            return circle(n, 'l', x, y, i, sq)

    if c == 'l':
        if x - 1 >= -i:
            exist = set(neighbors(x - 1, y)).intersection(sq)
            sq[(x - 1, y)] = sum(sq[e] for e in exist)
            return circle(n, 'l', x - 1, y, i, sq)
        else:
            return circle(n, 'd', x, y, i, sq)

    if c == 'd':
        if y - 1 >= -i:
            exist = set(neighbors(x, y - 1)).intersection(sq)
            sq[(x, y - 1)] = sum(sq[e] for e in exist)
            return circle(n, 'd', x, y - 1, i, sq)
        else:
            return circle(n, 'r', x, y, i, sq)


def main(inp):
    n = int(inp.strip())
    x = int(sqrt(n))
    if x % 2 == 0:
        m = x + 1
        l = int(x / 2)
    else:
        m = x + 2
        l = int((x + 1) / 2)
    d = [i for i in range(l * 2, l - 1, -1)]
    d += d[:-2][::-1]
    i = (m ** 2 - n) % len(d)
    sq = {(0, 0): 1}
    return d[i % len(d)], circle(n, 'r')
from math import sqrt
from itertools import cycle
from time import sleep
def neighbors(x,y):
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]


def circle(n,c,x=0,y=0,i=1,sq={(0,0):1}):
    print(sq)
    #(1,0) (1,1) (0,1) (-1,1) (-1,0) (-1,-1) (0,-1) (1,-1)
    if max(sq.values())>n:
        return max(sq.values())
    
    
    if c=='r':
        
        if x+1<=i:
            
            exist=set(neighbors(x+1,y)).intersection(sq)
            sq[(x+1,y)]=0
            for e in exist:
                sq[(x+1,y)]+=sq[e]
            return circle(n,'r',x+1,y,i,sq)
        elif (x,y+1) in sq:
            
            return circle(n,'r',x,y,i+1,sq)
        else:
            return circle(n,'u',x,y,i,sq)

    if c=='u':
        if y+1<=i:
            exist=set(neighbors(x,y+1)).intersection(sq)
            sq[(x,y+1)]=0
            for e in exist:
                sq[(x,y+1)]+=sq[e]
            return circle(n,'u',x,y+1,i,sq)
        else:
            return circle(n,'l',x,y,i,sq)

    if c=='l':
        if x-1>=-i:
            exist=set(neighbors(x-1,y)).intersection(sq)
            sq[(x-1,y)]=0
            for e in exist:
                sq[(x-1,y)]+=sq[e]
            return circle(n,'l',x-1,y,i,sq)
        else:
            return circle(n,'d',x,y,i,sq)

    if c=='d':
        if y-1>=-i:
            exist=set(neighbors(x,y-1)).intersection(sq)
            sq[(x,y-1)]=0
            for e in exist:
                sq[(x,y-1)]+=sq[e]
            return circle(n,'d',x,y-1,i,sq)
        else:
            return circle(n,'r',x,y,i,sq)
    
        

def main(inp):

    n=int(inp.strip())
   
    x=int(sqrt(n))

    if x%2==0:
        m=x+1
        l=int(x/2)
    else:
        m=x+2
        l=int((x+1)/2)
    
    d=[i for i in range(l*2,l-1,-1)]
    d+=d[:-2][::-1]
    i=(m**2-n)%len(d)

    sq={(0,0):1}
    
    return d[i%len(d)],circle(n,'r')

