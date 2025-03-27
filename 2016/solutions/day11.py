import re
import heapq
from more_itertools import powerset
from copy import deepcopy



def do(f,i,x,l):
    l[f+i].extend(x)
    if any(a+'G' not in l[f+i] and 'G' in ''.join(l[f+i])for a in l[f+i]if 'G' not in a):
        return (0,0)
    for j in x:
        l[f].remove(j)
        if any(a+'G' not in l[f] and 'G' in ''.join(l[f])for a in l[f]if 'G' not in a):
            return (0,0)

    return (-len(l[3]),-len(l[2]),-len(l[1]),-len(l[0])),list(map(sorted,l))

def add_remove(f,l):
    for i in [1,-1]:
        if 0<=f+i<len(l):
            if any(0<len(l[a]) for a in range(f+i+1)):

                for x in powerset(l[f]):

                    if 0<len(x)<=2:
                        
                        yield (f+i,*do(f,i,x,deepcopy(l)))

    


def solve(building):
    
    
    queue=[]
    for i in add_remove(0,deepcopy(building)):
        if i[1]:
            
            #(steps,current_floor,grid)
            q=(1,)+i
            
            heapq.heappush(queue,q)
            

               
    explored={(0,tuple(map(tuple,map(lambda x:[1 if 'G' in i else 0 for i in x],building))))}
    print(explored)
    # sleep(10)
    while queue:
        print(len(queue))
     
        steps,current,_,floors=heapq.heappop(queue)

        if (current,tuple(map(tuple,map(lambda x:[1 if 'G' in i else 0 for i in x],floors)))) in explored:
            continue

        explored.add((current,tuple(map(tuple,map(lambda x:[1 if 'G' in i else 0 for i in x],floors)))))
        
        if current==3 and len(floors[3])==sum([len(i) for i in building]): 
            return steps
        
        for i in add_remove(current,deepcopy(floors)):
            if i[1]:
                
                heapq.heappush(queue,(steps+1,)+i)



def main(inp):
    parse=inp.splitlines()
    floors=[[] for i in range(4)]
    
    for i,p in enumerate(parse):
        chip=re.findall('\w+(?=-)',p)
        gen=re.findall('\w+(?=\sgen)',p)
        floors[i].extend([c for c in chip]+[g+'G' for g in gen])
        floors[i].sort()
    floors2=deepcopy(floors)
    floors2[0].extend(['elerium','dilithium','eleriumG','dilithiumG'])
    return solve(floors),solve(floors2)