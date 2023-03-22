name=input("enter name")
print()
length=len(name)
for row in range(len(name)):
     for space in range(length-1):
         print(' ',end='')
     for i in range(row+1):
         print(name[i],end='')
     print()
     length-=1
