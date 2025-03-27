from math import factorial
from copy import deepcopy
def compute(instr,a):

    reg=dict(zip(['a','b','c','d'],[a,0,0,0]))
    
    i=0
    while i<len(instr):

        
        x=instr[i]

        match x[0]:
            case 'tgl':
                j=i+reg[x[1]]
                if j<len(instr):
                    z=instr[j]
                    if len(z)==2:
                        if z[0]=='inc':
                            instr[j][0]='dec'
                        else:
                            instr[j][0]='inc'
                    else:
                        if z[0]=='jnz':
                            instr[j][0]='cpy'
                        else:
                            instr[j][0]='jnz'

            case 'cpy':
                if x[2].isdigit():
                    i+=1
                    continue
                if x[1]in reg:
                    reg[x[2]]=reg[x[1]]
                else:
                    reg[x[2]]=int(x[1])
            case 'inc':
                reg[x[1]]+=1
            case 'dec':
                reg[x[1]]-=1
            case 'jnz' if (x[1].isdigit() and int(x[1])!=0) or (x[1] in reg and reg[x[1]]!=0):
                if x[2] in reg:
                    i+=reg[x[2]]
                else:
                    i+=int(x[2])
                
                continue
       
        i+=1

    return reg['a']
                

    

def main(inp):

    instr=list(map(lambda x:x.strip('\n').split(),inp.splitlines()))
    mod=deepcopy(instr)
    l=sorted([int(j) for i in instr for j in i if j.isdigit()])

    return compute(mod,7),factorial(12)+l[-1]*l[-2]