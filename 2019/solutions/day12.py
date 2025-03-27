import re
from itertools import combinations
from math import lcm

class Moon:
    def __init__(self,pos):
        self.start_x, self.start_y, self.start_z = pos
        self.x, self.y, self.z = pos
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def __repr__(self):
        return f"POSITIONS x:{self.x}, y:{self.y}, z:{self.z}  VELOCITIES vx:{self.vx}, vy:{self.vy}, vz:{self.vz}  "
    
    def gravity(self, other):
        if self.x < other.x:
            self.vx += 1
            other.vx -= 1
        elif self.x > other.x:
            self.vx -= 1
            other.vx += 1
        if self.y < other.y:
            self.vy += 1
            other.vy -= 1
        elif self.y > other.y:
            self.vy -= 1
            other.vy += 1
        if self.z < other.z:
            self.vz += 1
            other.vz -= 1
        elif self.z > other.z:
            self.vz -= 1
            other.vz += 1
        
    def velocity(self):
        self.x += self.vx 
        self.y += self.vy 
        self.z += self.vz

    def total_moon_energy(self):
        return self.kinetic_energy*self.potential_energy
    @property
    def potential_energy(moon):
        return abs(moon.x) + abs(moon.y) + abs(moon.z)
    @property   
    def kinetic_energy(moon):
        return abs(moon.vx) + abs(moon.vy) + abs(moon.vz)

    @property
    def state(self):
        return self.x, self.y, self.z, self.vx, self.vy, self.vz
    

def main(inp):
    raw = list(map(int,re.findall('-?\d+', inp)))
    moons = [Moon(raw[i:i+3]) for i in range(0,12,3)]

    states = {'x':[],'y':[],'z':[]}
    x=[]
    y=[]
    z=[]
    for m in moons:
        x.append((m.x,m.vx))
        y.append((m.y,m.vy))
        z.append((m.z,m.vz))
    states['x'].append(x)
    states['y'].append(y)
    states['z'].append(z)

    loops=[]
    total_energy = 0
    s=0
    while len(loops)<3:
        s+=1
        for a,b in combinations(moons,2):
            a.gravity(b)
        for m in moons:
            m.velocity()
        if s == 1000:
            for m in moons:
                total_energy += m.total_moon_energy()
        x = []
        y = []
        z = []
        for m in moons:
            x.append((m.x,m.vx))
            y.append((m.y,m.vy))
            z.append((m.z,m.vz))
        if x ==states['x'][0]:
            loops.append(s)
        if y ==states['y'][0]:
            loops.append(s)
        if z ==states['z'][0]:
            loops.append(s)
        states['x'].append(x)
        states['y'].append(y)
        states['z'].append(z)

    return total_energy,lcm(*loops)
                    