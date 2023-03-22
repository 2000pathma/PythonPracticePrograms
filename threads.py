#thread
##def a():
##    count=0
##    while count<5:
##        count+=1
##        print("function a")
##def b():
##    count=0
##    while count<5:
##        count+=1
##        print("function b")
##a()
##b()
#overcome this problem we can use threads
#1.kernel level thread-interact with operating system-start thread by os automatically
#2.user level thread-start by user
#thread- used for more function is run at a time in a program
#thread is implement in python by some packages(import in python)
#types of package 
#1._thread(name thread in python 2.7)
#2.threading
import _thread
import time #sometimes thread is sleep(waiting one sleep for other thread running)
def a(msg): #msg-arguments
    count=0
    while count<5:
        count+=1
        time.sleep(3)
        print(msg)
def b(msg):
    count=0
    while count<5:
        count+=1
        time.sleep(5)#time is used for print the output in time cap
        print(msg)
try: #used for sometime thread is not start(error)
    _thread.start_new_thread(a,("Thread1",)) #start the thread
    _thread.start_new_thread(b,("Thread2",))
except:
    print("error to start thread")
    
while 1: #used for start the program
    pass 

    
