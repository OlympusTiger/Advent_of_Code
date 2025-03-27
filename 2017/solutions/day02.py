from itertools import combinations


def main(inp):
    grid=[[int(i) for i in j.split()]for j in inp.splitlines()]
    s=0
    r=0
    for i in grid:
        s+=max(i)-min(i)
        for c in combinations(i,2):
            if c[0]%c[1]==0:
                r+=c[0]//c[1]
                break
            if c[1]%c[0]==0:
                r+=c[1]//c[0]
                break

    


    return s,r
                