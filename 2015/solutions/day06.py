from contextlib import suppress
import re
from collections import defaultdict


def part1(instructions):
    lights_on = defaultdict(set)
    for ins in instructions:
        a, b = (
            set(range(int(ins[1]), int(ins[3]) + 1)),
            set(range(int(ins[2]), int(ins[4]) + 1)),
        )
        if ins[0] == "on":
            for i in a:
                lights_on[i] |= b
        elif ins[0] == "off":
            for i in a:
                lights_on[i] -= b
        else:
            for i in a:
                to_remove = lights_on[i].intersection(b)
                to_add = b - lights_on[i].intersection(b)
                lights_on[i] -= to_remove
                lights_on[i] |= to_add

    return sum(map(len, lights_on.values()))


def part2(instructions):
    lights_on = defaultdict(list)

    for ins in instructions:
        a, b = (
            set(range(int(ins[1]), int(ins[3]) + 1)),
            set(range(int(ins[2]), int(ins[4]) + 1)),
        )
        if ins[0] == "on":
            for i in a:
                lights_on[i] += list(b)
        elif ins[0] == "toggle":
            for i in a:
                lights_on[i] += 2 * list(b)

        else:
            for i in a:
                for j in b:
                    with suppress(ValueError):
                        lights_on[i].remove(j)

    return sum(map(len, lights_on.values()))


def main(inp):
    instructions = [re.findall("on|off|toggle|\d+", line) for line in inp.splitlines()]

    return part1(instructions), part2(instructions)
