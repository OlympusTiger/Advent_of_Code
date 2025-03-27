from itertools import groupby

def loop(n,k=0):
    if k==50:
    
       
        return len(n)
    else:
        

        groups=groupby(n)
        new=''
        for i,g in groups:
            new+=str(len(list(g)))+i 
    return loop(new,k+1)


def main(inp):
    for i in inp.splitlines():
        print(i,loop(i))
    return None,None