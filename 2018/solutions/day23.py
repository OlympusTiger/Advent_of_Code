import re
from itertools import product
import heapq
from general import Manhattan
#142473501


class Sphere:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.x_min = x - r
        self.x_max = x + r
        self.y_min = y - r
        self.y_max = y + r
        self.z_min = z - r
        self.z_max = z + r

    def __repr__(self):
        return f'({self.x},{self.y},{self.z},{self.r})'

    def ranges(self):
        return ((self.x_min, self.y_min, self.z_min),
                (self.x_max, self.y_max, self.z_max))


class Box:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max, bots0):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max
        self.size = abs((x_max - x_min + 1) *
                        (y_max - y_min + 1) *
                        (z_max - z_min + 1))
        self.bots = bots0

    @property
    def min_dist(self):
        if self.size == 1:
            return self.x_min + self.y_min + self.z_min
        axes = []
        for i, j in [(self.x_min, self.x_max), (self.y_min, self.y_max),
                     (self.z_min, self.z_max)]:
            if i < 0 and j < 0:
                axes.append(abs(j))
            elif i > 0 and j > 0:
                axes.append(i)
            else:
                axes.append(0)
        return sum(axes)

    def __repr__(self):
        return f'({self.x_min},{self.x_max},{self.y_min},{self.y_max},{self.z_min},{self.z_max})'


    @property
    def sphere_overlap(self):
        d = 0
        for sphere in self.bots:
            closest_x = max(self.x_min, min(sphere.x, self.x_max))
            closest_y = max(self.y_min, min(sphere.y, self.y_max))
            closest_z = max(self.z_min, min(sphere.z, self.z_max))
            
            m = Manhattan((closest_x, closest_y, closest_z),
                          (sphere.x, sphere.y, sphere.z))
            
            if m.distance <= sphere.r:
                d += 1
        return d

    def __lt__(self, other):
        return (self.sphere_overlap, -self.min_dist) > (
            other.sphere_overlap, -other.min_dist)


def boxes_generate(x_min, y_min, z_min, x_max, y_max, z_max, b):
    boxes = []
    x1 = (x_max - x_min) // 2
    x = ((x_min, x1 + x_min), (x_min + x1 + 1, x_max))
    y1 = (y_max - y_min) // 2
    y = ((y_min, y1 + y_min), (y_min + y1 + 1, y_max))
    z1 = (z_max - z_min) // 2
    z = ((z_min, z1 + z_min), (z_min + z1 + 1, z_max))
    for l in list(product(x, y, z)):
        boxes.append(Box(l[0][0], l[0][1], l[1][0], l[1][1], l[2][0], l[2][1], b))
    return boxes


def main(inp):
    bots = list(map(lambda x: ((int(x[0]), int(x[1]), int(x[2])), int(x[3])),
                    [re.findall('-?\d+', i) for i in inp.splitlines()]))
    strong = max(bots, key=lambda x: x[1])
    p1 = (sum(1 for i in bots if
               abs(i[0][0] - strong[0][0]) +
               abs(i[0][1] - strong[0][1]) +
               abs(i[0][2] - strong[0][2]) <= strong[1]))


    bots3 = [Sphere(x[0][0], x[0][1], x[0][2], x[1]) for x in bots]

    x_min = min(bots3, key=lambda x: x.ranges()[0][0]).ranges()[0][0]
    y_min = min(bots3, key=lambda x: x.ranges()[0][1]).ranges()[0][1]
    z_min = min(bots3, key=lambda x: x.ranges()[0][2]).ranges()[0][2]
    x_max = max(bots3, key=lambda x: x.ranges()[1][0]).ranges()[1][0]
    y_max = max(bots3, key=lambda x: x.ranges()[1][1]).ranges()[1][1]
    z_max = max(bots3, key=lambda x: x.ranges()[1][2]).ranges()[1][2]

    boxes = boxes_generate(x_min, y_min, z_min, x_max, y_max, z_max, bots3)
    priority_queue = []
    for b in boxes:
        heapq.heappush(priority_queue, b)

    while priority_queue:
        q = heapq.heappop(priority_queue)
        if q.size == 1:
            return p1, q.min_dist

        boxes = boxes_generate(q.x_min, q.y_min, q.z_min, q.x_max, q.y_max, q.z_max, bots3)
        for b in boxes:
            heapq.heappush(priority_queue, b)


