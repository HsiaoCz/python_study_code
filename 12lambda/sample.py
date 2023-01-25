# lambda表达式的使用
lambda a: a*2
# 这个表达式的意思是 接收参数a 返回值=a*2
# 等价于


def func(a):
    return a*2


# 接收lambda表达式的返回值 可以这样写
b = (lambda a: a*2)(1)
print(b)
# 多参数的lambda表达式
res = (lambda a, b, c: a*b*c)(1, 2, 3)
print(res)

# lambda函数还可以作为一些内置函数的参数
# lambda函数还可以在pandas中使用
