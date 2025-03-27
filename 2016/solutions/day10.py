from collections import defaultdict

def factory(instr):
    bots=defaultdict(list)
    while instr:
        i=instr.pop(0)
        spl=i.split()
        if 'value' in i:
            v,b=spl[1],spl[-1]
            bots[b].append(int(v))
        elif 'gives' in i and len(bots[spl[1]])==2:
            b=spl[1]
            l=spl[5]+spl[6]if spl[5]=='output' else spl[6]
            h=spl[10]+spl[11]if spl[10]=='output' else spl[11]
            bots[l].append(min(bots[b]))
            bots[h].append(max(bots[b]))
        else:
            instr.append(i)

    if [17,61] in (l:=list(map(sorted,bots.values()))):
        x=l.index([17,61])
        return list(bots.keys())[x],bots['output0'][0]*bots['output1'][0]*bots['output2'][0]
            


def main(inp):
    instr=sorted(inp.splitlines(),key=len)
    

    return factory(instr)