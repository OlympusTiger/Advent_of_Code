from itertools import product


def main(inp):
    
    claimed=set()
    dups=set()
    common=0
    d={}
    for l in inp.splitlines():
        id,_,edges,size=l.split()
        x,y= map(int,edges.strip(':').split(','))
        size_x,size_y=map(int,size.split('x'))
        rect=set(product(range(x,x+size_x),range(y,y+size_y)))
        d[id[1:]]=rect
        for i in rect:
            if i in claimed and i not in dups:
                common+=1
                dups.add(i)
            else:
                claimed.add(i)
             
    for i in d:
        if not d[i]&dups:
            alone=i



        

            


    return common,alone
                    