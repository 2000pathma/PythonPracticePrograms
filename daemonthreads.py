#Daemon thread-used for run continuously at the end of program
import threading
import time
def worker_a():
    print("thread 1 started")
    time.sleep(10)
    print("thread 1 finished")
def worker_b():
    print("thread 2 started")
    print("thread 2 finished")
t1=threading.Thread(target=worker_a,daemon='true')
t2=threading.Thread(target=worker_b)
t1.start()
t2.start()
t1.join()
t2.join()
    
#used in continuous process by using threads
