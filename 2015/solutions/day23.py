import re


def solve(instr,s):

    reg={'a':s,'b':0}
    l=len(instr)
    i=0
    while i<l:	
        x=instr[i]	
        match x[0]:
            case 'hlf':
                reg[x[1]]=int(reg[x[1]]/2)			
            case 'tpl':
                reg[x[1]]*=3			
            case 'inc':
                reg[x[1]]+=1		
            case 'jmp':
                i+=int(x[1])
                continue
            case 'jie' if reg[x[1]]%2==0:
                i+=int(x[2])
                continue				
            case 'jio' if reg[x[1]]==1:
                i+=int(x[2])	
                continue
        i+=1
    return reg['b']

def main(inp):
    instr=list(map(lambda x:x.strip('\n'),inp.splitlines()))
    instr=list(map(lambda x:re.findall('\-?\+?\w+',x),instr))
    



    return solve(instr,0),solve(instr,1)