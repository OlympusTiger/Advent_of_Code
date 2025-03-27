from sympy import divisors

def count_house(target,part2):
    house=0
    s=0
    while s<target:	
        house+=1

        d=divisors(house)
        if part2:
            f =filter(lambda x:house/x<=50,d)
            s=sum(map(lambda x:x*11,f))
            continue
        s=sum(map(lambda x:x*10,d))

        
    return house
def main(inp):
  
    target=int(inp)
    print(target)
    

    return count_house(target,False),count_house(target,True)