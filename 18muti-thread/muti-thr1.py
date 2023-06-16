# 上面的程序需要先执行shopping，再执行game
# 如果希望程序能够同时执行这两个函数

import time
import threading


def game():
    """玩游戏 5秒钟
    """
    for i in range(5):
        print("---正在玩游戏---")
        time.sleep(1)


def shopping():
    """逛街 5 秒钟
    """
    for i in range(5):
        print("---正在逛街----")
        time.sleep(1)

# target=shopping是告诉这个线程等下去执行这个函数，
# 此时只是创建一个Thread对象，
# 并没有开始创建线程，直到我们调用start方法，该线程才会被创建
def main():
    t1 = threading.Thread(target=shopping)
    t2 = threading.Thread(target=game)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
