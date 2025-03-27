from itertools import product, groupby
from operator import sub
import re

def get_numbers(eng):
    nums = []
    for i, k in enumerate(eng):
        for l in re.finditer('\d+', k):
            nums.append((l.group(), i, l.start(), sub(*l.span()[::-1])))
    return nums

def get_adjacent(eng, symbols):
    nums = get_numbers(eng)
    exclude = []
    for n, ind, start, span in nums:
        if all(eng[ind+x][start+y] not in symbols for x, y in product([-1,0,1],range(-1,span+1)) if 0<=ind+x<len(eng) and 0<=start+y<len(eng[0]) and not(x==0 and y in range(span))):
            exclude.append(n)
    return nums, exclude

def main(inp):
    eng = inp.splitlines()
    symbols = set([i for i in inp if i != '.' and not i.isdigit()])
    nums, exclude = get_adjacent(eng, symbols)
    gears = []
    for n, ind, start, span in nums:
        for x, y in product([-1,0,1],range(-1,span+1)):
            if 0<=ind+x<len(eng) and 0<=start+y<len(eng[0]) and not(x==0 and y in range(span)) and eng[ind+x][start+y] == '*':
                gears.append((n, ind+x, start+y))
    res = 0
    for _, j in groupby(sorted(gears, key=lambda x: (x[1], x[2])), key=lambda x: (x[1], x[2])):
        if len(l := list(j)) == 2:
            res += int(l[0][0]) * int(l[1][0])
    return sum(int(i[0]) for i in nums) - sum(map(int, exclude)), res
