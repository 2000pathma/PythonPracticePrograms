##class Demo():
##    print("constructor")
##    def __init__(self):
##        self.name="vijay"
##        self.age=23
##    def display(self):
##        print("name is :",self.name)
##        print("age is :",self.age)
##
##obj=Demo()
##obj.display()


class Demo():
    print("constructor")
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def display(self):
        print("name is :",self.name)
        print("age is :",self.age)

obj=Demo("vijay",20)
obj.display() 

#constructor is used to pass an arguements to the class at the time of object creations 
