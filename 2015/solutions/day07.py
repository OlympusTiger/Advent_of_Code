
def parse(signals,override=None):
    wires={}
    print(signals)
    while signals:
        

        s=signals.pop(0)
        if s[-1]=='b' and override:
            print(434343434)
            wires['b']=override
            continue
        if len(s)==2:
            try:
                wires[s[-1]]=int(s[0])
            except ValueError:
                if s[0] in wires:
                    wires[s[-1]]=wires[s[0]]
                else:
                    signals.append(s)

        elif len(s)==3:
            if s[1].isdigit():
                wires[s[-1]]=2**16+~int(s[1])
            elif s[1] in wires:
                wires[s[-1]]=2**16+~wires[s[1]]
            else:
                signals.append(s)

        else:
            a=s[0] if s[0].isdigit() else s[0]
            b=s[2] if s[2].isdigit() else s[2]
            if {i for i in [a,b] if i.isalpha()}.issubset(set(wires)):
                a=int(a) if a.isdigit() else wires[a]
                b=int(b) if b.isdigit() else wires[b]
                if s[1]=='AND':
                    wires[s[-1]]=a&b
                elif s[1]=='OR':
                    wires[s[-1]]=a|b
                elif s[1]=='LSHIFT':
                    wires[s[-1]]=a<<b
                elif s[1]=='RSHIFT':
                    wires[s[-1]]=a>>b
            else:
                signals.append(s)
    else:
        return wires['a']




def main(inp):
    signals=[s.split(' -> ') for s in inp.splitlines()]
    signals=list(map(lambda x:x[0].split(' ')+[x[1]],signals))
    
    
    p1=parse(signals.copy())
    print(p1)
    return p1,parse(signals,p1)