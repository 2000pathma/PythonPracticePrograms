#assertion is one of the exception handling method
def age(value):
    assert value<0,'enter correct age'
    print(value)
inp=input("Enter the age")
age(inp)
