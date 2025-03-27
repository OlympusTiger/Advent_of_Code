from general import Grid
from itertools import product
def move(x, d):
    return (x[0] + d[0], x[1] + d[1])

def travel(grid, directions, start):
    robot = start
    for d in directions:
        nxt = move(robot, d)
        if grid[nxt] == '#':
            continue
        elif grid[nxt] == '.':
            grid[robot] = '.'
            robot = nxt
            grid[robot] = '@'
        else:
            to_move = nxt
            f = 2
            while grid[nxt] not in '.#':
                nxt = move(nxt, d)
                f += 1
            if grid[nxt] == '.':
                grid[robot] = '.'
                robot = to_move
                grid[robot] = '@'
                grid[nxt] = 'O'
            else:
                continue

    coords_sum = 0
    for i, j in product(range(grid.height), range(grid.width)):
        if grid[i, j] == 'O':
            coords_sum += 100 * i + j
    return coords_sum

def dfs(grid, start, d):
    if grid[start] == '[':
        half = move(start, (0, 1))
        boxes = {(start, half)}
    elif grid[start] == ']':
        half = move(start, (0, -1))
        boxes = {(half, start)}
    q = [start, half]
    seen = set()
    while q:
        p = q.pop()
        if p in seen:
            continue
        seen.add(p)
        nxt = move(p, d)

        if grid[nxt] == '#':
            return 0, grid
        
        if grid[nxt] == '[':
            half = move(nxt, (0, 1))
            boxes.add((nxt, half))
            q.extend([nxt, half])
        elif grid[nxt] == ']':
            half = move(nxt, (0, -1))
            boxes.add((half, nxt))
            q.extend([half, nxt])
    boxes = sorted(boxes)
    if d == (1, 0):
        boxes = boxes[::-1]
    for b in boxes:
        grid[b[0]] = '.'
        grid[b[1]] = '.'
        grid[move(b[0], d)] = '['
        grid[move(b[1], d)] = ']'

    return 1, grid

def travel_expanded(grid, directions, start):
    robot = start
    for d in directions:
        nxt = move(robot, d)
        if grid[nxt] == '#':
            continue
        elif grid[nxt] == '.':
            grid[robot] = '.'
            robot = nxt
            grid[robot] = '@'
        else:
            if d in ((0, -1), (0, 1)):
                to_move = nxt
                f = 2
                while grid[nxt] not in '.#':
                    nxt = move(nxt, d)
                    f += 1
                if grid[nxt] == '.':
                    grid[robot] = '.'
                    grid.popgrid(nxt)
                    robot = to_move
                    grid.insertgrid(robot, '@')
                else:
                    continue
            else:
                check, grid = dfs(grid, nxt, d)
                if check == 0:
                    continue
                else:
                    grid[robot] = '.'
                    robot = nxt
                    grid[robot] = '@'

    coords_sum = 0
    for i, j in product(range(grid.height), range(grid.width)):
        if grid[i, j] == '[':
            coords_sum += 100 * i + j
    return coords_sum

def main(inp):
    grid, raw_directions = inp.split('\n\n')
    raw_directions = raw_directions.replace('\n', '')
    directions = []
    for d in raw_directions:
        if d == '<':
            directions.append((0, -1))
        elif d == '>':
            directions.append((0, 1))
        elif d == '^':
            directions.append((-1, 0))
        elif d == 'v':
            directions.append((1, 0))

    expanded = []
    for l in grid.splitlines():
        temp = ''
        for c in l:
            if c == '.':
                temp += '..'
            elif c == '#':
                temp += '##'
            elif c == 'O':
                temp += '[]'
            elif c == '@':
                temp += '@.'
        expanded.append(list(temp))
    expanded = Grid(expanded)
    for i, j in product(range(expanded.height), range(expanded.width)):
        if expanded[i, j] == '@':
            ex_start = (i, j)
            break

    grid = Grid.from_txt_file(grid)
    for i, j in product(range(grid.height), range(grid.width)):
        if grid[i, j] == '@':
            start = (i, j)
            break
    return travel(grid, directions, start), travel_expanded(expanded, directions, ex_start)

