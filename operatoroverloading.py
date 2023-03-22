#operator overloading-polymorphism
##c=10+20
##print(c)
##
##s=int.__add__(10,20)
#also used string,float
###also perform mul,div,sub
##print(s)
#perform this add into another operation is called operator overloading
class student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,temp):
        m1=self.m1+temp.m1
        m2=self.m2+temp.m2
        s3=student(m1,m2)
        return s3


s1=student(30,40)
s2=student(50,20)
s3=s2+s1
print(s3.m1)
print(s3.m2)

