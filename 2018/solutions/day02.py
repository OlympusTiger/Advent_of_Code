from collections import Counter

def main(inp):

    IDs=sorted(inp.splitlines())
    print(len(IDs[0]))
    twos=0
    threes=0

    for ID in IDs:
        c=Counter(ID)
        if 2 in c.values():
            twos+=1
        if 3 in c.values():
            threes+=1
        
    IDs+=sorted(IDs,key=lambda x:x[1])
    for i in range(len(IDs)-1):
        d=[]
        for j in range(len(IDs[i])):
            if IDs[i][j]!=IDs[i+1][j]:
                d.append(j)

        if len(d)==1:
            IDs[i]=IDs[i][:d[0]]+IDs[i][d[0]+1:]
            break


    return twos*threes,IDs[i]
                    