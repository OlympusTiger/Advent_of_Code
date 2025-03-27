from itertools import chain
from more_itertools import chunked


def valid(x):
	m=max(x)	
	x.remove(m)	
	if sum(x)>m:
		return True
	return False

def find_triangles(triangles):
    possible=0
    for i in triangles:

        possible+=valid(list(i))
        
    return possible

def main(inp):
    horiz=list(map(lambda x:list(map(int,x.split())),inp.splitlines()))
    vert=chunked(chain(*map(list,zip(*horiz))),3)


    return find_triangles(horiz),find_triangles(vert)