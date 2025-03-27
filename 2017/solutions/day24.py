from collections import defaultdict
from copy import deepcopy

global allchains
allchains=[]

def search(p,mapss,chain):

    if not mapss[p]:
        
        allchains.append(chain)
        return
    for i in mapss[p]:
        
        m=deepcopy(mapss)
        m[p].remove(i)
        if i!=p:
            m[i].remove(p)
        search(i,m,chain+[int(i)])


def main(inp):
    components=[tuple(i.split('/')) for i in inp.splitlines()]
    maps=defaultdict(list)
    for i in components:
        maps[i[0]].append(i[1])
        if i[0]!=i[1]:
            maps[i[1]].append(i[0])
   
    chains=[]
    for a in maps['0']:
        
        m=deepcopy(maps)
        m['0'].remove(a)
        m[a].remove('0')
  
        search(a,m,[int(a)])

    
    max_l=len(max(allchains,key=lambda x:len(x)))
    longest_chains=[c for c in allchains if len(c)==max_l]
    s=map(lambda x:2*sum(x)-x[-1],allchains)
    s2=map(lambda x:2*sum(x)-x[-1],longest_chains)
    return max(s),max(s2)
                