from collections import defaultdict


def steps(pos, dirs, l):
    global path_lengths
    dir = dirs[0]
    steps = int(dirs[1:])
    paths = []
    if dir == 'R':
        for i in range(1, steps + 1):
            p = (pos[0], pos[1] + i)
            paths.append(p)
            l += 1
            path_lengths[p] += l
    elif dir == 'L':
        for i in range(1, steps + 1):
            p = (pos[0], pos[1] - i)
            paths.append(p)
            l += 1
            path_lengths[p] += l
    elif dir == 'U':
        for i in range(1, steps + 1):
            p = (pos[0] - i, pos[1])
            paths.append(p)
            l += 1
            path_lengths[p] += l
    elif dir == 'D':
        for i in range(1, steps + 1):
            p = (pos[0] + i, pos[1])
            paths.append(p)
            l += 1
            path_lengths[p] += l
    return paths, l


def main(inp):
    global path_lengths
    wire1, wire2 = inp.splitlines()
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')
    
    path_lengths = defaultdict(int)

    pos = (0, 0)
    l = 0
    path1 = set()
    for i in wire1:
        moves, l = steps(pos, i, l)
        path1.update(moves)
        pos = moves[-1]
        
    pos = (0, 0)
    l = 0
    path2 = set()
    for i in wire2:
        moves, l = steps(pos, i, l)
        path2.update(moves)
        pos = moves[-1]

    inter = path1.intersection(path2)

    return min(abs(i) + abs(j) for i, j in inter), min(path_lengths[i] for i in inter)
