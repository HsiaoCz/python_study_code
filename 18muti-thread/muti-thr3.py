# 有并发，那么必然存在着数据的竞态问题
# 解决竞态，自然需要加锁
import threading
import time

g_num = 0


def num_1(num):
    global g_num
    # 谁先执行到这里，谁就先上锁，另一方就只能等着这个锁解开
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()  # 释放锁
    print("---threading_num1:%d" % g_num)


def num_2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()  # 解锁
    print("---threading_num2 :%d ---" % g_num)


def main():
    t1 = threading.Thread(target=num_1, args=(1000000,))
    t2 = threading.Thread(target=num_2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(1.5)
    print("---threading_main :%d ---" % g_num)


# 创建互斥锁对象
mutex = threading.Lock

if __name__ == "__main__":
    main()
