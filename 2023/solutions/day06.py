from math import sqrt, ceil


def main(inp):
    lines=inp.splitlines()
    z=zip(map(int,lines[0].split()[1:]),map(int,lines[1].split()[1:]))
    p1=1
    for t in z:
        d=t[0]**2-4*t[1]
        if d<0:
            continue
        s1 = (t[0]-sqrt(d))/2
        s2 = (t[0]+sqrt(d))/2
        if int(s2)==s2 or int(s1)==s1:
            p1*=ceil(s2)-ceil(s1)-1
        else:
            p1*=ceil(s2)-ceil(s1)

    lines=[int(l[l.index(':')+1:].replace(' ','')) for l in lines]
    d=lines[0]**2-4*lines[1]
    s1 = (lines[0]-sqrt(d))/2
    s2 = (lines[0]+sqrt(d))/2
    
    if int(s2)==s2 or int(s1)==s1:
        p2=(ceil(s2)-ceil(s1)-1)
    else:
        p2=(ceil(s2)-ceil(s1))
            


    return p1,p2
                    