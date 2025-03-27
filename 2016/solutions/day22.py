from itertools import permutations
import re
import heapq
from copy import deepcopy
from uuid import uuid1



def move(nod,n,nxt,to_move):
	for i in to_move:
		nod[nxt][1].append(i)

		nod[n][1].remove(i)
	for n in nod:
		if target in nod[n][1]:
			l=sum(n)

	return l,nod


def adjent(n):
	l=[(0,1),(0,-1),(1,0),(-1,0)]
	for t in l:
		i,j=t
		if i!=j:
			if 0<=i+n[0]<=max_x and 0<=j+n[1]<=max_y:

				yield (i+n[0],j+n[1])


def free_space(n,node):
	for a in adjent(n):
		
		for i in node[n][1]+[node[n][1]]:
			if isinstance(i,(int,str)):

				if int(i)<=node[a][0]-sum(map(int,node[a][1])):

					yield (a,[i])
			elif len(i)>=2:
				if sum(map(int,i))<=node[a][0]-sum(map(int,node[a][1])):

					yield (a,i)

		




def access(nodes):
	global max_x,max_y,target

	
	max_x=max(map(lambda x:x[0],nodes.keys()))
	max_y=max(map(lambda x:x[1],nodes.keys()))
	
	goal=(max_x,0)
	print(max_x,max_y,goal)
	target=str(nodes[goal][1][0])
	print(nodes[goal])
	nodes[goal][1][0]=str(nodes[goal][1][0])
	

	queue=[]
	for n in nodes:
		for f in free_space(n,nodes):
			nxt,tera=f
			l,gr=move(deepcopy(nodes),n,nxt,tera)
			heapq.heappush(queue,(1,-l,uuid1(),gr))

	visited=set()
	while queue:
	
		steps,_,_,grid=heapq.heappop(queue)
	
		if repr(grid) in visited:
			continue
		
		visited.add(repr(grid))
		if target in grid[(0,0)][1]:
			return steps

		for n in grid:

			for f in free_space(n,grid):
				
				nxt,tera=f
				l,gr=move(deepcopy(grid),n,nxt,tera)
				heapq.heappush(queue,(steps+1,-l,uuid1(),gr))
		


		
from collections import Counter
def valid_pairs(nodes):
	total=0

	for a,b in permutations	(nodes.keys(),2):
		if nodes[a][1]<=nodes[b][2] and nodes[a][3]!=0:
			total+=1


	return total

#20+29+1++31*5
def main(inp):
	

#         (x, y): [size, used, available, use%]
	data=[list(map(int,re.findall('\d+',i))) for i in inp.splitlines()[2:]]
	
	nodes={(x[0],x[1]):x[2:] for x in data}

	gdata={(x[0],x[1]):str(x[3])+'/'+str(x[2]) for x in data}

	grid=[[]for _ in range(29+1)]
	for x in gdata:
		i,j=x
		grid[j].append(gdata[x])
		
	print(*grid,sep='\n')
	#20+29+1+31*5=205

	
	nodes2={(x[0],x[1]):[x[2],[x[3]]] if x[3]!=0 else [x[2],[]] for x in data}

	return valid_pairs(nodes),20+29+1+31*5