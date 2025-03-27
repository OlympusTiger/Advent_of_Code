

def main(inp):
    banks=list(map(int,inp.split()))
    print(banks)
    r=0
    mem=[banks]

    while mem.count(banks)!=2:
        i = banks.index(max(banks))

        banks=banks.copy()
        blocks=banks[i]
        banks[i]=0
        while blocks>0:
            i=(i+1)%len(banks)
            blocks-=1
            banks[i]+=1    
        r+=1
        mem.append(banks)

    i1=mem.index(banks)
    i2=mem.index(banks,i1+1)
    


    return r,i2-i1
                