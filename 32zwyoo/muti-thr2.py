# 多线程共享全局变量
import threading
import time

num = 100


def num_1():
    global num
    num += 1
    print("----threading_num:%d---" % num)


def num_2():
    print("----threading_num2:%d---" % num)


def main():
    t1 = threading.Thread(target=num_1)
    t2 = threading.Thread(target=num_2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("-----threading_main:%d--" % num)


if __name__ == "__main__":
    main()
