# lambda表达式的使用
lambda a: a*2

# 类似于


def func(a):
    return a*2


# 使用lambda表示的返回值，可以这样写
b = (lambda a: a*2)(12)

print(b)

# 多参数的lambda表达式
res = (lambda a, b, c: a*b*c)(1, 2, 3)

print(res)
