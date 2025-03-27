
def main(inp):
    if inp[-1] == '\n':
        inp = inp[:-1]

    lines = inp.splitlines()

    answer1 = 0
    answer2 = 0
    for l in lines:
        answer1 += len(l) - len(eval(l))
        
        a=l.count('\\')
        b=l.count('"') 
        answer2 += a+b+2

    return answer1,answer2
