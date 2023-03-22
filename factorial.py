# Python 3 program to ﬁnd # factorial of given number 
def factorial(n): 
# single line to ﬁnd factorial
#return 1 -->false
    return 1 if (n==1 or n==0) else n * factorial(n - 1) #5*factorial(5-1)
# Driver Code
num = int(input("Enter the number:"))
print ("Factorial of",num,"is", factorial(num)) 
