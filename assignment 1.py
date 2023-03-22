total = 0
while True:
    inp = input("Enter transation:")
    transaction=inp.split(" ")
    inp_type=transaction[0]
    amount=int(transaction[1])
    if inp_type=="D" or inp_type=="d":
        total+=amount
    elif inp_type=="W" or inp_type=="w":
        total-=amount
    else:
        pass
    inp=input("want to continue(Y for yes):")
    if not (inp[0]=="Y" or inp[0]=="y"):
        break
print("net amount :",total)
