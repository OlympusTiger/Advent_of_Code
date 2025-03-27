import re
from collections import deque
from itertools import cycle
def main(inp):
    players,marbles=map(int,re.findall('\d+',inp))
    scores=[0 for _ in range(players)]
    player=cycle(range(players))
    circle=deque([0])
    
    for i in range(1,100*marbles+1):
        p=next(player)
        if i%23==0:
            circle.rotate(7)
            scores[p]+=i+circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(i)

    return max(scores),None
                    