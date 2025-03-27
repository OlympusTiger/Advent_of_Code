from itertools import pairwise,groupby

def condition1(x):
    return any(i==j for i,j in pairwise(x))

def condition2(x):
    return all(i<=j for i,j in pairwise(x))

def condition3(x):
    g=groupby(x)
    return  any(len(list(i)) == 2 for _,i in g)


def main(inp):
    r1,r2=map(int,inp.split('-'))
    res1=0
    res2=0
    for i in range(r1,r2+1):
        
        if condition1(str(i)) and condition2(str(i)):
          
            res1+=1
            if condition3(str(i)):
                res2+=1
    


    return res1,res2
                    