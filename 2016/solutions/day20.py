
def lowest(ips):
    
    possible=sorted(list(map(lambda x:x[1]+1,ips)))
    for p in possible:
        if any(x[0]<=p<=x[1] for x in ips):
            continue
        else:
            return p


       
def total(ips):
    r=4294967295+1
    excude=[]
    for i in ips:
        for e in excude:
            if e[0]<=i[0]<=e[1] and e[0]<=i[1]<=e[1]:
                break
            elif i[0]<e[0] and i[1]>e[1]:
                excude.remove(e)
                excude.append([i[0],i[1]])
                break
            elif i[0]<e[0] and e[0]<=i[1]<e[1]:

                excude.remove(e)
                excude.append([i[0],e[1]])
                break
            elif e[0]<=i[0]<=e[1] and i[1]>e[1]:

                excude.remove(e)
                excude.append([e[0],i[1]])
            elif i[0]<e[0] and i[1]<e[0]:

                excude.append(i)
                break
            elif i[0]>e[1] and i[1]>e[1]:
                excude.append(i)
                break
        else:
            excude.append(i)
    excude.sort()
    
    x=0
    while x!=len(excude):
        x=len(excude)
        for i in range(len(excude)):
            for j in range(len(excude)):
                if i!=j:
                    if excude[j][0]<=excude[i][0]<=excude[j][1] and excude[j][0]<=excude[i][1]<=excude[j][1]:
                        excude.pop(i)
                        break
                    elif excude[i][0]<excude[j][0] and excude[j][1]<excude[i][1]:
                        excude.pop(j)
                        break
                    elif excude[i][0]<=excude[j][0]<=excude[i][1] and excude[i][1]<excude[j][1]:
                        excude[j]=[excude[i][0],excude[j][1]]
                        excude.pop(i)
                        break
                    elif excude[j][0]<=excude[i][0]<=excude[j][1] and excude[j][1]<excude[i][1]:
                        excude[i]=[excude[j][0],excude[i][1]]
                        excude.pop(j)
                        break
            else:
                continue
            break

    ex=map(lambda x:x[1]-x[0]+1,excude)
    return r -sum(ex)

def main(inp):
    ips=[list(map(int,x.split('-'))) for x in inp.splitlines()]

    
    
    

    return lowest(ips),total(ips)