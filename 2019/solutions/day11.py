from collections import defaultdict
from general import Grid

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


DIRECTIONS = Grid.adjacency_map(False)

def run(program, start_color):
    ship = defaultdict(lambda: 0, {(0, 0): start_color})
    position = (0, 0)
    dir = 2
    pointer = 0
    relative_base = 0
    paint = True
    painted_panels = set()
    while program[pointer] != 99:
        pointer, relative_base, output = opcodes(program, pointer, relative_base, ship[position])
        if output is not None:
            if paint:
                ship[position] = output
                painted_panels.add(position)
                paint = False
            else:
                turn = output or -1
                dir = (dir + turn) % 4
                position = Grid.move(position, DIRECTIONS[dir])
                paint = True

    if start_color == 0:
        return len(painted_panels)

    min_x = min(map(lambda x: x[0], ship))
    max_x = max(map(lambda x: x[0], ship))
    min_y = min(map(lambda x: x[1], ship))
    max_y = max(map(lambda x: x[1], ship))
    whites = [Grid.move(p,(min_x,min_y,-1)) for p in ship if ship[p] == 1]
    grid = Grid.from_points(whites, max_x - min_x + 1, max_y - min_y + 1, '.', '#')
    return grid



def main(inp):
    program = defaultdict(lambda: 0, {i: int(v) for i, v in enumerate(inp.split(','))})

    return run(program.copy(), 0), run(program.copy(), 1)
