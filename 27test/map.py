# python中的map
a = [1, 2, 3, 4, 5]

# 输出这个列表每个值的平方
b = []

for i in a:
    b.append(i*2)

print(b)

# 使用map函数，可以使计算并行


def mul(num):
    return num*2


print(list(map(mul, a)))
