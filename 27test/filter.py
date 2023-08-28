# 过滤函数
def func(x):
    return x > 5


l = [1, 23, 12, 4, 5, 6]
f = filter(func, l)
print(list(f))
