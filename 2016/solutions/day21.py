from collections import deque

def unsolve(instr):
    s=deque(list('fbgdceah'))

    new_to_old={}
    for o in range(len(s)):
        x=2*o+1
        if o>=4:
            x+=1
        new_to_old[x%len(s)]=o-x
  
    for i in instr[::-1]:
  
        match i[0]:
            case 'swap' if i[1]=='position':
                s[i[2]],s[i[5]]=s[i[5]],s[i[2]]
            case 'swap' if i[1]=='letter':
                a=s.index(i[2])
                b=s.index(i[5])
                s[a],s[b]=s[b],s[a]
            case 'rotate' if i[1]=='based':
                x=s.index(i[6])
                s.rotate(new_to_old[x])     
            case 'rotate' if i[1]=='left':
                s.rotate(i[2])
            case 'rotate' if i[1]=='right':
                s.rotate(-i[2])
            case 'reverse':
                s=list(s)
                s=s[:i[2]] + s[i[2]:i[4]+1][::-1] + s[i[4]+1:]
                s=deque(s)
            case 'move':
                s.rotate(-i[5])
                x=s.popleft()
                s.rotate(i[5])
                s.insert(i[2],x)
        
    return ''.join(s)


def generate(instr):
    s=deque(list('abcdefgh'))


    for i in instr:
        match i[0]:
            case 'swap' if i[1]=='position':
                s[i[2]],s[i[5]]=s[i[5]],s[i[2]]
            case 'swap' if i[1]=='letter':
                a=s.index(i[2])
                b=s.index(i[5])
                s[a],s[b]=s[b],s[a]
            case 'rotate' if i[1]=='based':
                x=s.index(i[6])+1
                if x>=4:
                    x+=1
                s.rotate(x)
            case 'rotate' if i[1]=='left':
                s.rotate(-i[2])
            case 'rotate' if i[1]=='right':
                s.rotate(i[2])
            case 'reverse':
                s=list(s)
                s=s[:i[2]] + s[i[2]:i[4]+1][::-1] + s[i[4]+1:]
                s=deque(s)
            case 'move':
                s.rotate(-i[2])
                x=s.popleft()               
                s.rotate(i[2])
                s.insert(i[5],x)
        
    return ''.join(s)


def main(inp):
    instr=[list(map(lambda x:x if x.isalpha() else int(x),i.split()))  for i in inp.splitlines()]

    
    return generate(instr),unsolve(instr)