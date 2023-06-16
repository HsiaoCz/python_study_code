# 传递参数的多进程
import multiprocessing


def test(a, b, c):
    print("---in 子进程---")
    print(a)
    print(b)
    print(c)


def main():
    print("---in 主进程---")
    p = multiprocessing.Process(target=test, args=(1, 2, 3))
    p.start()


if __name__ == "__main__":
    main()
