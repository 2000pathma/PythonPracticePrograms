#multilevel inheritance -one or more parent class and one child class
class father():#parent
    fname="ramesh"
class mother():#parent
    mname="priya"
class son(father,mother):#child
    sname="kanna"
obj=son()
print("sname",obj.sname)
print("fname",obj.fname)
print("mname",obj.mname)
