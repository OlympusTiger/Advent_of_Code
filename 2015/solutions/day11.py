from string import ascii_lowercase as alphabet


def con1(password):

    return any(password[t]==password[t+1]-1== password[t+2]-2 for t in range(len(password)-2))

def con2(password):
    return all(i not in [8,11,14] for i in password)

def con3(password):
    for i in range(len(password)-1):
        if password[i]==password[i+1]:
            for j in range(i+2,len(password)-1):
                if password[j]==password[j+1]:
                    return True
            return False
    
def increment(password):
    reverse=password[::-1]
    for i,n in enumerate(reverse):
        if n in [8,11,14] and i!=7:
            print(i)
            reverse=reverse[:i]+[n+1]+[0]*(len(password)-1-i)
            break
    password=reverse[::-1]
    password[0]+=1        
    for i,n in enumerate(password):

        if n==26:
            password[i]=0
            if i<len(password)-1:
                password[i+1]+=1 
    return password

def main(inp):

    old=True
    password=[ord(i)%97 for i in inp][::-1]
    print(password)

    

    while not (con1(password[::-1]) and  con2(password[::-1]) and con3(password[::-1])) or old:
        old=False
        password=increment(password)
        print(password)
       

        



    return ''.join([alphabet[i] for i in password[::-1]]),None