# gil global interpreter lock (cpython)
# python 中一个线程对应c语言中的一个线程
# gil使得同一时刻只有一个线程运行在一个cpu上执行字节码
# 无法将多个线程映射到多个cpu上
# gil 会根据执行的字节码行数和时间片释放gil
# gil 还会再遇到io操作的时候，会主动释放


import dis
import threading


def add(a):
    a = a+1
    return a


print(dis.dis(add))

total = 0


def addt():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=addt)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
