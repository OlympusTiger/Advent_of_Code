from more_itertools import flatten
import matplotlib.pyplot as plt
def dig(grid, maxdepth, spring):
    depth, w = spring
    q = {spring}
    passed = set()
    while q:
        depth, w = q.pop()
        passed.add((depth, w))

        while depth <= maxdepth:
            
            while depth <= maxdepth and grid[depth][w] == '.':
                grid[depth][w] = '|'
                depth += 1
            if depth > maxdepth:
                break
            if grid[depth][w] in '#|~':
                depth -= 1
                
                lw = w
                lh = None
                rw = w
                rh = None
                
                to_break = False
                while lh==None or rh==None:

                    if not lh:
                        if grid[depth + 1][lw] in '~#':
                       
                            lw -= 1
                            if grid[depth][lw] == '#':
                                lh = lw
                        else:
                            to_break = True
                            lh = lw
                           


                    if not rh:
                       
                        if grid[depth + 1][rw] in '~#':
                            rw += 1
                            if grid[depth][rw] == '#':
                                rh = rw
                        else:
                            to_break = True
                           
                            rh = rw

                else:
                    if to_break:
                        
                        for a in range(lh + 1, rh):
                            grid[depth][a] = '|'
                        if grid[depth][lh] == '.' and (depth, lh) not in passed:
                            q.add((depth, lh))
                        if grid[depth][rh] == '.' and (depth, rh) not in passed:
                            q.add((depth, rh))
                        break

                if not to_break:
                  
                    for a in range(lh + 1, rh):
                        grid[depth][a] = '~'

def main(inp):
    global clay
    spring = (0, 500)
    points = set()
    plot_points = []
    clay = []
    for l in inp.splitlines():
        a, b = l.split(', ')
        k = int(a[2:])
        l = b[2:]
        if 'x' in a:
            y1, y2 = l.split('..')
            clay.append(((int(y1), int(y2)), (k, k)))
            for l in range(int(y1), int(y2) + 1):
                points.add((l, k))
                plot_points.append((k, -l))
        else:
            x1, x2 = l.split('..')
            clay.append(((k, k), (int(x1), int(x2))))
            for l in range(int(x1), int(x2) + 1):
                points.add((k, l))
                plot_points.append((l, -k))

    a1, a2, a3, a4 = (
        min(clay, key=lambda x: x[0][0])[0][0],
        max(clay, key=lambda x: x[0][1])[0][1],

        min(clay, key=lambda x: x[1][0])[1][0],
        max(clay, key=lambda x: x[1][1])[1][1],
    )
    print(a1, a2, a3, a4)
    grid = [['.' for _ in range(a4 - a3 + 3)] for _ in range(a2 + 1)]
    if 0:
       v,b=zip(*plot_points)
       plt.scatter(v,b,marker='.',linewidths=1)
       plt.plot(500,0,marker='.')
       plt.show()
    for p in points:
        grid[p[0]][p[1] - a3 + 1] = '#'
    spring = (0, 500 - a3 + 1)
    print(spring)

    maxdepth = a2
    dig(grid, maxdepth, spring)
    print(sum(1 for i in flatten(grid[a1:]) if i in '|~'))
    # a=150
    # b=600
    # 0
    # for i in range(0+b, 1000+b):
    #     print(grid[i][0+a:137+a])
    # print(*grid, sep='\n')

    return sum(1 for i in flatten(grid[a1:]) if i in '|~'), sum(1 for i in flatten(grid[a1:]) if i in '~')
