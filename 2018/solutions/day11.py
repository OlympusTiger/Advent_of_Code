from itertools import product
from functools import cache
import numpy as np


sn=6303

def power(x,y):
    id=x+10
    p=id*y
    p=p+sn
    p=p*id
    p=int(str(p)[-3])
    p=p-5
    return p



def perim(x,y,k):
    return np.concatenate([arr[k+x-1,y:k+y],arr[x:k+x-1,k+y-1]]).sum()

@cache
def square(i,j,k):
    #return arr[i:i+k,j:j+k].sum()
    if k==1:
        return arr[i,j]
    return square(i,j,k-1)+perim(i,j,k)


def iterate(arr,a,b):
    sums={}
    for k in range(a,b):
        for i in range(0,300-k):
            for j in range(0,300-k):
                sums[(i+1,j+1,k)]=square(i,j,k)
    if a==3:
        return max(sums,key=lambda x:sums[x])[:-1]
    return max(sums,key=lambda x:sums[x])



def main(inp):
    global points,arr
    points=[power(x,y) for x,y in product(range(1,301),repeat=2)]

    arr=np.array(points).reshape(300,300)


            


    return iterate(arr,3,4),iterate(arr,1,301)
                    