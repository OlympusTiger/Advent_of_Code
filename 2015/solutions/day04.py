from hashlib import md5

def find_n(inp,n):
    h=''

    i=0
    while h[:n]!=n*'0':
        i+=1
        x=f'{inp}{i}'
        h=md5(x.encode()).hexdigest()
    return i
def main(inp):
    
    return find_n(inp,5),find_n(inp,6)