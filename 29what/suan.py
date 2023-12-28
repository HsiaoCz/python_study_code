# 算术运算符
# 这里面有些不一样的东西
a = 10
b = 3
print(a ** b)  # 打印a的b次幂
print(a // b)  # a除以b商的最大整数 10/3=3.3333...
# 这里直接取3 后面的去掉了
# 这里和取余a%b相对
print(a % b)
# while 语句 先判断循环条件 再执行循环
# while 后面可以跟 else
i = 0
while i * i < 1000:
    i += 1

print(i)

# 这里要注意 while直到循环
# while 后面可以加else
while i * i < 10:
    i += 1
    print(i)
else:
    print("over")

# 可以使用break 终止循环
while i < 20:
    i += 1
    if i == 5:
        break
    print(i)
else:
    print("over")

