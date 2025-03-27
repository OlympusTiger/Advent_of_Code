from copy import deepcopy


def main(inp):
    disk_map = list(map(int, inp))
    disk = []
    empty = []
    filled = []
    id = 0
    ind = 0
    for i in range(len(disk_map)):
        n = disk_map[i]
        if i % 2 == 0:
            disk.extend(n * [id])
            filled.append([ind, n, id])
            id += 1
            ind += n
        else:
            disk.extend(n * ['.'])
            empty.append([ind, n])
            ind += n

    filled1 = deepcopy(filled)
    empty1 = deepcopy(empty)

    for f in filled1[::-1]:
        while f[1]:
            if not empty1:
                break
            for e in empty1:
                if f[0] < e[0]:
                    empty1.remove(e)
                    break
                if f[1] <= e[1]:
                    new = [e[0], f[1], f[2]]
                    e[0] += f[1]
                    e[1] -= f[1]
                    f[1] = 0
                    if e[1] == 0:
                        empty1.remove(e)
                    filled1.append(new)
                    break
                elif f[1] > e[1]:
                    new = [e[0], e[1], f[2]]
                    f[1] -= e[1]
                    filled1.append(new)
                    empty1.remove(e)
                    break

    for f in filled[::-1]:
        for e in empty:
            if f[0] > e[0] and f[1] <= e[1]:
                filled.append([e[0], f[1], f[2]])
                e[0] += f[1]
                e[1] -= f[1]
                f[1] = 0
                if e[1] == 0:
                    empty.remove(e)
                break

    return sum(sum(range(f[0], f[0] + f[1])) * f[2] for f in filled1), sum(
        sum(range(f[0], f[0] + f[1])) * f[2] for f in filled)


