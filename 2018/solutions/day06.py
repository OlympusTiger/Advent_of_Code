from itertools import product

def region(x,co):
    print(x)
    i=0
    d=set(product(range(-i, i+1), repeat=2))
    passed = {(0, 0)}
    points=[]

    while d:
        for p in d:
      
            g = (p[0] + x[0], p[1] + x[1])
            new=[abs(g[0]-k[0])+abs(g[1]-k[1]) for k in co]
            if all(j>391 for j in new):
                return len(set(points))
            if sum(new)<10000:
                points.append(p)

        passed.update(d)

        i += 1
        d = set(product(range(-i, i+1), repeat=2)) - passed
        

def plane(x, co):


    i = 1
    d = set(product(range(-i, i+1), repeat=2))
    passed = {(0, 0)}

    closer = []


    while d:
        to_append = []
        for p in d:
            g = (p[0] + x[0], p[1] + x[1])
            
            if (g[0] < minx or g[1] < miny or g[0] > maxx or g[1] > maxy)and all(abs(p[0]) + abs(p[1]) < abs(k[0] - g[0]) + abs(k[1] - g[1]) for k in co):
                return 0

            if all(abs(p[0]) + abs(p[1]) < abs(k[0] - g[0]) + abs(k[1] - g[1]) for k in co):
                to_append.append(p)

        if to_append:
            closer.extend(to_append)
        else:
            break

        passed.update(d)

        i += 1
        d = set(product(range(-i, i+1), repeat=2)) - passed

    return len(set(closer))


def main(inp):
    global maxx, maxy, minx, miny
    coords = [tuple(map(int, i.split(', '))) for i in inp.splitlines()]
    finite = []
    for co in coords:
        i, j = co
        try:
            a = min([x for x in coords if x != (i, j) and i <= x[0] and j <= x[1]],
                    key=lambda y: abs(y[0] - i) + abs(y[1] - j))
            b = min([x for x in coords if x not in [(i, j), a] and i >= x[0] and j <= x[1]],
                    key=lambda y: abs(y[0] - i) + abs(y[1] - j))
            c = min([x for x in coords if x not in [(i, j), a, b] and i <= x[0] and j >= x[1]],
                    key=lambda y: abs(y[0] - i) + abs(y[1] - j))
            d = min([x for x in coords if x not in [(i, j), a, b, c] and i >= x[0] and j >= x[1]],
                    key=lambda y: abs(y[0] - i) + abs(y[1] - j))
            finite.append((co, [a, b, c, d]))
        except ValueError:
            continue
    maxy = max(map(lambda x: x[1], coords))
    maxx = max(map(lambda x: x[0], coords))
    miny = min(map(lambda x: x[1], coords))
    minx = min(map(lambda x: x[0], coords))
    print(maxx, minx, maxy, miny)
    center=(maxx-minx,maxy-miny)

    areas = [plane(x[0], coords.copy()) for x in finite]

    return None, region(center, coords.copy())
