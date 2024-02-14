# 函数定义与调用
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

# 函数参数
# 定义处 形式参数
# 调用处 实际参数
# 使用关键字参数 可以不按照顺序来写调用
m = calc(a=12, b=13)
print(m)
# 不使用关键字实参，需要按照顺序传入参数
