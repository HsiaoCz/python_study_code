# reduce函数
# reduce函数可以使各元素按顺序计算，每次计算结果也会参与到下次计算

import functools

a = [1, 2, 3, 4, 5, 6]

# 计算累乘


def mul(x1, x2):
    return x1*x2


print(functools.reduce(mul, a))
