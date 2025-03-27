from collections import defaultdict


def value_finder(program, modes, param_pos, pointer, relative_base, to_save=False):
    mode = modes // (10 ** (param_pos - 1)) % 10
    if mode == 0:
        address = program[pointer + param_pos]
        if to_save:
            return address
        return program[address]
    elif mode == 1:
        address = program[pointer + param_pos]
        return address
    elif mode == 2:
        address = relative_base + program[pointer + param_pos]
        if to_save:
            return address
        return program[address]


def opcodes(program, pointer, relative_base, input):
    mode_op = program[pointer]
    op = mode_op % 100
    modes = mode_op // 100
    output = None
    if op == 1:
        a = value_finder(program, modes, 1, pointer, relative_base)
        b = value_finder(program, modes, 2, pointer, relative_base)
        save = value_finder(program, modes, 3, pointer, relative_base, to_save=True)
        program[save] = a + b
        pointer += 4
    elif op == 2:
        a = value_finder(program, modes, 1, pointer, relative_base)
        b = value_finder(program, modes, 2, pointer, relative_base)
        save = value_finder(program, modes, 3, pointer, relative_base, to_save=True)
        program[save] = a * b
        pointer += 4
    elif op == 3:
        save = value_finder(program, modes, 1, pointer, relative_base, to_save=True)
        program[save] = input
        pointer += 2
    elif op == 4:
        output = value_finder(program, modes, 1, pointer, relative_base)
        pointer += 2
    elif op == 5:
        a = value_finder(program, modes, 1, pointer, relative_base)
        if a != 0:
            pointer = value_finder(program, modes, 2, pointer, relative_base)
        else:
            pointer += 3
    elif op == 6:
        a = value_finder(program, modes, 1, pointer, relative_base)
        if a == 0:
            pointer = value_finder(program, modes, 2, pointer, relative_base)
        else:
            pointer += 3
    elif op == 7:
        a = value_finder(program, modes, 1, pointer, relative_base)
        b = value_finder(program, modes, 2, pointer, relative_base)
        save = value_finder(program, modes, 3, pointer, relative_base, to_save=True)
        if a < b:
            program[save] = 1
        else:
            program[save] = 0
        pointer += 4
    elif op == 8:
        a = value_finder(program, modes, 1, pointer, relative_base)
        b = value_finder(program, modes, 2, pointer, relative_base)
        save = value_finder(program, modes, 3, pointer, relative_base, to_save=True)
        if a == b:
            program[save] = 1
        else:
            program[save] = 0
        pointer += 4
    elif op == 9:
        a = value_finder(program, modes, 1, pointer, relative_base)
        relative_base += a
        pointer += 2
    return pointer, relative_base, output


def run(program, input):
    pointer = 0
    relative_base = 0
    while program[pointer] != 99:
        pointer, relative_base, output = opcodes(program, pointer, relative_base, input)

    return output


def main(inp):
    program = defaultdict(lambda: 0, {i: int(v) for i, v in enumerate(inp.split(','))})

    return run(program.copy(), 1), run(program.copy(), 2)

