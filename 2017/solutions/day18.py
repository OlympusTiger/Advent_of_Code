from collections import defaultdict


def value(x, reg):
    return int(x) if x.lstrip('-').isdigit() else reg[x]


def duet(guide, p2=False, id=None, queue=None, registers={}, i=0, n=0):
    played = 0
    registers = defaultdict(int, registers)

    send = []
    while 0 <= i < len(guide):
        g = guide[i]

        match g[0]:
            case 'snd':
                if not p2:
                    played = registers[g[1]]
                else:
                    n += 1
                    send.append(value(g[1], registers))
            case 'set':
                registers[g[1]] = value(g[2], registers)
            case 'add':
                registers[g[1]] += value(g[2], registers)
            case 'mul':
                registers[g[1]] *= value(g[2], registers)
            case 'mod':
                registers[g[1]] %= value(g[2], registers)
            case 'rcv':
                if not p2:
                    return played
                elif queue:
                    registers[g[1]] = queue.pop(0)
                else:
                    return (queue, registers, i, send, n)
            case 'jgz' if value(g[1], registers) > 0:
                i += value(g[2], registers)
                continue
        i += 1

    return (queue, registers, i, [], n)


def parallel(guide):
    queue1, reg1, i1, end1, n1 = [], {'p': 0}, 0, False, 0
    queue2, reg2, i2, end2, n2 = [], {'p': 1}, 0, False, 0
    start = True

    while start or ((queue1 or queue2) and not (end1 and end2)):
        start = False
        if not end1:
            queue1, reg1, i1, q1, n1 = duet(
                guide, p2=True, id=0, queue=queue1, registers=reg1, i=i1, n=n1
            )

            if q1:
                queue2.extend(q1)
            else:
                queue1 = []
        if not end2:
            queue2, reg2, i2, q2, n2 = duet(
                guide, p2=True, id=1, queue=queue2, registers=reg2, i=i2, n=n2
            )

            if q2:
                queue1.extend(q2)
        if i1 >= len(guide):
            end1 = True
        if i2 >= len(guide):
            end2 = True
    return n2


def main(inp):
    guide = [line.split() for line in inp.splitlines()]

    return duet(guide), parallel(guide)




