row=5
while row>=1:
    column=5
    while column>=row:
        print(column,end='')
        column-=1#or column=column-1
    print()
    row=row-1#row-=1
