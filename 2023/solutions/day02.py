

def part1(id,pulls):
    rr=12
    gg=13
    bb=14
    for p in pulls:
        for i in p.split(', '):
            num,color=i.split()
            if color=='red':
                if int(num)>rr:
                    return 0
            elif color =='green':
                if int(num)>gg:
                    return 0
            elif color=='blue':
                if int(num)>bb:
                    return 0
                
    return id 

def part2(pulls):
    r_max=0
    g_max=0
    b_max=0

    for p in pulls:
        for i in p.split(', '):
            num,color=i.split()
            if color=='red':
                r_max=max(r_max,int(num))
            elif color =='green':
                g_max=max(g_max,int(num))
            elif color=='blue':
                b_max=max(b_max,int(num))

    return r_max*g_max*b_max


def main(inp):
    games=inp.splitlines()

    p1=0
    p2=0
    for game in games:
        id,pulls=game.split(':')
        id =int(id.split()[1])
        pulls=pulls.split(';')
        p1+=part1(id,pulls)
        p2+=part2(pulls)

    return p1,p2
                    