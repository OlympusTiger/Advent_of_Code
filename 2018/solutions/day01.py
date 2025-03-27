

def main(inp):
    l=inp.splitlines()
    s=0
    for i in l:
        s+=int(i)
    fq=set()
    f=0
    i=0
    while f not in fq:
        
        if i==len(l):
            i=0
        fq.add(f)
        f+=int(l[i])
        i+=1
    
    return s,f
                    