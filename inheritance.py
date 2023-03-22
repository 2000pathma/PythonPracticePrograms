#inheritance-used for derived attributes from base class to child class
#1.single inheritance-1 base & 1 child class
##class father():#base class 
##    fname="raja"
##    fage=40
##class son(father):#child class
##    sname="kumar"
##    sage=20
##obj=son()
##print("father name is",obj.fname)
##print("son name is",obj.sname)
#2.multi level inheritance
##class gfather():#base class 
##    gfname="ragavan"
##    gfage=100
##class father(gfather):#base class 
##    fname="raja"
##    fage=40
##class son(father):#child class
##    sname="kumar"
##    sage=20
##obj=son()
##print("grandfather name is",obj.gfname)
##print("father name is",obj.fname)
##print("son name is",obj.sname)
#3.multiple inheritance
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


