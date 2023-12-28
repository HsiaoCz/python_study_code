# lambda表达式

lambda a: a*2
# 表达式的意思是 接收参数a返回值为a=a*2
# 它等价于


def func(a):
    return a*2


# lambda表达式还可以这样写
b = (lambda a: a+2)(1)
print(b)

# 多参数的lambda表达式
res = (lambda a, b, c: a*b*c)(1, 2, 3)
print(res)

# lambda可以作为一些内置函数的参数
# lambda函数可以在pandas中使用