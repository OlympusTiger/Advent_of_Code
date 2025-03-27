


def main(inp):
    masses=list(map(int,inp.splitlines()))
    s1=0
    s2=0
    for mass in masses:
        s1+=mass//3-2

    for mass in masses:
        while mass//3-2>0:
            mass=mass//3-2
            s2+=mass
    
    return s1,s2  
                    