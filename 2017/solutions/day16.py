
def dance(programs,moves,part2=False):
    mem=[]
    x=0

    while programs not in mem:
        x+=1
        mem.append(programs.copy())
        for m in moves:
            if m[0]=='s':
                programs=programs[-int(m[1:]):]+programs[:-int(m[1:])]
            elif m[0]=='x':
                p=sorted(list(map(int,m[1:].split('/'))))
                i=programs[p[0]]
                programs[p[0]]=programs[p[1]]
                programs[p[1]]=i
            elif m[0]=='p':
                p1,p2=m[1:].split('/')
                i,j=programs.index(p1),programs.index(p2)
                programs[i]=p2
                programs[j]=p1

        if not part2:
            return programs
        
    return mem[1000000000%x]
   

def main(inp):
    moves=inp.split(',')
    programs=[chr(i)for i in range(ord('a'),ord('p')+1)]

    return ''.join(dance(programs.copy(),moves)),''.join(dance(programs,moves,True))
                