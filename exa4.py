#inheritance-used for derived attributes from base class to child class
#1.single inheritance-1 base & 1 child class
##class father():#base class 
##    fname="subramaniyan"
##    fage=47
##class son(son):#child class
##    sname="ramesh"
##    sage=21
##obj=father()
##print("father name is",obj.fname)
##print("son name is",obj.sname)


#2.multi level inheritance
##class gfather():#base class 
##    gfname="muthu"
##    gfage=80
##class father():#base class 
##    fname="raja"
##    fage=40
##class son(father,gfather):#child class
##    sname="kumar"
##    sage=20
##obj=son()
##print("grandfather name is",obj.gfname)
##print("father name is",obj.fname)
##print("son name is",obj.sname)

class father():#base class 
    fname="ragavan"
    fage=40
class mother():#base class 
    mname="ramu"
    mage=30
class son(father,mother):#child class
    sname="kumar"
    sage=20
obj=son()
print("father name is",obj.fname)
print("mother name is",obj.mname)
print("son name is",obj.sname)

