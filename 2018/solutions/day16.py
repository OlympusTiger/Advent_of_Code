import re
from copy import deepcopy
from collections import defaultdict


def addr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] + ins[b]
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def addi(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] + b
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def mulr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] * ins[b]
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def muli(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] * b
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def banr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] & ins[b]
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def bani(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] & b
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def borr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] | ins[b]
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def bori(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a] | b
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def setr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = ins[a]
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def seti(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = a
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0    
    
def gtir(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = 1 if a > ins[b] else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def gtri(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = 1 if ins[a] > b else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def gtrr(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = 1 if ins[a] > ins[b] else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0
    
def eqir(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = 1 if a == ins[b] else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def eqri(ins,outs,nums):
    n,a,b,c = nums
    ins[c] = 1 if ins[a] == b else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def eqrr(ins,outs,nums):
    n,a,b,c = nums
    
    ins[c] = 1 if ins[a] == ins[b] else 0
    if outs is None:
        return ins
    if ins == outs:
        return 1
    return 0


def main(inp):
    in_outs,program = inp.split('\n\n\n\n')
    in_outs = [list(map(lambda x:list(map(int,re.findall('\d+',x))),i.splitlines())) for i in in_outs.split('\n\n')]
    program = [list(map(int,i.split())) for i in program.splitlines()]


    operations = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
    opcodes = defaultdict(lambda: set())
    over_3 = 0
    for x in in_outs:
        z = 0
        possible = []
        l = x[1][0]
        for f in operations:
            y = deepcopy(x)
            k = f(y[0],y[2],y[1])
            z += k
            if k:
                possible.append(f)

        if opcodes[l] == set():
            opcodes[l] = set(possible)
        else:
            opcodes[l] = opcodes[l].intersection(set(possible))
        
        if z >= 3:
            over_3 += 1

    cleared = set()
    while any(len(i)>1 for i in opcodes.values()):
        for k in opcodes:
            if k not in cleared and len(opcodes[k]) == 1:
                for k2 in opcodes:
                    if k2 != k and k2 not in cleared:
                        opcodes[k2] = opcodes[k2].difference(opcodes[k])
                cleared.add(k)
                
                break
    for o in opcodes:
        opcodes[o] = opcodes[o].pop()
    reg = [0,0,0,0]
    for k in program:
        reg = opcodes[k[0]](reg,None,k)



            
    return over_3,reg[0]

