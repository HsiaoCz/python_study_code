# 生成器
# 这是一个生成器函数
# 当一个函数有一个yield标识的时候
# python会给它打个标签，认为它是一个生成器函数
def gen(num):
    while num > 0:
        yield num
        num -= 1
    return


# 调用一个生成器函数，会返回一个生成器对象
# 保存到g这个变量
# 生成器对象
g = gen(5)

first = next(g)
# 当执行next这个函数的时候，才开始真正执行函数体
for i in g:
    print(i)

