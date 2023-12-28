import multiprocessing
import time


def shopping():
    for i in range(5):
        print("-----正在购物------")
        time.sleep(1)


def game():
    for i in range(5):
        print("------正在打游戏--------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=shopping)
    p2 = multiprocessing.Process(target=game)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
