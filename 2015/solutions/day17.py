from itertools import combinations

def calc(cont,n,liters,part2):
    total=0
    for i in range(1,n+1):
        for p in combinations(cont,i):
            if sum(p)==liters:
                if part2:
                    for p in combinations(cont,i):
                        if sum(p)==liters:
                                total+=1
                    return total
                total+=1
    return total
    

def main(inp):
    cont=[int(i) for i in inp.splitlines()]
    n=len(cont)
    liters=150
    

    return calc(cont,n,liters,False),calc(cont,n,liters,True)
