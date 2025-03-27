from itertools import product
from collections import deque
from time import time

s=time()
HEADINGS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def move(pos, heading):
    return (pos[0] + heading[0], pos[1] + heading[1])

def hiking_trail(grid, start):
    scores = 0
    ratings = 0
    finish = set()
    q = deque([start])
    while q:
        pos = q.pop()
        elevation = grid[pos[0]][pos[1]]
        if elevation == 9:
            ratings += 1
            if pos not in finish:
                finish.add(pos)
                scores += 1
                continue
        for heading in HEADINGS:
            nxt = move(pos, heading)
            if in_bounds(nxt, grid) and grid[nxt[0]][nxt[1]] == elevation + 1:
                q.append(nxt)
    return scores, ratings

def main(inp):
    topographic_map = [list(map(int, list(i))) for i in inp.splitlines()]
    starts = []
    for i, j in product(range(len(topographic_map)), repeat=2):
        if topographic_map[i][j] == 0:
            starts.append((i, j))

    scores = []
    ratings = []
    for start in starts:
        s, r = hiking_trail(topographic_map, start)
        scores.append(s)
        ratings.append(r)

    return sum(scores), sum(ratings)


