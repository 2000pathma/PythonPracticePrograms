name=input("enter name")
print()
length=len(name)
for row in range(len(name)):
     for space in range(row):
         print(' ',end='')
     for i in range(length):
         print(name[i],end='')
     print()
     length-=1
