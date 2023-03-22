#user defined exception
class Error(Exception):
    pass
class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass
num=10
while True:
    try:
        ch=int(input("Enter the number"))
        if ch<10:
            raise TooSmallError
        elif ch>10:
            raise TooLargeError
        break
    except TooSmallError:
        print("you entered too small number,please try again")
    except TooLargeError:
        print("you entered too large number,please try again")
print("you entered correcr number")
