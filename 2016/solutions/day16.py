

def dragon(x,max_l):

    while len(x)<=max_l:
        x+='0'+''.join(['0' if i=='1' else '1' for i in x[::-1]])
    return x[:max_l]

def check_sum(x):
    while len(x)%2==0:
        x=''.join([str(int(x[i]==x[i+1]))for i in range(0,len(x),2)])
    return x
def main(inp):
    
    
    return check_sum(dragon(inp,272)),check_sum(dragon(inp,35651584))