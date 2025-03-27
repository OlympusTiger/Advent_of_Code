from sympy import divisors

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



from time import sleep

def process(reg0,program):
    regs=[reg0,0,0,0,0,0]
    pointer=0
    while pointer<len(program):
        if sum(regs)>1 and regs[1]==0:
            target=regs[4]
            break
        
        #1 3 8 18 115 309 794
        regs[ip]=pointer
        ops,a,b,c=program[pointer]
        regs=operations[ops](regs,None,[0,int(a),int(b),int(c)])
        pointer=regs[ip]+1
    
    print(sum(divisors(target)))
    return regs[0]

def main(inp):
    global operations,ip
    ip=int(inp.splitlines()[0].split()[-1])
    program=[i.split() for i in inp.splitlines()[1:]]
    operations={'addi':addi,'addr':addr,'mulr':mulr,'muli':muli,'banr':banr,'bani':bani,'borr':borr,'bori':bori,'setr':setr,'seti':seti,'gtir':gtir,'gtri':gtri,'gtrr':gtrr,'eqir':eqir,'eqri':eqri,'eqrr':eqrr}
    # regs=[0,0,0,0,0,0]
    # pointer=0
    # while pointer<len(program):
    #     sleep(1)
    #     print(regs)
    #     #1 3 8 18 115 309 794
    #     regs[ip]=pointer
    #     ops,a,b,c=program[pointer]
    #     regs=operations[ops](regs,None,[0,int(a),int(b),int(c)])
    #     pointer=regs[ip]+1


    
    return process(0,program),process(1,program)
                    