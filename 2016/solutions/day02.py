
move={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
phone=[[[1,2,3],[4,5,6],[7,8,9]],[[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]]

def nxt(p,n,p2):
	if n[0]:
		if 0<=p[0]+n[0]<3+2*p2 and phone[p2][p[0]+n[0]][p[1]]!=0:
			p=(p[0]+n[0],p[1])
	else:
		if 0<=p[1]+n[1]<3+2*p2 and phone[p2][p[0]][p[1]+n[1]]!=0:
			p=(p[0],p[1]+n[1])
	return p

def search(instr,p2):
    digits=''
    pos=(1,1)
    for i in instr:
        for m in i:
            pos=nxt(pos,m,p2)
        digits+=str(phone[p2][pos[0]][pos[1]])
    return digits
def main(inp):
    instr=inp.splitlines()
    instr=[[move[i] for i in j.strip('\n')]for j in instr]

    return search(instr,0),search(instr,1)