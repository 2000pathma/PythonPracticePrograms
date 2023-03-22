#####read the file contents 
##f=open("E:\MARKS.txt","r+")
##str=f.read()
###str=f.read(12) size is given then the size occupy the character is only print 
##print(str)
##f.close()


#convert file information into the list
f=open("E:\MARKS.txt","r+")
student=[]
for line in f.readlines():
    value=line.split()
    student.append([value[0],value[1],value[2]])
print(student)
f.close()

#Read the line from the file
##f=open("E:\MARKS.txt","r+")
##for line in f.readlines():
##    print("priya")
##    print(line)
##f.close()

##searching a keyword from the file
##f=open("E:\MARKS.txt","r+")
##inp=input("Enter the keyword")
##count=0
##for line in f.readlines():
##    count+=1
##    if inp in line:
##        print("keyword found in the number",count)
##f.close()
##
##f=open("E:\MARKS.txt","r+")
##f.write("\n Student Mark Details")
##str=f.read()
##print(str)
##f.close()
