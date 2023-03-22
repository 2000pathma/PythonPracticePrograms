row=5
value=97
while row>=1:
    column=5
    while column>=row:
        print(chr(value),end='')
        value+=1
        column-=1
    print()
    row-=1
