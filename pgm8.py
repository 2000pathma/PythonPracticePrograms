row=1
while row<=5:
    value=90
    column=1
    while column<=row:
        print(chr(value),end='')
        column+=1
        value-=1
    row+=1
    print()

  
