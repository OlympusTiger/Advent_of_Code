from collections import Counter
from itertools import product



w=25
h=6
def grid(layer):
    return [[layer[i*w+j]for j in range(w)] for i in range(h)]

def coloring(layers):
    for i,j in product(range(h),range(w)):
        for l in range(len(layers)):
            if layers[l][i][j]==0:
                layers[0][i][j]='.'
                print(layers[0])
                break
            elif layers[l][i][j]==1:
                layers[0][i][j]='#'
                break
    return layers


def main(inp):
    data = list(map(int, inp))
    layers = [data[i:i+w*h] for i in range(0,len(data),w*h)]
    counting = map(Counter,layers)
    fewest_0=min(counting,key=lambda x:x[0])
    layers = list(map(grid,layers))
    layers=coloring(layers)
    print(*layers[0],sep = '\n')

    return fewest_0[1]*fewest_0[2],None
                    