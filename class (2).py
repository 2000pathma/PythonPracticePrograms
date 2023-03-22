##class Demo:
##    print("class method")
##    def example(self,a,b):
##        c=a+b
##        print(c)
##obj=Demo()
##obj.example(10,20)

#self is used for access the variable outside the function
##class Demo:
##    print("class method")
##    d=60
##    def example(self,a,b):
##        c=a+b+self.d #self is must placed
##        print(c)
##obj=Demo()
##obj.example(10,20)

#return is used for return the value to the answer
class Demo:
    print("class method")
    d=60
    def example(self,a,b):
        c=a+b+self.d #self is must placed
        return c
obj=Demo()
ans=obj.example(10,20)
print("answer",ans)



