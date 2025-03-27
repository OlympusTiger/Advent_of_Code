
def Part2(rules,mol):
    drules=dict(map(lambda x:x[::-1],rules))
    length=list(set(map(len,drules)))[::-1]
    t=0
    while mol!='e':	
        for i in range(len(mol)):		
            for l in length:			
                if i==0:
                    if mol[-l:]in drules:
                        mol=mol[:-l]+drules[mol[-l:]]
                        t+=1
                        break
                if mol[-l-i:-i]in drules:			
                    mol=mol[:-l-i]+drules[mol[-l-i:-i]]+mol[-i:]				
                    t+=1
                    break
            else:
                continue
            break
                
    return t
def Part1(rules,mol):
    molecules=set()

    for r in rules:
        s=mol.split(r[0])
        for i in range(1,len(s)):
            new=r[0].join(s[:i])+r[1]+r[0].join(s[i:])
            molecules.add(new)
    return len(molecules)

def main(inp):
    rule,mol=inp.split('\n\n')

    rules=[r.split(' => ') for r in rule.splitlines()]

    return Part1(rules,mol),Part2(rules,mol)