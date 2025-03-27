import re

def main(inp):
    scan=''
    for s in inp.splitlines():
        scan+=s

    pattern='mul\(\d+,\d+\)'
    valid_muls=re.findall(pattern,scan)
    valid_sum=sum(eval(s) for s in valid_muls)
    
    split_do=scan.split('do')
    actual_valid_sum=0
    for part in split_do:
        if part.startswith('n\''):
            continue
        else:
            actual_valid_muls=re.findall(pattern,part)
            actual_valid_sum+=sum(eval(s) for s in actual_valid_muls)


    return valid_sum,actual_valid_sum
                    