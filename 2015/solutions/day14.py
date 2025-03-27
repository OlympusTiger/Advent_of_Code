import re


def part1(deer,pos,t=2503,d=0):

    if t>deer[1]:

        pos+=[d+i*deer[0] for i in range(1,deer[1]+1)]
        d+=deer[0]*deer[1]
        t=t-deer[1]
        
    else:
        return d+t*deer[0],pos+[d+i*deer[0] for i in range(1,t+1)]
    
    if t>deer[2]:
        pos+=[d for i in range(deer[2])]
        return part1(deer,pos,t-deer[2],d)
    else:
        return d,pos+[d for i in range(t)]


        


def main(inp):
    deers=[list(map(int,re.findall('\d+',i))) for i in inp.splitlines()]

    distances=[]
    positions=[]
    for deer in deers:
        pos=[]
        d,pos=part1(deer,pos)
        distances.append(d)
        positions.append(pos)
   
    
    points=[0]*len(deers)
    for i in zip(*positions):
        for j in range(len(i)):
            if i[j]==max(i):
                points[j]+=1




    return max(distances),max(points)