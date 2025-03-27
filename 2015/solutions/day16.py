import re


def special(sue,tape,th,n):
	if th in['trees','cats']:
		if sue[n][th]>tape[th]:
			return True
	if th in ['pomeranians','goldfish']:
		if sue[n][th]<tape[th]:
			return True 
	return False 
def search_p2(sue,tape):
    
    for s in sue:
        if all(sue[s][i]==tape[i] if i not in['trees','cats','pomeranians','goldfish'] else special(sue,tape,i,s) for i in sue[s]):
            return s
    
def search(sue,tape):

    for s in sue:
          if all(sue[s][i]==tape[i] for i in sue[s]):
            return s
    
def main(inp):
    
    file=inp.split('\n\n')
    
    sue={}
    for i,l in enumerate(file[0].splitlines(),1):
        info=l.split(':',1)[1]
        a=re.findall('[a-z]+',info)
        b=re.findall('\d+',info)
        sue[str(i)]=dict(zip(a,b))

    msg=file[1]
    a=re.findall('[a-z]+',msg)
    b=re.findall('\d+',msg)
    tape=dict(zip(a,b))

    return search(sue,tape),search_p2(sue,tape)
