# 在python中一切都是对象
# 在python定义一个函数
# 只是定义了一个变量，变量保存了这个function object
# 函数是callable ，可以被调用
# 本质上一切对象都可以调用
# 只不过不是callable的对象，调用在运行时会出错

import time


def get_multiple_func(n):

    def multiple(x):
        return n*x

    return multiple


double = get_multiple_func(10)
triple = get_multiple_func(12)

print(double(2))
print(triple(2))

# 装饰器本身是一个函数


def dec(f):
    pass


@dec
def dell(x):
    return x*2

# 绝大多数时候，使用decorator
# 参数是函数，返回值也是函数


def timeit(f):

    def wrapper(x):
        start = time.time()
        ret = f(x)
        print(time.time-start)
        return ret

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)


my_func(1)

# 带参数的decrator


def timeji(iteration):

    def inner(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time()-start)
            return ret
        return wrapper

    return inner


@timeji(1000)
def hello(x):
    return x*2


hello(2)
