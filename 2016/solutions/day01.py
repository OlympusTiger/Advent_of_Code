import re

d=['N','E','S','W']
dir=dict.fromkeys(d,0)


def travel(steps,Part2):
    pos='N'
    loc=[0,0]
    locations=[]
    for s in steps:
        n=int(re.search('\d+',s).group())
        ind=d.index(pos)
        if s[0]=='L':
            pos=d[ind-1]
            dir[pos]+=n
        else:
            pos=d[(ind+1)%4]
            dir[pos]+=n
        if Part2:
            if pos=='N':
                for i in range(1,n+1):
                    if (a:=[loc[0],loc[1]+i]) in locations:
                        return a[0]+a[1]
                        
                    else:
                        locations.append(a)
                else:
                    loc[1]+=n
                    continue 
                
                    
                
            elif pos=='S':
                for i in range(1,n+1):
                    if (a:=[loc[0],loc[1]-i]) in locations:
                        return a[0]+a[1]
                        
                    else:
                        locations.append(a)
                else:
                    loc[1]-=n
                    continue 
                
            elif pos=='E':
                for i in range(1,n+1):
                    if (a:=[loc[0]+i,loc[1]]) in locations:
                        return a[0]+a[1]
                        
                    else:
                        locations.append(a)
                else:
                    loc[0]+=n
                    continue 
                
            
            else :
                for i in range(1,n+1):
                    if (a:=[loc[0]-i,loc[1]]) in locations:
                        return a[0]+a[1]
                        
                    else:
                        locations.append(a)
                else:
                    loc[0]-=n
                    continue 

                
    return abs(dir['S']-dir['N'])+abs(dir['W']-dir['E'])
def main(inp):
    steps=list(map(lambda x:x.strip(),inp.split()))
        


    return travel(steps,False),travel(steps,True)