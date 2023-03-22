def factorial(x):
    """This is a recursive function-call a function itself.
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num =int(input("Entet num:"))
print("The factorial of", num, "is", factorial(num))
