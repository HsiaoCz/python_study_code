# 比较运算符
# 结果为布尔值
print(1 >= 2)
print(2 >= 3)

a = "hello"
b = "hallo"

print(a == b)

# 比较字符串的大小，会逐一比较两个字符串的unicode编码的大小
s = [1, 2]
m = ["m"]

print(s == m)
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
# 算术运算符
# 这里面有些不一样的东西
a = 10
b = 3
print(a**b)  # 打印a的b次幂
print(a // b)  # a除以b商的最大整数 10/3=3.3333...
# 这里直接取3 后面的去掉了
# 这里和取余a%b相对
print(a % b)
