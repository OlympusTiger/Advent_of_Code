from collections import Counter


def main(inp):
    lists=inp.splitlines()
    left_list=[]
    right_list=[]
    for l in lists:
        l,r=l.split()
        left_list.append(int(l))
        right_list.append(int(r))
    left_list.sort()
    right_list.sort()
    p1=sum(abs(x-y) for x,y in zip(left_list,right_list))

    l_count=Counter(left_list)
    r_count=Counter(right_list)
    p2=sum(c*l_count[c]*r_count[c] for c in l_count)
    
    return p1,p2  
                    