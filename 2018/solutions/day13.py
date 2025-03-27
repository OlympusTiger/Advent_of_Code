from itertools import cycle
from copy import deepcopy


def crash_course(grid, diretions, carts, remove_crashed=False):
    while True:
        if remove_crashed and len(carts) == 1:
            return carts[0][0][::-1]

        new_carts = []
        carts.sort(key=lambda x: x[0])
        positions = list(map(lambda x: x[0], carts))

        x = 0
        while x < len(carts):
            removed = False

            p, d, cy = carts[x]
            i = p[0] + d[0]
            j = p[1] + d[1]
            if (i, j) in positions:
                if remove_crashed:
                    for l in range(len(carts)):
                        if carts[l][0] == (i, j):
                            del carts[l]
                            removed = True
                            break

                    for l in range(len(new_carts)):
                        if new_carts[l][0] == (i, j):
                            del new_carts[l]
                            removed = True
                            break

                    positions.remove((i, j))

                else:
                    return (j, i)
            else:
                positions.remove(p)
                positions.append((i, j))
            if grid[i][j] == '+':
                z = diretions.index(d)
                d = diretions[(z + next(cy)) % 4]
            elif grid[i][j] == '/':
                if d == (0, 1):
                    d = (-1, 0)
                elif d == (1, 0):
                    d = (0, -1)
                elif d == (0, -1):
                    d = (1, 0)
                elif d == (-1, 0):
                    d = (0, 1)
            elif grid[i][j] == '\\':
                if d == (0, 1):
                    d = (1, 0)
                elif d == (1, 0):
                    d = (0, 1)
                elif d == (0, -1):
                    d = (-1, 0)
                elif d == (-1, 0):
                    d = (0, -1)
            if not remove_crashed or not removed:
                new_carts.append([(i, j), d, cy])

            x += 1
        carts = new_carts.copy()


def main(inp):
    grid = [list(i) for i in inp.splitlines()]
    carts = []
    diretions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    initial_diretions = {'>': 0, 'v': 1, '<': 2, '^': 3}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            x = grid[i][j]
            if x in ['<', '>', '^', 'v']:
                carts.append([(i, j), diretions[initial_diretions[x]], cycle([-1, 0, 1])])
                if x in ['<', '>']:
                    grid[i][j] = '-'
                else:
                    grid[i][j] = '|'

    return crash_course(
        grid, diretions, deepcopy(carts)
    ), crash_course(grid, diretions, carts, remove_crashed=True)

