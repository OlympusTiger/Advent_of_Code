from itertools import product, pairwise
from heapq import heappop, heappush

Numpad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          [None, '0', 'A']]
rnum = {Numpad[i][j]: (i, j) for i, j in product(range(4), range(3))}

Navpad = [[None, (-1, 0), 'A'],
          [(0, -1), (1, 0), (0, 1)]]
rnav = {Navpad[i][j]: (i, j) for i, j in product(range(2), range(3))}

pads = [Numpad, Navpad]
trans = {(0, 1): '>', (0, -1): '<', (1, 0): 'v', (-1, 0): '^'}

headings = ((0, 1), (0, -1), (1, 0), (-1, 0))

def move(p, d):
    return p[0] + d[0], p[1] + d[1]

def in_bounds(grid, p):
    return 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])

def get_directions(path):
    return [(y[0] - x[0], y[1] - x[1]) for x, y in pairwise(path)]

cache = {}
def bfs(id, start, end, max_depth):
    if id > 0:
        e = rnav[end]
        locs[id] = e
        if (id, start, end) in cache:
            return cache[(id, start, end)]
    pad = Navpad if id > 0 else Numpad

    paths = []
    q = [(0, start, [start])]
    seen = set()
    maxs = float('inf')
    while q:
        steps, pos, path = heappop(q)
        if steps > maxs:
            break
        if pad[pos[0]][pos[1]] == end and steps <= maxs:
            maxs = steps
            end_pos = pos
            path = get_directions(path)
            paths.append(path + ['A'])
            continue
        if (pos, tuple(path)) in seen:
            continue
        seen.add((pos, tuple(path)))
        for heading in headings:
            nxt = move(pos, heading)
            if in_bounds(pad, nxt) and pad[nxt[0]][nxt[1]] is not None:
                heappush(q, (steps + 1, nxt, path + [nxt]))
    locs[id] = end_pos

    all_paths_lens = []
    if id == max_depth:
        for path in paths:
            all_paths_lens.append(len(path))
        return min(all_paths_lens)
    for path in paths:
        lengths = []
        for p in path:
            lengths.append(bfs(id + 1, locs[id + 1], p, max_depth))
        all_paths_lens.append(sum(lengths))
    cache[(id, start, end)] = min(all_paths_lens)
    return min(all_paths_lens)

def search(codes, max_depth):
    cache.clear()
    global locs
    all_my_pad = 0
    for code in codes:
        locs = [(3, 2)] + [(0, 2)] * max_depth
        my_pad = 0
        for c in code:
            my_pad += bfs(0, locs[0], c, max_depth)
        all_my_pad += my_pad * int(code[:-1])
    return all_my_pad

def main(inp):
    codes = inp.splitlines()
    return search(codes, 2), search(codes, 25)





