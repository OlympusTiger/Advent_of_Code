import heapq
from itertools import compress
from copy import deepcopy


hp1=50
mana=500
hp2=55
dmg2=8
class State:
	def __init__(self,spent,hp1,mana,arm,shield,poison,recharge,hp2):
		self.spent=spent
		self.hp1=hp1	
		self.mana=mana
		self.arm=arm
		self.shield=shield
		self.poison=poison
		self.recharge=recharge
		self.hp2=hp2
		
	def effects(self):
		if self.shield:
			self.arm=9
			self.shield-=1
		else:
			self.arm=0
		if self.poison:
			self.hp2-=3
			self.poison-=1
		if self.recharge:
			self.mana+=101
			self.recharge-=1
			
	def __lt__(self,other):
		return self.spent<other.spent

def available_spells(state):
	spells=['MM','Drain','Shield','Poison','Recharge']
	c=list(compress(spells,[1,1,not state.shield,not state.poison,not state.recharge]))
	
	for s in c:
		
		new=deepcopy(state)#alter existing state to pass to new
		
		if s=='MM' and new.mana>=53:
			new.spent+=53
			new.mana-=53
			new.hp2-=4
			
		elif s=='Drain'and new.mana>=73:
			new.spent+=73
			new.mana-=73
			new.hp1+=2
			new.hp2-=2
			
		elif s=='Shield'and new.mana>=113:
			new.spent+=113
			new.mana-=113
			new.shield=6
			
		elif s=='Poison'and new.mana>=173:		
			new.spent+=173
			new.mana-=173
			new.poison=6
			
		elif s=='Recharge'and new.mana>=229:
			new.spent+=229
			new.mana-=229
			new.recharge=5
			
		yield new
		
		
def fight(Part2):

#State(Spent,Hp1,Mana,armor,Shield,Poison,Recharge,Hp2)
	queue=[]	
	initial=State(0,hp1,mana,0,0,0,0,hp2)

	for n in available_spells(initial):#My turn 1
		if Part2:
			n.hp1-=1  
		heapq.heappush(queue,n)
		
	explored=set()
	
	while queue:
		print(len(queue))
		
		state=heapq.heappop(queue)	
		if state in explored:
			continue
		explored.add(state) 
		 

#__________________________________
						 #Boss Turn
		state.effects()  
	
		if state.hp2<=0:		
			return state.spent
			
		if dmg2-state.arm>=1:
			state.hp1-=dmg2-state.arm
		else:
			state.hp1-=1
			
		if state.hp1<=0:
			continue
#_______________________________
				  	   #My Turn 
		if Part2:
			state.hp1-=1 #turn start dmg
		if state.hp1<=0:
			continue	
			
		state.effects()
		
		if state.hp2<=0:		
			return state.spent
			
		if state.mana<53:#no spell available?...
			continue
		
		for n in available_spells(state):#next spell
			
			heapq.heappush(queue,n)


def main(inp):


    return fight(False),fight(True)