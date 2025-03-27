import re


def main(inp):
    words=inp.splitlines()
    mp={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    patt='|'.join(mp.keys())+'|'+'|'.join(mp.values())
    
    p1=0
    p2=0
    for w in words:
        a1=re.search('\d',w).group()
        b1=re.search('\d',w[::-1]).group()
        n=a1+b1
        p1+=int(n)

        a2=re.search(patt,w).group()
        a2=mp.get(a2,a2)
        b2=re.search(patt[::-1],w[::-1]).group()
        b2=mp.get(b2[::-1],b2[::-1])
        n=a1+b2
        p2+=int(n)


    return p1,p2
                    