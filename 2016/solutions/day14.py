from hashlib import md5
import re
from functools import cache

@cache
def hashing(inp, n, t):
    s=inp+str(n)
    md=md5(s.encode()).hexdigest()
    for _ in range(t):
        md=md5(md.encode()).hexdigest()

    f3=re.findall(r'(\w)\1\1',md)
    f5=re.findall(r'(\w)\1\1\1\1',md)
    return (f3,f5)


def start(inp,t):
    n=0
    i=-1
    while n<64:
        i+=1
        f3=hashing(inp,i,t)[0]
        
        if f3:

            if any(f3[0] in hashing(inp,j,t)[1] for j in range(i+1,i+1000)):
                n+=1
    return i

def main(inp):

        
        
    



    return start(inp,0),start(inp,2016)
