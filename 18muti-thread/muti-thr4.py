# 前面那种锁，一个函数拿个临界资源必须要把循环执行完毕
# 这无疑是废时间的
# 那么我们可以使用这种
import threading
import time

g_num = 0


def num_1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()  # 解锁
    print("---threading_num1 :%d ---" % g_num)


def num_2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()  # 解锁
    print("---threading_num2 :%d ---" % g_num)


# 创建互斥锁对象
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=num_1, args=(1000000,))
    t2 = threading.Thread(target=num_2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(1.5)
    print("---threading_main :%d ---" % g_num)


if __name__ == '__main__':
    main()
