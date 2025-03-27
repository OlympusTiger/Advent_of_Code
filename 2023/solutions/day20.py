from math import lcm
from copy import deepcopy

class Module:
    def __init__(self, line):
        if line[0] == 'broadcaster':
            self.name = line[0]
            self.type = 'B'
        else:
            self.name = line[0][1:]
            self.type = line[0][0]
        self.state = False
        self.dest = line[1].split(', ')
        if self.type == '&':
            self.mem = {}

def sequence2(modules, mods, que, loop):
    while que:
        s, m, p = que[0]
        if m not in modules.keys():
            que.pop(0)
            continue
        elif modules[m].type == '%' and p == 'L':
            que += [(m, d, 'H') if modules[m].state == False 
               else (m, d, 'L') for d in modules[m].dest]
            modules[m].state = not modules[m].state
        elif modules[m].type == '&':
            modules[m].mem[s] = p
            if all(i == 'H' for i in modules[m].mem.values()):
                modules[m].state = True
                if m in mods:
                    mods[m] += [loop]
            else:
                modules[m].state = False
            que += [(m, d, 'L') if all(b == 'H' for b in modules[m].mem.values())
               else (m, d, 'H') for d in modules[m].dest]
        que.pop(0)
    return mods

def sequence(modules, que, Lows, Highs):
    while que:
        s, m, p = que[0]
        if p == 'L':
            Lows += 1
            Highs += 1
        if m not in modules.keys():
            que.pop(0)
            continue
        elif modules[m].type == '%' and p == 'L':
            que += [(m, d, 'H') if modules[m].state == False 
               else (m, d, 'L') for d in modules[m].dest]
            modules[m].state = not modules[m].state
        elif modules[m].type == '&':
            modules[m].mem[s] = p
            que += [(m, d, 'L') if all(b == 'H' for b in modules[m].mem.values())
               else (m, d, 'H') for d in modules[m].dest]
        que.pop(0)
    return Lows, Highs, {m.name: m.state for m in modules.values()}

def pulses(modules):
    Highs = 0
    Lows = 0
    initial = {m.name: m.state for m in modules.values()}
    states = initial.copy()
    start = True
    loop = 0

    while (loop < 1000 and states != initial) or start:
        start = False
        queue = [('B', d, 'L') for d in modules['broadcaster'].dest]
        Lows += 1
        Lows, Highs, states = sequence(modules, queue, Lows, Highs)
        loop += 1

    return Lows * Highs

def min_presses(modules):
    mods = {}
    for m in modules:
        if modules[m].dest == ['rx']:
            for a, b in modules.items():
                if m in b.dest:
                    for k, l in modules.items():
                        if a in l.dest:
                            mods[k] = []
    loop = 1
    while [] in mods.values():
        queue = [('B', d, 'L') for d in modules['broadcaster'].dest]
        mods = sequence2(modules, mods, queue, loop)
        loop += 1
    return lcm(*list(map(lambda i: i[0], mods.values())))

def main(inp):
    config = [l.split(' -> ') for l in inp.splitlines()]
    modules = {m.name: m for m in map(Module, config)}
    for n in modules.keys():
        if modules[n].type == '&':
            for a, b in modules.items():
                if n in b.dest:
                    modules[n].mem[a] = 'L'
    return pulses(deepcopy(modules)), min_presses(modules)

