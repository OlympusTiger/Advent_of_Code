import re
from sympy import solve
from sympy.abc import i, j


def calculate_score(claws, offset):
    score = 0

    for claw in claws:
        numbers = list(map(int, re.findall('-?\d+', claw)))
        a = numbers[:2]
        b = numbers[2:4]
        p = [x + offset for x in numbers[4:]]
        solutions = []

        for r in solve([p[0] - a[0] * i - b[0] * j, p[1] - a[1] * i - b[1] * j], [i, j], dict=True):
            if r[i] == int(r[i]) and r[j] == int(r[j]):
                solutions.append(3 * r[i] + r[j])
        if solutions:
            score += min(solutions)
    return score


def main(input_):
    claws = input_.split('\n\n')

    return calculate_score(claws, 0), calculate_score(claws, 10000000000000)

