# 装饰器
# 装饰器本身是一个函数
# 它传入函数作为参数
# 返回值也是函数
import time


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
