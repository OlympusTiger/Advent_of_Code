def main(inp):
  
    floor=0
    for i in range(len(inp)):
        if floor==-1:
            break
        if inp[i]=='(':
            floor+=1
        else:
            floor-=1
    return inp.count('(')-inp.count(')'),i