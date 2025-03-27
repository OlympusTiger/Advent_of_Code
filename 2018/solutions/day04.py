from collections import Counter, defaultdict
from re import search


def main(inp):
    records = sorted(inp.splitlines())
    guards = defaultdict(lambda: [0, []])

    i = 0
    while i < len(records):
        g = search('(?<=#)\d+', records[i]).group(0)
        i += 1
        while i < len(records) and '#' not in (r := records[i]):
            if 'asleep' in r:
                a = search('(?<=00:)\d+', r).group(0)
            else:
                w = search('(?<=00:)\d+', r).group(0)
                guards[g][0] += int(w) - int(a)
                guards[g][1].extend(range(int(a), int(w)))
            i += 1

    g = max(guards.items(), key=lambda x: x[1][0])
    minute = max(Counter(g[1][1]).items(), key=lambda x: x[1])

    guard_max = [(x, max(Counter(guards[x][1]).items(), key=lambda x: x[1])) for x in guards]
    m = max(guard_max, key=lambda x: x[1][1])

    return int(g[0]) * minute[0], int(m[0]) * m[1][0]
                    