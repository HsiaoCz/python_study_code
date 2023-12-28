# python的函数定义与调用
# 函数的创建和调用


def hello(a, b):
    print(a + b)


hello(12, 13)

# 有返回值的函数


def calc(a, b):
    c = a + b
    return c


result = calc(12, 13)
print(result)
# 使用关键字参数 可以不按照顺序来写调用
m = calc(a=12, b=13)
print(m)
# 不使用关键字实参，需要按照顺序传入参数

# 传入的参数是不可变类型时，在函数体内改变参数的值，对函数外的参数没有影响
# 传入可变参数，在函数内修改参数的值，对函数外的参数也会改变


# 个数可变的位置参数
# 个数可变的关键字参数
def func(*a):
    print(a)


func(10, 20, 30)

# 函数定义的时候，关键字参数
# 结果为字典


def hell(**args):
    print(args)


hell(a=10, b=20, c=30)
# 个数可变的位置参数只能定义一个
# 可变的关键字参数只能定义一个

# 在一个函数的定义中，既有关键字参数，又有个数可变的位置形参
# 要求个数可变的位置形参放在个数可变的关键字形参之前
# 可变位参只能在可变关键字参数之前

# 函数有多个返回值的时候,结果为元组
