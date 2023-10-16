# for 只有一个语句
# for in else

for item in "hello":
    print(item)

# 声明整数列表
num = [1, 2, 3, 4, 5]
for i in num:
    print(i)

# for 可迭代的对象包括 字符串、列表、元组、集合、字典
#  for和while都可以添加 else子句
# 作用主要是在循环体正常结束的时候 执行该子句
# 循环体异常退出时 不执行
for i in range(10):
    print(i)
else:
    print("over")

for i in range(11):
    if i == 3:
        break
    print(i)
else:
    print("循环体异常提出不会执行该语句")

# 循环体中断，不会执行else
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
