# 线程同步
# lock Rlock
# 锁会影响线程
# 锁会引起死锁
# 可重入锁
# RLock
# 在同一个线程里面，可以多次调用acquire()，需要注意acquire的次数要和release的次数相同

import threading
from threading import Lock

total = 0
lock = Lock


def addt():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = threading.Thread(target=addt)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
