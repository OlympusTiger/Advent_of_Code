import re
import json
from benedict import benedict

def dig(cont,path):
    if isinstance(cont,dict) and 'red' in cont.values():
        paths.append(path)
        return
    if isinstance(cont,(int,str)):
        return
    if isinstance(cont,dict):
        for k in cont:
            dig(cont[k],path+[k])
    if isinstance(cont,list):
        for i in range(len(cont)):
            dig(cont[i],path+[i])



    

def main(inp):
    global data,paths
    paths=[]
    nums1=re.findall('-?\d+',inp)

    data=json.loads(inp)
    data=benedict(data)
    for k in data:
        dig(data[k],[k])

    for p in paths:
        data[*p]=0
        
    nums2=re.findall('-?\d+',str(data))

    return sum(map(int,nums1)),sum(map(int,nums2))