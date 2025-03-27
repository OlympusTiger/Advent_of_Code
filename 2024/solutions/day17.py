
def operand(v, reg):
    if v in range(4):
        return v
    elif v == 4:
        return reg[0]
    elif v == 5:
        return reg[1]
    elif v == 6:
        return reg[2]


def operations(op, oper, reg, i):
    if op == 0:
        r = reg[0] // (2 ** operand(oper, reg))
        reg[0] = r
        i += 2
    elif op == 1:
        r = reg[1] ^ oper
        reg[1] = r
        i += 2
    elif op == 2:
        r = operand(oper, reg) % 8
        reg[1] = r
        i += 2
    elif op == 3:
        if reg[0] == 0:
            i += 2
        else:
            i = oper
    elif op == 4:
        r = reg[1] ^ reg[2]
        reg[1] = r
        i += 2
    elif op == 5:
        r = operand(oper, reg) % 8
        return reg, i + 2, r
    elif op == 6:
        r = reg[0] // (2 ** operand(oper, reg))
        reg[1] = r
        i += 2
    elif op == 7:
        r = reg[0] // (2 ** operand(oper, reg))
        reg[2] = r
        i += 2
    return reg, i, None


def recursive_search(program, pr, n):
    if not pr:
        return n
    for j in range(8):
        nxt = (n << 3) + j
        reg = {0: nxt, 1: 0, 2: 0}
        i = 0
        while i < len(program):
            a, b = program[i], program[i + 1]
            reg, i, out = operations(a, b, reg, i)
            if out == pr[-1]:
                ret = recursive_search(program, pr[:-1], nxt)
                if ret is None:
                    continue
                return ret
            elif out is not None:
                break
    return None


def main(inp):
    regs, program = inp.split('\n\n')
    reg = {}
    for i, r in enumerate(regs.splitlines()):
        t = int(r.split(':')[1])
        reg[i] = t
    program = program.split(':')[1].strip()
    program = list(map(int, program.split(',')))
    i = 0
    outs = []
    while i < len(program):
        a, b = program[i], program[i + 1]
        reg, i, out = operations(a, b, reg, i)
        if out != None:
            outs.append(out)
    return ','.join(map(str, outs)), recursive_search(program, program, 0)

