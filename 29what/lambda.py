# lambda表达式的使用
lambda a: a*2

# 意思是 接收参数a 返回值=a*2


def func(a):
    return a*2


b = (lambda a: a*2)(3)

res = (lambda a, b, c: a*b*c)(2, 3, 5)

print(res)
