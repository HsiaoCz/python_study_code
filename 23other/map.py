# python中的map
a = [1, 2, 3, 4, 5]

# 如何输出这个列表的每个值的平方
b = []

for i in a:
    b.append(i*2)

print(b)

# 使用map函数
# map对每个元素的计算是并行的


def mul(num):
    return num*2


print(list(map(mul, a)))
