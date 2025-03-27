from hashlib import md5

def hash_md5(id,p2):
    open=list(map(str,range(8)))
    p=[None]*8
    i=0
    while open:
        x=id+str(i)
        h=md5(x.encode()).hexdigest()
        if h.startswith('00000'):
            if p2 and h[5] in open:
                open.remove(h[5])
                p[int(h[5])]=h[6]
            elif not p2:
                open.pop(0)
                p.remove(None)
                p.append(h[5])
                
        i+=1
    return ''.join(p)

    



def main(inp):

       
    return hash_md5(inp,False),hash_md5(inp,True)