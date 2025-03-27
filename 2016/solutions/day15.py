import re
def drop(discs):
	t=0
	while True:
		if all((d[2]+t+i)%d[0]==0 for i,d in enumerate(discs,1)):
			return t
		t+=1	

def main(inp):
	discs=[list(map(int,re.findall('\d+',i)[1:])) for i in inp.splitlines()]
	
	return drop(discs),drop(discs+[[11,0,0]])