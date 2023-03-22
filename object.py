class Demo:
    print("class method:")
#print class attributes directly without creating a object
    d=int(input("Enter d:"))
    def example(self,a,b):#self is used for access both local and global variables self is used for access the data members
        c=a+b+self.d 
        return c
obj=Demo()
ans=obj.example(10,20)
print("answer is:",ans)
