from shapely import Polygon


def main(inp):
    guide1=[x.split() for x in inp.splitlines()]
    heading1={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    pos=(0,0)
    corners1=[]
    for g in guide1:
        pos=tuple(map(lambda x:x[0]+x[1]*int(g[1]), zip(pos, heading1[g[0]])))
        corners1.append(pos)
    shape1=Polygon(corners1)


    guide2=[x.split()[-1] for x in inp.splitlines()]
    heading2={'0':(0,1),'2':(0,-1),'3':(-1,0),'1':(1,0)}
    guide2=[(int(g[2:7],16),heading2[g[-2]]) for g in guide2]
    corners2=[]
    for g in guide2:
        pos=tuple(map(lambda x:x[0]+x[1]*int(g[0]), zip(pos, g[1])))
        corners2.append(pos)
    shape2=Polygon(corners2)
            

    return int(1+shape1.area+shape1.length/2),int(1+shape2.area+shape2.length/2)
                    