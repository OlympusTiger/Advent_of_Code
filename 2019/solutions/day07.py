from itertools import permutations,cycle


class Amps:
    def __init__(self,program,inputs):
        self.program = program
        self.pointer = 0
        self.inputs = inputs

    @property
    def instructions(self):
        return self.program[self.pointer]




def value_finder(program,modes,param_pos,pointer,to_save=False):
    mode = modes//(10**(param_pos-1))%10
    if mode == 0:
        if to_save:
            return program[pointer+param_pos]
        return program[program[pointer+param_pos]]
    elif mode == 1:
        return program[pointer+param_pos]
         




def opcodes(program, pointer, inputs):
    mode_op = program[pointer]
    op = mode_op%100
    modes = mode_op//100
    output = None 
    if op == 1:
        a = value_finder(program,modes,1,pointer)
        b = value_finder(program,modes,2,pointer)
        save=value_finder(program,modes,3,pointer,to_save=True)
        program[save] = a + b
        pointer += 4
    elif op == 2:
        a = value_finder(program,modes,1,pointer)
        b = value_finder(program,modes,2,pointer)
        save=value_finder(program,modes,3,pointer,to_save=True)
        program[save] = a * b
        pointer += 4
    elif op == 3:
        if not inputs:
            return pointer, False
        save=value_finder(program,modes,1,pointer,to_save=True)
        program[save] = inputs.pop(0)
        pointer += 2
    elif op == 4:
        output = value_finder(program,modes,1,pointer)
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
        save=value_finder(program,modes,3,pointer,to_save=True)
        if a<b:
            program[save] = 1
        else:
            program[save] = 0
        pointer += 4
    elif op == 8:
        a = value_finder(program,modes,1,pointer)
        b= value_finder(program,modes,2,pointer)
        save=value_finder(program,modes,3,pointer,to_save=True)
        if a==b:
            program[save] = 1
        else:
            program[save] = 0
        pointer += 4
    return pointer,output


def run(program,inputs):
    pointer = 0
    while program[pointer] != 99:
        pointer,output = opcodes(program, pointer,inputs)
    return output


def run_feedback(config):
    program,pointer,inputs = config
    outputs=[]
    while program[pointer] != 99:
        pointer,output = opcodes(program, pointer, inputs)
        if output is not None and output is not False: 
            outputs.append(output)
        elif output == False:  
            return program,pointer,inputs,outputs
    return program,pointer,inputs,outputs



def straight_feed(program):
    thrusts=[]
    for phases in permutations(range(5)):
        output=0
        for phase in phases:
            output = run(program.copy(),[phase,output])
        thrusts.append(output)
    return max(thrusts)


def feedback_loop(program):
    thrusts=[]
    for phases in permutations(range(5,10)):
        thrust=0
        amps_config = [[program.copy(),0,[phase]] for phase in phases]
        amps_config[0][2].append(0)
        for i in cycle(range(5)):
            if all(amps_config[a][0][amps_config[a][1]]==99 for a in range(5)):
                thrusts.append(thrust)
                break
            *amps_config[i],outputs=run_feedback(amps_config[i])
            thrust=max(outputs)
            amps_config[(i+1)%5][2].extend(outputs)

    return(max(thrusts))
        
        
        


def main(inp):
    program = [int(i) for i in inp.split(',')]


    return straight_feed(program),feedback_loop(program)
                    