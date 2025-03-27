
def compute(instr,a):
    

    reg=dict(zip(['a','b','c','d'],[a,0,0,0]))
    i=0
    out=[]
    while i<len(instr):
        x=instr[i]
 
        match x[0]:
            case 'out':

                out.append(reg[x[1]])
                if len(out)==12:
                    if out==[0,1]*6:
                        return a
                    else:
                        return compute(instr,a+1)


            case 'cpy':
                if x[1].isdigit():
                    reg[x[2]]=int(x[1])
                else:
                    reg[x[2]]=reg[x[1]]
            case 'inc':
                reg[x[1]]+=1
            case 'dec':
                reg[x[1]]-=1
            case 'jnz' if (x[1].isdigit() and int(x[1])!=0) or (x[1] in reg and reg[x[1]]!=0):
                i+=int(x[2])
                continue
        i+=1
    # return reg['a']
                

    

def main(inp):
    instr=list(map(lambda x:x.strip('\n').split(),inp.splitlines()))
    print(instr)

    return compute(instr,0),None