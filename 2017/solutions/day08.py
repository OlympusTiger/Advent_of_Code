from collections import defaultdict




def valid(registers,x):
    r,e,c=x.split()
    match e:
        case '==':
            return registers[r]==int(c)
        case '!=':
            return registers[r]!=int(c)
        case '<':
            return registers[r]<int(c)
        case '<=':
            return registers[r]<=int(c)
        case '>':
            return registers[r]>int(c)
        case '>=':
            return registers[r]>=int(c)


def main(inp):
    guide=[i.split(' if ') for i in inp.splitlines()]

    registers=defaultdict(int)
    mem=set()
    for i in guide:
        if valid(registers,i[1]):
            r,op,n=i[0].split()
            if op=='inc':
                registers[r]+=int(n)
            else:
                registers[r]-=int(n)
        mem.update(registers.values())

        


    return max(registers.values()),max(mem)
                