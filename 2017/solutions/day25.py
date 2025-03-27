


def main(inp):
    start=[i for i in inp.split('\n\n')]
    begin=start[0].splitlines()
    starting_state=ord(begin[0].split()[-1].strip('.'))-65
    total_steps=int(begin[1].split()[-2].strip('.'))
    
    states=start[1:]

    guide=[]
    for s in states:
        temp={}
        lines=s.splitlines()
        for i in range(2):
            current=1 if '1' in lines[i*4+1] else 0
            to_write=1 if '1' in lines[i*4+2] else 0
            direction=1 if 'right' in lines[i*4+3] else -1
            next_state=ord(lines[i*4+4].split()[-1].strip('.'))-65
            temp[current]=[to_write,direction,next_state]

        guide.append(temp)
    tape=[0]
    i=0
    state=starting_state
    for x in range(total_steps):
        c=tape[i]
        tape[i]=guide[state][tape[i]][0]
        i+=guide[state][c][1]
        if i<0:
            tape.insert(0,0)
            i=0
        elif i>=len(tape):
            tape.append(0)
        state=guide[state][c][2]


    return sum(tape),None
                