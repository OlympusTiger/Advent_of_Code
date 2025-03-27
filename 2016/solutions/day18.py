
def is_safe(a,b,c):
    return not int(c!=a==b==0 or a!=b==c==0 or c!=a==b==1 or a!=b==c==1)

    
def next_floor(floor,n):
    floor.append([])
    for i in range(len(floor[0])):
        if i==0:
            floor[n+1].append(is_safe(1,floor[n][i],floor[n][i+1]))
        elif i==len(floor[0])-1:
            floor[n+1].append(is_safe(floor[n][i-1],floor[n][i],1))
        else:  
            floor[n+1].append(is_safe(floor[n][i-1],floor[n][i],floor[n][i+1]))
    return floor


def main(inp):
    floor=[[0 if i=='^' else 1 for i in inp]]
    n=0
    while n<40-1:     #  #40 or #40000
        floor=next_floor(floor,n)
        n+=1

    return sum(map(sum,floor)),None