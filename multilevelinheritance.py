#multilevel inheritance -one parent class and one or more child class
class gfather():#parent
    gfname="muthu"
class father(gfather):#parent
    fname="ramesh"
class son(father):#child
    sname="kanna"
obj=son()
print("sname",obj.sname)
print("fname",obj.fname)
print("gfname",obj.gfname)
