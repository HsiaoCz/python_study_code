# python生成器
# 生成器函数，函数里面有yield关键字
# 只要调用生成器函数，返回的是生成器对象
# 生成器对象，python编译字节码的时候就产生了
# yield 可以一直写，这和return不同

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1
