#access specifier
#public-access from all
#protected -not access public &access inherited class
#private - only access that one class
#underscore meaning
#name angling -used for one variable is not overriding by other
class Demo():
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
d=Demo()
print(d.a)
print(d._b)
#print(d.__c)
print(d._Demo__c)
dc=dir(d) #used this for crt variables naming
print(dc)
#we use for access specifier but not it is correct
