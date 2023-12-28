# python生成器


def gen_func():
    yield 1


def func():
    return 1


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n = n + 1

