

def main(inp):
    r=3010
    c=3019
        
    pos=sum(range(r-1))+c*r+sum(range(c))

    code=20151125
    for _ in range(pos-1):
        code=(code*252533)%33554393
    return code,None