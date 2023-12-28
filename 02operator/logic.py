# python的逻辑运算只有三个
# 逻辑非 not ! 取反
# 逻辑或 or | 有一个为真则为真
# 逻辑与 and & 都为真才为真
# 结果为布尔值
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

# python 的逻辑与和逻辑或也采用的是短路设计
# 所谓的短路指在计算过程中，只要结果确定，则不再计算后面的表达式，从而提高效率
# 例如 and 只要前面的表达式为假后面的就不用计算
# or 只要第一个为真后面的就不用计算
