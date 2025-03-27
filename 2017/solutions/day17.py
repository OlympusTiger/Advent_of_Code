
def part2(steps):
    pos1=[]
    p=0
    for i in range(1,50000000+1):
        p=1+(steps+p)%i
        if p==1:
            pos1.append(i)
    return pos1[-1]

def main(inp):
    steps=int(inp)
    # steps=3
    buffer=[0]
    p=0
    for i in range(1,2017+1):
        p=1+(steps+p)%i
        buffer.insert(p,i)
        
    return buffer[buffer.index(2017)+1],part2(steps)    
                