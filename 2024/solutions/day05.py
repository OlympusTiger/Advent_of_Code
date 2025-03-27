from itertools import combinations

def part1(rules,update):
    for i,j in combinations(update,2):
        if [j,i] in rules:
            return 0
    return update[len(update)//2]




def part2(rules,update):
    ind=0
    new=[update.pop(0)]
    while update:
        x=update.pop(0)
        move_to_back=True
        s=0
        for n in new:
            if [x,n] in rules:
                move_to_back=False
                if new.index(n)>=s:
                    s=new.index(n)+1
            elif [n,x] in rules:
                move_to_back=False
                if new.index(n)<s:
                    s=new.index(n)
        if move_to_back:
            update.append(x)
            continue
        ind+=1
        new.insert(s,x)
    return new[len(new)//2]


def main(inp):
    rules,updates=inp.split('\n\n')
    rules=[list(map(int,i.split('|'))) for i in rules.splitlines()]
    updates=[list(map(int,i.split(','))) for i in updates.splitlines()]         

    correct=0
    fixed=0
    for update in updates:
        s=part1(rules,update)
        if s:
            correct+=s
        else:

            fixed+=part2(rules,update)
        

    

    return correct,fixed
                    