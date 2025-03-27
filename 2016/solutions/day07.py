import re
from more_itertools import sliding_window,distribute

def ssl_check(outer,inner):
    v=[]
    for out in outer:
        v.extend([(c[1],c[0],c[1])  for c in sliding_window(out,3) if c[0]==c[2] and c[0]!=c[1]])
    for x in v: 
        if any(x in sliding_window(inn,3) for inn in inner):
            return 1
    return 0

def tls_check(outer,inner):
    
    if any(any((c[0],c[1])==(c[3],c[2]) and c[0]!=c[1] for c in sliding_window(out,4))for out in outer):
        if all(all((c[0],c[1])!=(c[3],c[2]) or len(set(c))==1 for c in sliding_window(inn,4))for inn in inner):
            return 1
    return 0


def main(inp):
    ip_list=inp.splitlines()
    tls=0
    ssl=0
    for ip in ip_list:
        div=re.split('\[|\]',ip)
        outer,inner=distribute(2,div)
        outer=list(outer)
        inner=list(inner)
        tls+=tls_check(outer,inner)
        ssl+=ssl_check(outer,inner)

    return tls,ssl
