import re
from copy import deepcopy
from collections import defaultdict
from itertools import product, groupby
import networkx as nx

def main(inp):
    bricks = [list(map(int, re.findall('\d+', l))) for l in inp.splitlines()]
    bricks = list(map(lambda x: [(x[0], x[3]), (x[1], x[4]), (x[2], x[5])], bricks))
    bricks.sort(key=lambda x: x[-1][0])
    def brick_loc(br):
        return list(product(range(br[0][0], br[0][1] + 1), range(br[1][0], br[1][1] + 1)))

    occupied = defaultdict(list)

    for z, b in enumerate(bricks):
        height = b[2][1] - b[2][0] + 1
        points = brick_loc(b)
        
        if b[2][0] == 1:
            for i in range(1, height + 1):
                occupied[i] += points
        else:
            for lvl in range(list(occupied.keys())[-1], 0, -1):
                if any(x in occupied[lvl] for x in points):
                    bricks[z][2] = [lvl + 1, lvl + height]
                    for l in range(lvl + 1, lvl + height + 1):
                        occupied[l] += points
                    break
            else:
                bricks[z][2] = [1, height]
                for l in range(1, height + 1):
                    occupied[l] += points

    bricks.sort(key=lambda x: x[2][1])

    groups = {l: list(g) for l, g in groupby(bricks, key=lambda b: b[2][1])}

    for b in bricks:
        if b[2][0] != b[2][1]:
            if b[2][0] in groups:
                groups[b[2][0]] += [b]
            else:
                groups[b[2][0]] = [b]

    G = nx.DiGraph()
    nofall = []

    for lvl in list(groups.keys()):
        for b in groups[lvl]:
            if b[2][0] == lvl and b[2][0] != b[2][1]:
                continue

            if lvl + 1 not in groups:
                nofall.append(tuple(map(tuple, b)))
                continue
            possible = deepcopy(groups[lvl])
            possible.remove(b)
            support = [i for i in groups[lvl + 1] if set(brick_loc(b)).intersection(set(brick_loc(i)))]

            for s in support:
                G.add_edge(tuple(map(tuple, b)), tuple(map(tuple, s)))

            if not possible and support:
                continue

            if not support:
                nofall.append(tuple(map(tuple, b)))
                continue
            else:
                rest = []
                for p in possible:
                    rest += brick_loc(p)

                if all(set(brick_loc(s)).intersection(rest) for s in support):
                    nofall.append(tuple(map(tuple, b)))


    c = 0

    def go_up(node):
        rem = set()

        for n in H.successors(node):
            if len(list(H.predecessors(n))) > 1:
                rem.add((node, n))
            else:
                if H.successors(n):
                    rem=rem|go_up(n)

        H.remove_edges_from(rem)
        return rem

    for start in G:
        if start not in nofall:
            H = G.copy()
            go_up(start)
            c+=(len(nx.descendants(H, start)))



    return len(nofall),c
                    