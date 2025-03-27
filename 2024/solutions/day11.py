from functools import cache


@cache
def rules(stone):
    st = str(stone)
    if stone == 0:
        return [1]
    elif len(st) % 2 == 0:
        return [int(st[:len(st)//2]), int(st[len(st)//2:])]
    else:
        return [stone * 2024]

@cache
def blink(stone, i):
    if i == 1:
        return len(rules(stone))
    return sum(blink(s, i-1) for s in rules(stone))

def run(stones, times):
    return sum(blink(s, times) for s in stones)

def main(inp):
    stones = [int(i) for i in inp.split()]
    return run(stones, 25), run(stones, 75)

