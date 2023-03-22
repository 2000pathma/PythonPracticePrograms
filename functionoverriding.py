#polymorphism
#function overriding - derived one class function into another class function (derived class function is accessed)
#suppose function is not in derived class then access the base class
class Demo():
    def fun(self):
        print("Demo class")
class Demo1(Demo):
    def fun(self):
        print("Demo 1 class")
obj=Demo1()
obj.fun()
