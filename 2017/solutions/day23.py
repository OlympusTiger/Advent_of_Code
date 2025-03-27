from sympy import isprime
def value(x, reg):
    return int(x) if x.lstrip('-').isdigit() else reg[x]


def main(inp):
    guide=[i.split() for i in inp.splitlines()]
    
    registers=dict.fromkeys(['a','b','c','d','e','f','g','h'],0)
    i=0
    times=0
    while i<len(guide):
        g=guide[i]
        match g[0]:
            case 'set':
                registers[g[1]]=value(g[2],registers)
            case 'sub':
                registers[g[1]]-=value(g[2],registers)
            case 'mul':
                registers[g[1]]*=value(g[2],registers)
                times+=1
            case 'jnz' if value(g[1],registers)!=0:
                i+=value(g[2],registers)
                continue
        i+=1

    
    registers=dict.fromkeys(['a','b','c','d','e','f','g','h'],0)
    registers['a']=1
    x=0
    while x<=9:
        g=guide[x]
        match g[0]:
            case 'set':
                registers[g[1]]=value(g[2],registers)
            case 'sub':
                registers[g[1]]-=value(g[2],registers)
            case 'mul':
                registers[g[1]]*=value(g[2],registers)
                times+=1
            case 'jnz' if value(g[1],registers)!=0:
                x+=value(g[2],registers)
                continue
        x+=1

    reg_h=0
    for y in range(registers['b'],registers['c']+1,17):
        if not isprime(y):
            reg_h+=1

    return times,reg_h
                