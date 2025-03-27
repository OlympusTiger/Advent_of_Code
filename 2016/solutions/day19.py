
def p2(circle):   #6.5 hours i think
    i=0
    while len(circle)>1:
        p=(i+len(circle)//2)%len(circle)
        x=circle[i]
        circle.pop(p)
        i=(circle.index(x)+1)%len(circle)
    return circle[0]
def main(inp):

    circle=range(1,int(inp)+1)
    part2=p2(list(circle))
    start=True

    f=0
    while len(circle)>1:

        x=len(circle)%2
        circle=circle[f::2]
        f=f^x

            

    return circle[0],part2

