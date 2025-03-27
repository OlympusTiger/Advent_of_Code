from operator import eq,not_


def check_difH(mir,ind,off):
	x=map(eq,mir[ind+off],mir[ind-1-off])
	return sum(map(not_,x))
	
def check_difV(mir,ind,off):
	x=[mir[i][ind+off]!=mir[i][ind-1-off] for i in range(len(mir))]
	return sum(x)

def reflection(mirrors,smudge=0):
    vert=0
    horiz=0

    for m in mirrors:
        hor=False
        for l in range(1,len(m)):
            if check_difH(m,l,0)==smudge:	
                r=(min(l,len(m)-l))
                
                if m[l-r:l-1]==m[l+1:l+r][::-1]:
                    hor=True
                    horiz+=l*100				
                    break
            elif check_difH(m,l,0)==0 and smudge==1:
                r=(min(l,len(m)-l))
                s=[check_difH(m,l,o) for o in range(0,r)]
                if sum(s)==1:
                    hor=True
                    horiz+=l*100
                    break      
        if not hor:
            for l in range(1,len(m[0])):
                if check_difV(m,l,0)==smudge:
                    r=(min(l,len(m[0])-l))
                    s=[check_difV(m,l,o) for o in range(r)]
                    if sum(s)==smudge:						
                        vert+=l			
                        break
                elif check_difV(m,l,0)==0 and  smudge==1:	
                    r=(min(l,len(m[0])-l))
                    s=[check_difV(m,l,o) for o in range(r)]
                    if sum(s)==1:			
                        vert+=l
                        break
                        
    return vert+horiz


def main(inp):
    mirrors=[i.splitlines() for i in inp.split('\n\n')]
    

    return reflection(mirrors),reflection(mirrors,1)
                    