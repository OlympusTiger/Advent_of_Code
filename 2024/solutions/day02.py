from itertools import pairwise



def increasing(a,b):
    return 1<=abs(a-b)<=3 and b>a

def decreasing(a,b):
    return 1<=abs(a-b)<=3 and b<a

def fix_report(report):
    for i in range(len(report)):
        temp=report.copy()
        temp.pop(i)
        if all(increasing(a,b) for a,b in pairwise(temp)) or all(decreasing(a,b) for a,b in pairwise(temp)):
            return True
    return False


def main(inp):
    reports=[list(map(int,i.split())) for i in inp.splitlines()]
    
    safe_reports=0
    fixed_reports=0
    for report in reports:
        if all(increasing(a,b) for a,b in pairwise(report)) or all(decreasing(a,b) for a,b in pairwise(report)):
            safe_reports+=1

        else:
            if fix_report(report):
                fixed_reports+=1



    return safe_reports,fixed_reports+safe_reports
                    