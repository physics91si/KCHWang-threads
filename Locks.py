import random
import time
import threading

class Num():
    def __init__(self,counter=0):
        self.counter = counter
    def increment(self):
        temp = self.counter
        time.sleep(random.uniform(1,2)) #Just a fancy random amount of sleep for the thread calling this
        temp += 1
        self.counter = temp
        
def worker(num):
    with lock:
        num.increment()
    return

threads = []
num = Num()
lock = threading.Lock()

for i in range(15):
    t = threading.Thread(target=worker, args=(num,))
    threads.append(t)
    myName = "Thread " + str(i)
    t.setName(myName)
    t.start()

for t in threads:
    t.join()
    print(t.getName(), "joined")
print(num.counter)
