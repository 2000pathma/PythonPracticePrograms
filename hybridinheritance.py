#hybrid inheritance-combination if different types of inheritance
#hierarchical inheritance
class get:
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
#multiple inheritance
class Arithmetic(addition,subtraction):
    def arith(self):
        self.add()
        self.sub()
obj=Arithmetic()
obj.arith()
        
