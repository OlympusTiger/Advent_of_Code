from collections import deque
from functools import reduce
def knot_hash(inp):
   
    lengths=list(map(ord,inp))+[17,31,73,47,23]
   
    lis=list(range(256))
    skip=0
    pos=0
    for _ in range(64):
        for l in lengths:
            if pos+l>=len(lis):
                r=pos+l-len(lis)
                lis=deque(lis)
                lis.rotate(-r)
                lis=list(lis)
                pos=pos-r
                lis=lis[:pos]+lis[pos:pos+l][::-1]+lis[pos+l:]
                lis=deque(lis)
                lis.rotate(r)
                lis=list(lis)
                pos=pos+r
            else:
                lis=lis[:pos]+lis[pos:pos+l][::-1]+lis[pos+l:]
                
            pos=(pos+l+skip)%len(lis)
            skip+=1
   
    dense=[]
    for i in range(16):
        dense.append(reduce(lambda x,y:x^y,lis[i*16:(i+1)*16]))
    
    return ''.join(map(lambda x:format(x,'02x'),dense))


def main(inp):
    lengths=list(map(int,inp.split(',')))
    lis=list(range(256))
   
    skip=0
    pos=0
    for l in lengths:
      
        if pos+l>=len(lis):
            r=pos+l-len(lis)
            lis=deque(lis)
            lis.rotate(-r)
            lis=list(lis)
            pos=pos-r
            lis=lis[:pos]+lis[pos:pos+l][::-1]+lis[pos+l:]
            lis=deque(lis)
            lis.rotate(r)
            lis=list(lis)
            pos=pos+r
        else:
            lis=lis[:pos]+lis[pos:pos+l][::-1]+lis[pos+l:]

        pos=(pos+l+skip)%len(lis)
        skip+=1
        


    return lis[0]*lis[1],knot_hash(inp)
                