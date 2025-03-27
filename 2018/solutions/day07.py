import re
import networkx as nx


def main(inp):
    
    instr = [re.findall('(?:\s)([A-Z])(?:\s)', x) for x in inp.splitlines()]
    G = nx.DiGraph()
    for x in instr:
        G.add_edge(x[0], x[1])
    l = list(nx.lexicographical_topological_sort(G, key=lambda x: ord(x)))
    lex = ''.join(l)


    pred = {x: nx.ancestors(G, x) for x in G.nodes}
    passed = set()
    workers = {i: [] for i in range(5)}
    lex2 = ''
    t = 0
    while len(passed) < len(lex):
        
        for i in range(5):
            if workers[i]:
                if workers[i][1] == 0:
                    lex2 += workers[i][0]
                    passed.add(workers[i][0])
                    workers[i] = []
                else:
                    workers[i][1] -= 1
                    continue

        for i in range(5):
            if not workers[i]:
                possible = sorted([x for x in range(len(l)) if all(z in passed for z in pred[l[x]])])
                
                if possible:
                    w = l[possible.pop(0)]
                    l.remove(w)
                    workers[i] = [w, ord(w) - 64 - 1 + 60]


        t += 1


    return lex, t - 1

