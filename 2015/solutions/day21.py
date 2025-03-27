from itertools import product,permutations


def add_tuples(a,b):
	return tuple(map(lambda x,y:x+y,a,b))

def items(armor,rings):
	a_combs=[(0,0,0)]
	r_combs=[(0,0,0)]
	for a in armor:
		a_combs.append(tuple(armor[a].values()))
	for r in rings:
		r_combs.append(tuple(rings[r].values()))	
	for r1,r2 in permutations(rings,2):
		t=add_tuples(tuple(rings[r1].values()),tuple(rings[r2].values()))
		r_combs.append(t)
		
	combs=[]
	for a,b in product(a_combs,r_combs):
		combs.append(add_tuples(a,b))
		
	return sorted(combs,key=lambda x:x[0])

def fight(weapons,combs,Part2):
    Hp2,Ad2,Def2=104,8,1
    costs=[]
    for w,c in product(weapons.values(),combs):
     
     
        total=add_tuples(tuple(w.values()),c)	
        cost,Ad1,Def1=total
       
	
        Hp1=100
        Hp2,Ad2,Def2=104,8,1
        if Ad1>Def2:	
            Dmg1=Ad1-Def2
        else:
            Dmg1=1
        if Ad2>Def1:	
            Dmg2=Ad2-Def1
        else:
            Dmg2=1

        while Hp1>0 and not Part2:
            Hp2-=Dmg1
          
            if Hp2<=0:
                costs.append(cost)
                break
            Hp1-=Dmg2


        if Part2:     
            while Hp1>0:
                Hp2-=Dmg1
                if Hp2<=0:
                    break
                Hp1-=Dmg2
            else:
                costs.append(cost)
    return costs

def main(inp):
    
    weap,arm,rin=inp.split('\n\n')
    
    attributes=weap.splitlines()[0].split()[1:]
  
    weapons={}
    armor={}
    rings={}

    for w in weap.splitlines()[1:]:
     
        temp=w.split()

        weapons[temp[0]]=dict(zip(attributes,map(int,temp[1:])))
    for a in arm.splitlines()[1:]:
        temp=a.split()
        armor[temp[0]]=dict(zip(attributes,map(int,temp[1:])))
    for r in rin.splitlines()[1:]:
        temp=r.split('   ')
        temp.remove('')
        rings[temp[0]]=dict(zip(attributes,map(int,temp[1:])))
    
    combs=items(armor,rings)
 
    
    
    return min(fight(weapons,combs,False)),max(fight(weapons,combs,True))