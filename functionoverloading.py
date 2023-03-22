#polymorphism
#function overloading-not access directly in python
##class Demo():
##    def fun(self):
##        print("hello")
##    def fun(self,a):
##        print(a)
##obj=Demo()
###obj.fun()
##obj.fun(23)
##obj.fun(10)
#function overloading perform only indirectly
class Demo():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            c=a+b+c
        elif a!=None and b!=None:
            c=a+b
        else:
            c=a
        print(c)
obj=Demo()
obj.sum(10,20,30)
obj.sum(10,20)
obj.sum(10)



