from collections import Counter
def calc(particles):
    for i in range(len(particles)):
            part=particles[i]
            x=part['p'][0]+part['v'][0]+part['a'][0]
            part['p'][0]=x
            part['v'][0]=part['v'][0]+part['a'][0]
            y=part['p'][1]+part['v'][1]+part['a'][1]
            part['p'][1]=y
            part['v'][1]=part['v'][1]+part['a'][1]
            z=part['p'][2]+part['v'][2]+part['a'][2]
            part['p'][2]=z
            part['v'][2]=part['v'][2]+part['a'][2]
    return particles

def Dx(particles):

    for j in range(3000):
        particles=calc(particles)
        c=Counter(map(lambda x:tuple(x['p']),particles))
        co=len(particles)-list(c.values()).count(1)
        for _ in range(co):
            for a in c:
                if c[a]>1:
                
                    m=sorted([i for i in range(len(particles)) if tuple(particles[i]['p'])==a],reverse=True)
                    for k in m:
                        particles.pop(k)
    return len(particles)
                      
             


def main(inp):
    particles=[{j[0]:list(map(int,j[3:-1].split(','))) for j in i.split(', ')} for i in inp.splitlines()  ]
    
    m=min(particles,key=lambda x:(sum(map(abs,x['a'])),sorted(list(map(lambda y:x['a'][y]*x['v'][y],range(3)))),sum(map(abs,x['p']))))
    i=particles.index(m)
    Dx(particles)

    




    return i,Dx(particles)         