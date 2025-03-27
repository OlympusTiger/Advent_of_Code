from itertools import permutations,combinations_with_replacement
import re
from functools import reduce






def recipe(prop,spoons,Part2):			
	scores=[]

	for s in spoons:
		for p in permutations(s):
			total=[]
			c=[p[i]* pr for i,pr in enumerate(prop[4])]

			if sum(c)!=500 and Part2:
				continue
			for i in range(4):
				t=[p[i]* pr for i,pr in enumerate(prop[i])]
				if sum(t)<=0:
					break
				else:
					
					total.append(sum(t))
			else:
				
				scores.append(reduce(lambda x,y: x*y,total))
	return max(scores)
		
def main(inp):
    prop=[list(map(int,re.findall('-?\d+',i))) for i in inp.splitlines()]
    prop=list(zip(*prop))
    spoons=[]
    for p in combinations_with_replacement(range(100),len(prop[0])):	
        if sum(p)==100:
            spoons.append(p)
    return recipe(prop,spoons,False),recipe(prop,spoons,True)