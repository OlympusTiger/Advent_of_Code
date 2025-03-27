

def react(mol,c=None):
    l=len(mol)
    new_l=0
    while l!=new_l:

        l=new_l or l

        for i in range(l-1,0,-1):
            try:
                if mol[i-1].lower()==mol[i].lower() and mol[i-1]!= mol[i]:
                    mol.pop(i-1)
                    mol.pop(i-1)
            except IndexError:
                pass
        new_l=len(mol)
    if c:
        mol=[x for x in mol if x.lower()!=c]
        return react(mol)
    return mol

def main(inp):
    mol=list(inp)
    # l=len(mol)
    # print(l)
    # new_l=0
    # while l!=new_l:

    #     l=new_l or l

    #     for i in range(l-1,0,-1):
    #         try:
    #             if mol[i-1].lower()==mol[i].lower() and mol[i-1]!= mol[i]:
    #                 mol.pop(i-1)
    #                 mol.pop(i-1)
    #         except IndexError:
    #             pass

    sizes=[]

    for i in range(ord('a'),ord('z')+1):
        # mol_n=[x for x in mol if x.lower()!=chr(i)]

        sizes.append(len(react(mol,chr(i))))

    return  len(react(mol)),min(sizes)
                    