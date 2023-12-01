# python生成器
# Python中的生成器是一种特殊类型的函数，
# 它可以在需要时生成值，而不必一次性生成所有值并将它们存储在内存中。
# 生成器能够延迟产生序列的元素，这样可以减少内存占用并提高效率，特别是在处理大量数据时

# 生成器本身是一个特殊的迭代器
# 当python发现 yield 会将函数打个标签
# 标示为生成器函数
# 调用一个生成器函数，会返回一个生成器对象
# 只有对生成器对象调用next()时，才会开始执行

def gen(num):
    while num > 0:
        yield num
        num -= 1
        return


g = gen(5)

first = next(g)

for i in g:
    print(i)
