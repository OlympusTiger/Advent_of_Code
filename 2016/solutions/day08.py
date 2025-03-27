import re
from numpy import roll,count_nonzero,hsplit,full


def encode(lcd,seq):
    for s in seq:
        a,b=map(int,re.findall('\d+',s))
        if 'rect' in s:
            lcd[:b,:a]='#'
        elif 'row' in s:
            lcd[a,:]=roll(lcd[a,:],b)
        elif 'column' in s:
            lcd[:,a]=roll(lcd[:,a],b)

    for i in hsplit(lcd,10):
        print(i)
        print()
    return count_nonzero(lcd=='#')


            


def main(inp):
    seq=inp.splitlines()
    lcd=full((6,50),'.')

    return encode(lcd,seq),None
