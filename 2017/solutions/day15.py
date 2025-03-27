
# def operation(x,f):
#     div=2147483647
#     return (x*f)%div

def operation(x,f,i):
    div=2147483647
    k=(x*f)%div
    if k%i==0:
        return k
    else:
        return operation(k,f,i)

def sample(gens,factors,size,m=0):
    t=0
    for i in range(size):
        gens['A']=operation(gens['A'],factors['A'],4**m)
        gens['B']=operation(gens['B'],factors['B'],8**m)
        if abs(gens['A'] - gens['B'])%65536==0:
            t+=1
    return t

def main(inp):
    gens={i.split()[1]:int(i.split()[-1]) for i in inp.splitlines()}
    factors={'A': 16807, 'B': 48271}
    
    return sample(gens.copy(),factors,40000000),sample(gens,factors,5000000,1)
                