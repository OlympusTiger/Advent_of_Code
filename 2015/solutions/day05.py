from re import sub
from itertools import pairwise

def con1(s):
    return sub('[aeiou]','0',s).count('0')>=3
def con2(s):
    return any(s[i]==s[i+1] for i in range(0,len(s)-1))
def con3(s):
    return not any(p in s for p in ['ab','cd','pq','xy'])
def con4(s):
    return any(s.count(''.join(i))>=2 for i in pairwise(s))
def con5(s):
    return any(s[i]==s[i+2] for i in range(0,len(s)-2))

def main(inp):
    p1=p2=0
    for s in inp.splitlines():   
        p1+=con1(s) and con2(s) and con3(s)
        p2+=con4(s) and con5(s)
       
    return p1,p2