import re
from functools import partial
def parse_step(step):
    lens=re.search('[a-z]+',step).group()
    return convert_steps(lens),lens,re.search('(-|\d)',step).group()

def convert_steps(step):
    def hash_alg(char,start):
        return ((start+ord(char))*17)%256

    res=0
    for i in step:
        res=hash_alg(i,res) 
    return res

def check_box(boxes,b,l,f):
    if f.isdigit():        
        boxes[b][l]=int(f)
    else:
        boxes[b].pop(l, None)
    return

def box_power(boxes,b):

    power=0
    for i,k in enumerate(list(boxes[b].keys()),1):
        power+=(b+1)*i*boxes[b][k]
    return power


def main(inp):
    sequence = inp.split(',')

    boxes = [{} for i in range(256)]
    for s in sequence:
        box,lens,focal=parse_step(s)
        check_box(boxes,box,lens,focal)       

    return sum(map(convert_steps,sequence)),sum(map(partial(box_power,boxes),range(256)))
                    