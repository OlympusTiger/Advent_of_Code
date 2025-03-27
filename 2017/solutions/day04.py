from collections import Counter


def main(inp):
    c1=0
    c2=0
    for i in inp.splitlines():
        pas=i.split()
        if set(Counter(pas).values())=={1}:
            c1+=1
            coun=[sorted(Counter(x)) for x in pas]
            if all(coun.count(x)==1 for x in coun):
                c2+=1

        
        


    return c1,c2
                