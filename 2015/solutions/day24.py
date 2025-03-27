from itertools import permutations
from functools import reduce
from operator import mul
def search(gifts,parts):
    w=sum(gifts)/parts
    groups=[]
    for i in range(len(gifts)):
        if groups:
            return min(groups)
        for p in permutations(gifts,i):
            if sum(p)==w:
                groups.append(reduce(mul,p))



def main(inp):
    gifts=list(map(int,inp.splitlines()))
    
    return search(gifts,3),search(gifts,4)