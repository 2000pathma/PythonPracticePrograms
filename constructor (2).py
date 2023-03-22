#at the time of object creation for the class constructor is defaultly run
#self keyword is used for access the constructor parameters & self is must for al
#constructor is used for pass the arguements for the class in obj creation
##class Demo():
##    print("welcome")
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def display(self):
##        print("name is ",self.name)
##        print("age is ", self.age)
##obj=Demo("priya",20)
##obj.display()

#constructor is also used without passing values
class Demo():
    print("welcome")
    def __init__(self):
        self.name="ramesh"
        self.age=21
    def display(self):
        print("name is ",self.name)
        print("age is ", self.age)
obj=Demo()
obj.display()

