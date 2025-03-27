from collections import defaultdict


def gens(state,rules,n):
    s=[]
    for c in range(n):
      
        if c>3 and n==50000000000:
            if s[-1]-s[-2]==(z:=s[-3]-s[-4]):
                x=s[-1]+z*(50000000000-c-1)
                return x

        
        current=state.copy()
        for i in range(min(state.keys())-2,max(state.keys())+4):

            z=''.join([current[j] for j in range(i-2,i+3)])

            state[i]=rules[z]

        state=sorted(state.items())
        if n==50000000000:
            s.append(sum(map(lambda x:x[0] if x[1]=='#'else 0,state)))
        state=defaultdict(lambda :'.',state)
    return sum(map(lambda x:x if state[x]=='#' else 0,state))

def main(inp):
    state,rules=inp.split('\n\n')
    state=state.split(':')[1].strip()
    rules={i.split(' => ')[0]:i.split(' => ')[1].strip() for i in rules.splitlines()}
    state={i:j for i,j in enumerate(state)}
    state=defaultdict(lambda :'.',state)
    
    return gens(state,rules,20),gens(state,rules,50000000000)
                    