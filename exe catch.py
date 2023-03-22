import sys     #import this package for error catching
a=[2,4,6,'a',8]
for i in a:
    try:
        c=2/i#2/4=1
        print(c)
    except:
        print("oops",sys.exc_info()[0],"occured")
#type error is occured
#name and type error is predefined exceptions
        
