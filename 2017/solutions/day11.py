from collections import Counter

def distance(d):
    c=Counter(d)
    v1=c['n']-c['s']      
    v2=c['ne']-c['sw']
    v3=c['nw']-c['se']
    
    loc=(directions['n'][0]*v1+directions['ne'][0]*v2+directions['nw'][0]*v3,directions['n'][1]*v1+directions['ne'][1]*v2+directions['nw'][1]*v3)
    r=loc[0]+loc[1]-loc[0]*0.5
    return r
def main(inp):
    global directions
    directions={'n':(0,1),'s':(0,-1),'ne':(1,0.5),'nw':(-1,0.5),'se':(1,-0.5),'sw':(-1,-0.5)}
    
    d=inp.split(',')
    mem=set()
    for i in range(len(d)):
        mem.add(distance(d[:i]))

    


    return distance(d),max(mem)
                