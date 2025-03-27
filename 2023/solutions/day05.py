def get_map(m):
    return [list(map(int, x.split())) for x in m]

def source_to_dest(l, nums):
    mp = get_map(l)
    for i, s in enumerate(nums):
        for r in mp:
            if s in range(r[1], r[1] + r[2]):
                nums[i] = s - r[1] + r[0]
    return nums

def get_map2(m):
    l = [list(map(int, x.split())) for x in m]
    r = [[[i[0], i[0] + i[2]], [i[1], i[1] + i[2]]] for i in l]
    return r

def source_to_dest2(d, m):
    m = get_map2(m)
    new = []
    for i, s in enumerate(d):
        for j in range(len(m)):
            if s[1] <= m[j][1][0] or s[0] >= m[j][1][1]:
                if j == len(m) - 1:
                    new.append([s[0], s[1]])
                    break
                else:
                    continue
            else:
                if s[0] >= m[j][1][0] and s[1] <= m[j][1][1]:
                    new.append([m[j][0][0] - m[j][1][0] + s[0], m[j][0][1] - m[j][1][1] + s[1]])
                    break
                elif s[0] < m[j][1][0] and s[1] <= m[j][1][1]:
                    new.append([m[j][0][0], m[j][0][1] - m[j][1][1] + s[1]])
                    d.append([s[0], m[j][1][0]])
                    break
                elif s[0] >= m[j][1][0] and s[1] > m[j][1][1]:
                    new.append([m[j][0][0] - m[j][1][0] + s[0], m[j][0][1]])
                    d.append([m[j][1][1], s[1]])
                    break
                elif s[0] < m[j][1][0] and s[1] > m[j][1][1]:
                    new.append([m[j][0][0] - m[j][1][0] + s[0], m[j][0][1] - m[j][1][1] + s[1]])
                    d.append([m[j][1][0], m[j][1][1]])
                    break
                elif j == len(m) - 1:
                    new.append([s[0], s[1]])
                    break
    return new

def main(inp):
    raw = inp.split('\n\n')
    seeds = raw[0]
    maps = raw[1:]
    seeds = list(map(int, seeds.split()[1:]))
    maps = [x[x.index(':') + 1:].strip('\n ').split('\n') for x in inp.split('\n\n')]
    seeds2 = seeds[:]
    for m in maps:
        data = source_to_dest(m, seeds)

    seeds2 = [[seeds2[i], seeds2[i] + seeds2[i + 1]] for i in range(0, len(seeds2), 2)]
    for m in maps:
        data2 = source_to_dest2(seeds2, m)
    return min(data), min(filter(lambda y: y > 0, map(lambda x: x[0], data2)))
