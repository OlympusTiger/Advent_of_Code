


def main(inp):
    firewall={int(i.split(': ')[0]):int(i.split(': ')[1]) for i in inp.splitlines()}
    severity=0
    for l in firewall:
        loc=list(range(firewall[l]))+list(range(firewall[l]-2,0,-1))
        if loc[l%len(loc)]==0:
            severity+=l*firewall[l]     
    i=0
    while True:
        if all((loc:=list(range(firewall[l]))+list(range(firewall[l]-2,0,-1))) and  loc[(l+i)%len(loc)]!=0 for l in firewall):
            break
        i+=1

    return severity,i
                