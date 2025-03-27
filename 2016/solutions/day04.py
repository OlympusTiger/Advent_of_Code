from collections import Counter
from itertools import takewhile

def search(rooms,p2):
    real=[]
    for r in rooms:
        msg=list(takewhile(lambda x: x.isalpha(),r.replace('-','')))
      
        c=Counter(list(msg))
        
        s=sorted(c,key=lambda x:(-c[x],x))[:5]
        
        if ''.join(s)==r[-6:-1]:	
            
            n=int(''.join(filter(lambda x:x.isdigit(),r)))
            new=[chr(97+(ord(i)-97+n)%26) for i in msg]
            
            if p2 and 'northpole' in ''.join(new):
                print(new)
                return n
            real.append(n)
    return sum(real)

def main(inp):
    rooms=inp.splitlines()
    
    return search(rooms,False),search(rooms,True)