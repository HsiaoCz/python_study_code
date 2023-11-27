# 过滤函数
def func(x):
    return x > 5


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6]
    f = filter(func, l)
    print(list(f))
