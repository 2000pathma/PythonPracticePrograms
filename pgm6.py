value=91
row=1
column=1
while row<=5:
    while column<=row:
        print(chr(value),end='')
        value+=1
        column+=1
    column=1
    row+=1
    print()
