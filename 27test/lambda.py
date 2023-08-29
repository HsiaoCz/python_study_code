# lambda 表达式的使用
lambda a: a*2

# 这个表达式等价于


def func(a):
    return a*2


# 接收lambda表达式的返回值，可以这样写
b = (lambda a: a*2)(1)
print(b)

# 多个参数的lambda表达式
res = (lambda a, b, c: a*b*c)(1, 2, 3)
print(res)
