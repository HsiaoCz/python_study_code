# 获取进程号
import multiprocessing
import os
import time


def test():
    while True:
        print(f"---in 子进程 pid={os.getpid()}")
        time.sleep(1)


def main():
    print(f"----in 主进程 pid={os.getpid()}----")
    p = multiprocessing.Process(target=test)
    p.start()


# 主进程的创建了子进程，
# 所以在进程的ppid就是父进程，那么主进程的ppid就是python解释器的pid


def test1():
    while True:
        print(f"---in 子进程 pid={os.getpid()},父进程{os.getppid()}---")
        time.sleep(1)


def main1():
    print(f"----in 主进程 pid={os.getpid()} ,父进程 pid={os.getppid()}----")
    p2 = multiprocessing.Process(target=test1)
    p2.start()


if __name__ == "__main__":
    main()
    main1()
