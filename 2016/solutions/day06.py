from collections import Counter

def jammer(pos,p2):
    m=''
    for i in pos:
        m+=Counter(i).most_common()[-p2][0]
    return m
def main(inp):
    msgs=inp.splitlines()
    pos=list(map(list,zip(*msgs)))

    return jammer(pos,0),jammer(pos,1)