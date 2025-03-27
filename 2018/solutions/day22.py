from itertools import product
from functools import cache
import heapq

@cache
def erosion_level(pos):
    return (geologic_index(pos) + depth) % 20183

@cache
def geologic_index(pos):
    if pos[0] == 0 and pos[1] == 0:
        return 0
    if pos[0] == 0:
        return pos[1] * 16807
    if pos[1] == 0:
        return pos[0] * 48271
    return erosion_level((pos[0]-1, pos[1])) * erosion_level((pos[0], pos[1]-1))

def adjacent(grid, pos):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (pos[0]+i, pos[1]+j) in grid:
            yield (pos[0]+i, pos[1]+j)

def traverse(grid):
    pos = (0, 0)
    minutes = 0
    Q = []
    heapq.heappush(Q, (0, pos, 't'))
    heapq.heappush(Q, (7, pos, 'c'))
    explored = set()
    rocky = {'c', 't'}
    wet = {'c', 'n'}
    narrow = {'t', 'n'}
    while Q:
        minutes, pos, tool = heapq.heappop(Q)
        if (pos, tool) in explored:
            continue
        explored.add((pos, tool))

        if pos == target and tool == 't':
            return minutes

        current = grid[(pos[0], pos[1])]
        for a in adjacent(grid, pos):
            new = grid[(a[0], a[1])]

            if current == 0:
                if new == 0:
                    heapq.heappush(Q, (minutes+1, a, tool))
                    heapq.heappush(Q, (minutes+8, a, (rocky-{tool}).pop()))
                elif new == 2:
                    if tool == 't':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 't'))
                elif new == 1:
                    if tool == 'c':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 'c'))
            if current == 1:
                if new == 1:
                    heapq.heappush(Q, (minutes+1, a, tool))
                    heapq.heappush(Q, (minutes+8, a, (wet-{tool}).pop()))
                elif new == 2:
                    if tool == 'n':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 'n'))
                elif new == 0:
                    if tool == 'c':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 'c'))
            if current == 2:
                if new == 2:
                    heapq.heappush(Q, (minutes+1, a, tool))
                    heapq.heappush(Q, (minutes+8, a, (narrow-{tool}).pop()))
                elif new == 1:
                    if tool == 'n':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 'n'))
                elif new == 0:
                    if tool == 't':
                        heapq.heappush(Q, (minutes+1, a, tool))
                    else:
                        heapq.heappush(Q, (minutes+8, a, 't'))

def main(inp):
    global depth, target
    depth = 4848
    target = (700, 15)

    grid = {}

    for p in product(range(target[0]+200), range(target[1]+200)):
        grid[p] = erosion_level((p[0], p[1])) % 3
    grid[(target[0], target[1])] = 0

    return sum(t[1] for t in grid.items() if t[0][0] <= target[0] and t[0][1] <= target[1]), traverse(grid)

