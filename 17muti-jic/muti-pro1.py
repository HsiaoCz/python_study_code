# 与多线程共享全局变量不同，多进程之间不共享全局变量，
# 例如在全局创建了一个列表，在子进程中进行追加

import multiprocessing
import time

num = [1, 2, 3, 4]


def test():
    num.append(5)
    print(num)


def test1():
    print(num)


def main():
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=test1)
    p1.start()
    time.sleep(1)
    p2.start()
    time.sleep(1)
    print(num)


if __name__ == "__main__":
    main()
