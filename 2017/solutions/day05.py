


def main(inp):
    guide=list(map(int,inp.splitlines()))
    guide1=guide.copy()
    i=0
    steps1=0
    
    while i<len(guide):
        guide[i]+=1
        i+=guide[i]-1
        steps1+=1
    
    i=0
    steps2=0
    while i<len(guide1):
        if guide1[i]>=3:
            guide1[i]-=1
            i+=guide1[i]+1
        else:
            guide1[i]+=1
            i+=guide1[i]-1
        steps2+=1
        
        
    return steps1,steps2
                