def calc(a, b):
    c = a+b
    return c


print(calc(a=12, b=13))
# 使用关键字参数，可以不按照顺序来写调用

# 定义默认值参数


def fun(a, b=10):
    print(a, b)


fun(10, 12)
fun(12)

# 个数可变的位置参数，为元组


def func(*a):
    for i in a:
        l = []
        l[i] = a[i]
    return l


func("hello", "hi", "jsjs")

# **关键字参数
# 函数有多个返回值的时候，结果为元组
# 函数有一个返回值，返回类型
# 多个返回值的时候，返回元组
# 函数传入的参数是不可变类型，在函数内改变参数的值，对函数外的参数没有影响
# 传入可变参，在函数内修改参数的值，函数外的参数也会被改变
