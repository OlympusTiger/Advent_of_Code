

def value_finder(program,modes,param_pos,pointer):
    mode = modes//(10**(param_pos-1))%10
    if mode == 0:
        return program[program[pointer+param_pos]]
    elif mode == 1:
        return program[pointer+param_pos]
         




def opcodes(program, pointer, input):
    mode_op = program[pointer]
    op = mode_op%100
    modes = mode_op//100

    output = None 
    vals=[]
    if op == 1:
        a = value_finder(program,modes,1,pointer)
        b = value_finder(program,modes,2,pointer)
        save=program[pointer+3]
        program[save] = a + b
        pointer += 4
    elif op == 2:
        a = value_finder(program,modes,1,pointer)
        b = value_finder(program,modes,2,pointer)
        save=program[pointer+3]
        program[save] = a * b
        pointer += 4
    elif op == 3:
        save = program[pointer+1]
        program[save] = input
        pointer += 2
    elif op == 4:
        mode = modes%10
        if mode == 0:
            output = program[program[pointer+1]]
        elif mode == 1: 
            output = program[pointer+1]
        pointer += 2
    elif op == 5:
        a = value_finder(program,modes,1,pointer)
        if a != 0:
            pointer = value_finder(program,modes,2,pointer)
        else:
            pointer += 3
    elif op == 6:
        a = value_finder(program,modes,1,pointer)
        if a == 0:
            pointer = value_finder(program,modes,2,pointer)
        else:
            pointer += 3
    elif op == 7:
        a = value_finder(program,modes,1,pointer)
        b= value_finder(program,modes,2,pointer)
        s = program[pointer+3]
        if a<b:
            program[s] = 1
        else:
            program[s] = 0
        pointer += 4
    elif op == 8:
        a = value_finder(program,modes,1,pointer)
        b= value_finder(program,modes,2,pointer)
        s = program[pointer+3]
        if a==b:
            program[s] = 1
        else:
            program[s] = 0
        pointer += 4

    return pointer,output


def run(program,input):
    pointer = 0
    while program[pointer] != 99:
        pointer,output = opcodes(program, pointer,input)
        
    return output


def main(inp):
    program = [int(i) for i in inp.split(',')]

    return run(program.copy(),1), run(program.copy(),5)
                    
                    