# from sympy import Eq,solve_linear_system,symbols,solve,nsolve,solveset,S
from collections import defaultdict


def parser(line):
    inputs, output = line.split(" => ")
    output = output.split()
    output = (output[1], int(output[0]))
    inputs = [i.split() for i in inputs.split(", ")]
    inputs = [(i[1], int(i[0])) for i in inputs]
    return output[0], output[1], inputs


def mining(reactions, prod_mod):
    materials = defaultdict(int)
    spare = defaultdict(int)
    materials["FUEL"] += 1
    q = [("FUEL")]
    while q:
        current = q.pop(0)
        if current == "ORE":
            continue
        need = materials[current]
        for m, p in reactions[current]:
            
            


def main(inp):
    reactions = {}
    prod_mod = {}
    for line in inp.splitlines():
        o, p, i = parser(line)
        reactions[o] = i
        prod_mod[o] = p
    print(prod_mod)
    mining(reactions, prod_mod)
    return None, None
