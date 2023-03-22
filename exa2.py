#######read the file contents 
##f=open("E:\MARKS.txt","r+")
###str=f.read()
##str=f.read(50) #size is given then the size occupy the character is only print 
##print(str)
##f.close()


##convert file information into the list
##f=open("E:\MARKS.txt","r+")
##student=[] #create a empty list
##for line in f.readlines():  
##    value=line.split() #separate student,mark ,details
##    student.append([value[0],value[1],value[2]])
##print(student)
##print(type(student))
##f.close()


#Read the line from the file
##f=open("E:\MARKS.txt","r+")
##for line in f.readlines():
##    print("COLLEGE MARK")
##    print(line)
##f.close()


##searching a keyword from the file
##f=open("E:\MARKS.txt","r+")
##inp=input("Enter the keyword") #Student
##count=0
##for line in f.readlines():
##    count+=1 #count=count+1
##    if inp in line:  
##        print("keyword found in the number",count)
##f.close()

f=open("E:\MARKS.txt","r+")
f.write("\n PRIYA IT 89 ")
str=f.read()
print(str)
f.close()

