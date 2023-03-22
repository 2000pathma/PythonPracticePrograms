#hierarchical inheritance --one base class and multiple child class
class get:#base class
    def getin(self):
        self.a=int(input("Enter value A:"))
        self.b=int(input("Enter value B:"))
class addition(get):#child class
    def add(self):
        self.getin()
        c=self.a+self.b
        print("Addition:",c)
class subtraction(get):#child class
    def sub(self):
        self.getin()
        c=self.a-self.b
        print("subtraction:",c)

obj1=addition()
obj1.add()

obj2=subtraction()
obj2.sub()
