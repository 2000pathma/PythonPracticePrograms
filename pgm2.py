row=5
value=1
while row>=1:
    column=5
    while column>=row:
        print(value,end='')
        value+=1
        column-=1
    print()
    row-=1
