from itertools import product


def optimize(e,r,m):
    if m=='*':
        if r%e==0:
            return True
        return False
    elif m=='||':
        l=len(str(e))
        if int(str(r)[-l:])==e:
            return True
        return False
    return True

def operations(a,b,op):
   
    if op=='+':
        return a+b
    elif op=='*':
        return a*b
    elif  op=='||':
        return int(f'{a}{b}')
    
def search(eq,r,operators):
    for p in product(operators,repeat=len(eq)-1):
        
        if not optimize(eq[-1],r,p[-1]):
            continue
        new=operations(eq[0],eq[1],p[0])
        for i,e in enumerate(eq[2:],1):
            if new>r:
               continue
            new=operations(new,e,p[i])
        if new==r:
            
            return True
    return False

def main(inp):
    equations=[i for i in inp.splitlines()]
    p1=0
    p2=0
    for i in equations:
        r,eq=i.split(':')
        r=int(r)
        eq=list(map(int,eq.split()))
        if search(eq,r,['*','+']):
            p1+=r
        if search(eq,r,['*','+','||']):
            p2+=r

        
            


    return p1,p2
                    