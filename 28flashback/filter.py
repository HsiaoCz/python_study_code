# 过滤函数
def func(x):
    return x > 5


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    f = filter(func, 1)
    print(list(f))
