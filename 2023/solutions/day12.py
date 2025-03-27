from functools import cache
import re

@cache
def match_next(spr,nums): 
    combs=0
    for i,_ in enumerate(spr):
        if nums and '#' not in spr[0:i] and len(spr[i:])>=nums[0]:
            if '.' not in spr[i:i+nums[0]] and (len(spr)==nums[0]+i or spr[nums[0]+i]!='#'):
                if len(nums)==1 and (len(spr)==nums[0]+i or '#' not in spr[nums[0]+i:]):
                    combs+=1                                                    
                    continue
                else:
                    combs+=match_next(spr[nums[0]+i+1:],nums[1:])
                    continue
            else:
                continue
        else:
            return combs
    return combs

def arrangements(field,modifier=1):
    c=0
    for _,f in enumerate(field):
        new=f[0]+('?'+f[0])*(modifier-1)
        n=f[1]*modifier
        b=match_next(new,n)
        c+=b
    return c

def main(inp):
    field=[i.split() for i in inp.splitlines()]
    field=list(map(lambda x: [x[0],tuple(map(int,x[1].split(',')))],field))
    for i in range(len(field)):
        field[i][0]=re.sub('\.+','.',field[i][0])     


    return arrangements(field),arrangements(field,5)
                    