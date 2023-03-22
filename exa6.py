def add_sub():#function 
    first=float(input("enter first number"))
    second=float(input("enter second number"))
    add=first+second
    sub=first-second
    return [add,sub]
results=[]
for i in range(5):#0 to 4
    results.append(add_sub())

print(results)
    
                 
