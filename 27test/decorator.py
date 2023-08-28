# 装饰器
# 在使用装饰器之前，有以下条件
# 1.存在闭包
# 2.存在需要被装饰的函数

# 函数的地址值

def test():
    pass


print(test)

# 直接打印函数会打印function test at 后面加一个地址值
# 每个函数名字都存放着一个它的地址值

# 闭包就是在函数内部又定义了一个函数
# 闭包的条件
# 1.存在函数的嵌套关系
# 2.内层函数引用了外层函数的变量
# 3.外层函数返回内层函数的地址值
# 函数名存着地址值


def Hello(num):
    def in_Hello():
        print(num)

    return in_Hello


result = Hello(10)
result()

# 装饰器：不修改的原来的代码而能够动态的为一个类添加一些额外的功能
# 装饰器会将被装饰的函数作为参数传递给装饰器同名的函数


def welcome(func):
    def in_func():
        print("welcome to hongkk")
        # 这里调用被装饰的函数
        func()
    return in_func


@welcome
# 装饰器会自动将被装饰的函数传递给装饰器函数
def login():
    print("登录成功")
