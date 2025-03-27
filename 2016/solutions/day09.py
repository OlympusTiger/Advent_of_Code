from itertools import takewhile


def part1(inp):
    i=0
    dec=0
    while i<len(inp):
        if inp[i]=='(':
            j=inp[i:].index(')')
            s,t=map(int,inp[i+1:i+j].split('x'))  #streak,times
            dec+=len(inp[i+j+1:i+j+1+s])*t
            i+=j+1+s
            
        else:
            dec+=1
            i+=1
    return dec


def part2(inp):
    i=0
    l=0
    while i<len(inp):
        if inp[i]=='(':
            j=inp[i:].index(')')
            s,t=map(int,inp[i+1:i+j].split('x'))  #streak,times
            l+=t*part2(inp[i+j+1:i+j+1+s])
            i+=j+1+s
            
        else:
            l+=1
            i+=1
    return l
def main(inp):
    
    
    return part1(inp),part2(inp)