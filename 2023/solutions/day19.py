import re
from functools import reduce

def work(workflow, ins, x):
    for i in workflow[ins].split(','):
        if i in 'AR':
            return i
        if i[1] == '<':
            if x[i[0]] < int(re.search('\d+', i).group()):
                return i.split(':')[1]
            else:
                continue
        elif i[1] == '>':
            if x[i[0]] > int(re.search('\d+', i).group()):
                return i.split(':')[1]
            else:
                continue
        return i

def acc_rej(workflow, part):
    g = 'in'
    while (temp := work(workflow, g, part)) not in 'AR':
        g = temp
    else:
        if work(workflow, g, part) == 'A':
            return True
        else:
            return False

def part1(parts, workflow):
    accepted = []
    for item in parts:
        if acc_rej(workflow, item):
            accepted.append(item)
    nums = 0
    for i in accepted:
        nums += sum(i.values())
    return nums

def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))

def find_range_pos(x):
    cat = x[0]
    num = int(re.search('\d+', x).group())
    if '>' in x:
        r = range(num + 1, 4001)
    else:
        r = range(1, num)
    accepted[count][cat] = range_intersect(accepted[count][cat], r)

def find_range_neg(x):
    cat = x[0]
    num = int(re.search('\d+', x).group())
    if '<' in x:
        r = range(num, 4001)
    else:
        r = range(1, num + 1)
    accepted[count][cat] = range_intersect(accepted[count][cat], r)

def track_parent(workflow, child):
    for p in workflow.keys():
        if child in re.findall('[AR]|[a-z]{2,3}', workflow[p]):
            ind = re.findall('[AR]|[a-z]{2,3}', workflow[p]).index(child)
            for i, cond in enumerate(workflow[p].split(',')):
                if child == cond:
                    return None if p == 'in' else track_parent(workflow, p)
                elif i == ind:
                    find_range_pos(cond)
                    return None if p == 'in' else track_parent(workflow, p)
                else:
                    find_range_neg(cond)

def find_As(workflow, child, v, ind, end):
    for k, cond in enumerate(v.split(',')):
        if cond == 'A':
            track_parent(workflow, child)
            return
        elif k == ind:
            find_range_pos(cond)
            track_parent(workflow, child)
            return
        else:
            find_range_neg(cond)

def part2(workflow):
    global accepted, count
    count = 0
    accepted = []
    for i, value in enumerate(workflow.values()):
        start = list(workflow.keys())[i]
        for j, part in enumerate(value.split(',')):
            if 'A' in part:
                accepted.append(dict.fromkeys(['x', 'm', 'a', 's'], range(1, 4001)))
                find_As(workflow, start, value, j, ':A' in part)
                count += 1
    total = 0
    for d in accepted:
        total += reduce(lambda x, y: x * y, map(len, d.values()))
    return total

def main(inp):
    instr, items = inp.split('\n\n')
    part = [item.strip('{}').split(',') for item in items.splitlines()]
    parts = []
    for item in part:
        parts.append({i.split('=')[0]: int(i.split('=')[1]) for i in item})
    workflow = {ins[:-1].split('{')[0]: ins[:-1].split('{')[1] for ins in instr.splitlines()}
    return part1(parts, workflow), part2(workflow)

