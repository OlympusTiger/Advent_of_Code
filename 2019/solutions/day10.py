from general import Grid
from itertools import chain,zip_longest
from math import atan2,degrees
from collections import defaultdict



def slope(a,b):
    angle = (180-degrees(atan2(b[1]-a[1],b[0]-a[0])))
    return angle


#@snoop
def main(inp):
    grid = Grid.from_txt_file(inp)
    asteroids=grid._find('#','X')
    all_centres={}
    for aster in asteroids:
        inline=defaultdict(list)
        for ast in asteroids:
            if aster!=ast:
                angle = slope(aster,ast)
                dist = abs(aster[0]-ast[0])+abs(aster[1]-ast[1])
                inline[angle].append((ast,dist))
        all_centres[aster]=inline
    best_loc = max(all_centres,key=lambda x:len(all_centres[x].values()))
    targets = sorted(all_centres[best_loc].items(),key=lambda x:x[0])
    targets = map(lambda x:x[1],targets)
    targets = map(lambda x:sorted(x,key=lambda y:y[1]),targets)
    zipped = [i[0] for i in chain(*zip_longest(*targets)) if i is not None]
#LOL    zipped = [i[0] for i in chain(*zip_longest(*map(lambda x: sorted(x, key=lambda y: y[1]), map(lambda x: x[1], sorted(all_centres[best_loc].items(), key=lambda x: x[0]))))) if i is not None]
    th200=zipped[199]

    return len(all_centres[best_loc]),th200[1]*100+th200[0]
                    