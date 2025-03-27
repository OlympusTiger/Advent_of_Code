from itertools import pairwise


def main(inp):
    
    nums=list(map(int,list(inp.strip())))
    t1=0
    for x in pairwise(nums):
        if x[0]==x[1]:
            t1+=x[0]
    if nums[0]==nums[-1]:
        t1+=nums[0]


    l=len(nums)
    t2=0
    for i in range(l):
        if nums[i]==nums[int((i+(l/2))%l)]:
            t2+=nums[i]
    

    return t1,t2
                