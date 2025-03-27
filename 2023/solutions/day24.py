from sympy import symbols,solve,Eq
from sympy.geometry import Point, Line
import re
from itertools import combinations


class Hails:
    def __init__(self,raw):
        raw=list(map(int,re.findall('-?\d+',raw)))
        self.start_x=raw[0]
        self.start_y=raw[1]
        self.start_z=raw[2]
        self.vel_x=raw[3]
        self.vel_y=raw[4]
        self.vel_z=raw[5]
        self.slope2D = self.vel_y/self.vel_x

    def __str__(self):
        return f'{self.start_x}, {self.start_y}, {self.start_z}, @, {self.vel_x}, {self.vel_y}, {self.vel_z}'
    
    def equation2D(self):
        return Line(Point(self.start_x,self.start_y),Point(self.start_x+self.vel_x,self.start_y+self.vel_y))
    
    def time_eq(self,t):
        return TimeEquations(self,t)

class TimeEquations(Hails):
    def __init__(self,hail,t):
        self.hail=hail
        self.t=t
    def time_x(self):
        return self.hail.vel_x*self.t+self.hail.start_x
    def time_y(self):
        return self.hail.vel_y*self.t+self.hail.start_y
    def time_z(self):
        return self.hail.vel_z*self.t+self.hail.start_z
    

def main(inp):
    hails = [Hails(i) for i in inp.splitlines()]

    low=200000000000000
    high=400000000000000

    x,y,t,t1,t2=symbols('x y t t1 t2')
    c=0
    for a,b in combinations(hails,2):
        if a.slope2D==b.slope2D:
            print((a.start_x,a.start_y),(b.start_x,b.start_y))
            continue
        # ss=solve([x-a.time_eq(t1).time_x(),x-b.time_eq(t2).time_x(),y-a.time_eq(t1).time_y(),y-b.time_eq(t2).time_y()],[x,y,t1,t2],dict=True)
        # if not ss:
        #     continue
        # ss=ss[0]
    
        # if ss[t1]>=0 and ss[t2]>=0 and low<=ss[x]<=high and low<=ss[y]<=high:
        #     c+=1
        inter = a.equation2D().intersection(b.equation2D())[0]

        if low<=inter.x<=high and low<=inter.y<=high:
            if (inter.x-a.start_x)*a.vel_x>0 and (inter.y-a.start_y)*a.vel_y>0 and (inter.x-b.start_x)*b.vel_x>0 and (inter.y-b.start_y)*b.vel_y>0:
                c+=1

    ax,ay,az,bx,by,bz,t1,t2,t3=symbols('ax ay az bx by bz t1 t2 t3')
    h1=hails[0]
    h2=hails[1]
    h3=hails[2]

    eq1=Eq(ax*t1+bx,h1.time_eq(t1).time_x())
    eq2=Eq(ay*t1+by,h1.time_eq(t1).time_y())
    eq3=Eq(az*t1+bz,h1.time_eq(t1).time_z())
    eq4=Eq(ax*t2+bx,h2.time_eq(t2).time_x())
    eq5=Eq(ay*t2+by,h2.time_eq(t2).time_y())
    eq6=Eq(az*t2+bz,h2.time_eq(t2).time_z())
    eq7=Eq(ax*t3+bx,h3.time_eq(t3).time_x())
    eq8=Eq(ay*t3+by,h3.time_eq(t3).time_y())
    eq9=Eq(az*t3+bz,h3.time_eq(t3).time_z())
    ss=solve([eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9],[ax,ay,az,bx,by,bz,t1,t2,t3],dict=True)[0]

    return c,ss[bx]+ss[by]+ss[bz]
                    