import re

def main(inp):
    points = [{'p': [a, b], 'v': [c, d]} for a, b, c, d in map(lambda x: list(map(int, re.findall(r'-?\d+', x))), inp.splitlines())]
    
    i = 0
    while True:
        i += 1
        for point in points:
            point['p'][0] += point['v'][0]
            point['p'][1] += point['v'][1]
        
        min_x = min(point['p'][0] for point in points)
        min_y = min(point['p'][1] for point in points)
        max_x = max(point['p'][0] for point in points)
        max_y = max(point['p'][1] for point in points)
        
        if max_y - min_y <= 12:

            if min_x > 0:
                x = -min_x
            else:
                x = min_x

            if min_y > 0:
                y = -min_y
            else:
                y = min_y
            for point in points:
                point['p'][0] += x
                point['p'][1] += y
            grid = [['.' for _ in range(max_x + x + 1)] for _ in range(max_y + y + 1)]
            for point in points:
                grid[point['p'][1]][point['p'][0]] = '#'
            print(*(''.join(row) for row in grid), sep='\n')
            break
    return None, i
                
