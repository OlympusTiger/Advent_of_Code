


def main(inp):

    target=int(inp)
    target2=inp
 


    elf1=0
    elf2=1
    recipes='37'
    a=int(recipes[elf1])
    b=int(recipes[elf2])
    
 
    res1=0
    res2=0
    while True:
        l=len(recipes)
        if l>=target+10:
            res1=recipes[target:target+10]
            if res2:
                break
        if l%100000==0 and target2 in recipes:
            x=recipes.index(target2)
            res2=x
            if res1 :
                break
        s=str(a+b)
  
        for i in s:
            recipes+=i
        
        elf1=(elf1+1+a)%len(recipes)
        elf2=(elf2+1+b)%len(recipes)
        a=int(recipes[elf1])
        b=int(recipes[elf2])
        
    


       
    return res1,res2
                    