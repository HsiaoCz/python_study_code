# 个数可变的位置参数
# 类似于go的...


def hello(*a):
    print(a)

hello(10, 20, 30)
# 位置参数，就是直接传值
# 输出的结果为元组

# 个数可变的关键字参数
# 结果为字典


def Hello(**args):
    print(args)

Hello(a=10, b=20, c=40, d=50)

# 个数可变的位置参数和个数可变的关键字参数都只能定义一个
# 而且可变位参只能在可变关键字参数之前
# 函数返回多个返回值的时候，结果为元组
