from itertools import product


def opcodes(program, pointer):
    op = program[pointer]
    if op == 1:
        a, b, s = program[pointer + 1:pointer + 4]
        program[s] = program[a] + program[b]
        pointer += 4
    elif op == 2:
        a, b, s = program[pointer + 1:pointer + 4]
        program[s] = program[a] * program[b]
        pointer += 4

    return pointer


def pair_finder(program):
    for i, j in product(range(100), repeat=2):
        if run(program.copy(), i, j) == 19690720:
            return 100 * i + j


def run(program, a, b):
    program[1] = a
    program[2] = b
    pointer = 0
    while program[pointer] != 99:
        pointer = opcodes(program, pointer)

    return program[0]


def main(inp):
    program = [int(i) for i in inp.split(',')]


    return run(program.copy(), 12, 2), pair_finder(program)
                    