from hashlib import md5
from itertools import compress
dir={'U':(0,-1),'D':(0,1),'L':(-1,0),'R':(1,0)}

def hash_md5(id,pos):
    h=md5(id.encode()).hexdigest()[:4]
    mask=[i in 'bcdef' for i in h] #  [U D L R] 
    d= dict(compress(dir.items(),mask))
    for n in d:
        i=dir[n]
        new=(pos[0]+i[0],pos[1]+i[1])
        if new[0] in range(4) and new[1] in range(4):
            yield new,n


def search(code):
    queue=[]
    queue.append((0,(0,0),''))
    total=[]
    while queue:
        steps,pos,path=queue.pop()
        if pos==(3,3):
            total.append(steps)
            continue
        for n in hash_md5(code+path,pos):
            queue.insert(0,(steps+1 ,n[0],path+n[1]))
    return total


def main(inp):
    return min(search(inp)), max(search(inp))