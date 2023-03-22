#single inheritance -one parent class and one child class
class father():#parent
    fname="ramesh"
class son(father):#child
    sname="kanna"
obj=son()
print("sname",obj.sname)
print("fname",obj.fname)
