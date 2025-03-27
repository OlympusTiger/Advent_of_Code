from itertools import product
LINKS={'-':([0,1,'7J-'],[0,-1,'-FL']),'7':([1,0,'|LJ'],[0,-1,'-FL']),'J':([-1,0,'|F7'],[0,-1,'F-L']),'F':([0,1,'J-7'],[1,0,'|JL']),'L':([-1,0,'F|7'],[0,1,'-J7']),'|':([-1,0,'7F|'],[1,0,'|JL'])}
HEADINGS=[(-1,0),(0,1),(1,0),(0,-1)]
from time import sleep

def get_next(perim,k,l,p,symb):
	if  0<=k+p[0]<len(scetch[0]) and 0<=l+p[1]<len(scetch[1]):
		pos=(p[0]+k,p[1]+l)	
		prev=symb
		symbol = scetch[pos[0]][pos[1]]
		valid,i,j=valid_symbol(k,l,symbol)
		if valid:
			perim.append(pos)
			return perim,symbol,i,j,pos			
	return perim,False,None,None,None
	
def valid_symbol(k,l,s):
	k=-k
	l=-l
	if s=='S':
		return True,start[0],start[1]
	if s!='.' and [k,l] in map(lambda x:x[:2],LINKS[s]) :
		edge=list(map(lambda x: x[:2],LINKS[s]))
		edge.remove([k,l])
		return True,edge[0][0],edge[0][1]	
	return False,None,None

def move(point,direction):
    return point[0]+direction[0],point[1]+direction[1]
    
def in_bounds(point):
    return 0<=point[0]<len(scetch) and 0<=point[1]<len(scetch[0])

def get_same_space(point,perim):
    space=[]
    q=[point]
    seen={start}
    while q:
        p=q.pop(0)
        for d in HEADINGS:
            nxt=move(p,d)
            if in_bounds(nxt) and nxt not in perim and nxt not in seen:
                space.append(nxt)
                q.append(nxt)
                seen.add(nxt)
    return space
                
        

def search_edges(point,perim,incude,exclude):
    count=0
    for i in range(0,point[0]):

        for e,p in enumerate(perim):
            
            if p==(i,point[1]) and perim[e][1]!=perim[(e-1)%len(perim)][1]:
                dif1=0
                delta=e
                while dif1==0:
                    try:			
                        dif1=perim[delta][1]-perim[1+delta][1]                             
                    except IndexError:
                        dif1=perim[delta][1]-perim[0][1]
                        delta=0
                    delta+=1
                else :					
                    dif2=0
                    delta=e
                    while dif2==0:	
                        try:
                            dif2=perim[delta][1]-perim[delta-1][1]
                        except IndexError:
                            dif2=perim[delta][1]-perim[0][1]
                            delta=0						
                        delta-=1
                if dif1*dif2<0:	
                    count+=1     
    if count%2==1:
        incude.update(get_same_space(point,perim))  
    else:
        exclude.update(get_same_space(point,perim))     
    return count%2==1,incude,exclude

def main(inp):
    global start,scetch
    scetch=[i for i in inp.splitlines()]
    for i,j in product(range(len(scetch)),range(len(scetch[0]))):
        if scetch[i][j]=='S':
            start=(i,j)
    for i,j in HEADINGS:
        symbol='S'
        begin=True
        pos=start
        s=0
        steps=0
        perim=[start]
        while symbol!='S' or begin==True:
            begin=False
            perim,symbol,i,j,pos= get_next(perim,i,j,pos,symbol)
            if symbol==False:
                break
            steps+=1

        else:
            if symbol=='S':
                break
    
    i_max=max(perim,key=lambda x:x[0])[0]
    j_max=max(perim,key=lambda x:x[1])[1]
    i_min=min(perim,key=lambda x:x[0])[0]
    j_min=min(perim,key=lambda x:x[1])[1]
    d=[i for i in product(list(range(len(scetch))),list(range(len(scetch[0])))) if i not in perim and i[0]>=i_min and i[0]<=i_max and i[1]>=j_min and i[1]<=j_max]
    nests = 0
    incude=set()
    exclude=set()
    for i,j in d:
        if (i,j) in perim or (i,j) in exclude:
            continue
        if (i,j) in incude:
            nests+=1
            continue
        n,incude,exclude=search_edges((i,j),perim,incude,exclude)
        nests+=n
                
    return steps//2,nests
                    