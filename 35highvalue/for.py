# for 只有一个语句
# for -in else
print("-------字符串--------")
for item in "hello":
    print(item)

# 声明整数列表
numbers = [12, 13, 14, 15]
print("--------整数列表--------")
for i in numbers:
    print(i)

# for 可迭代的对象包括 字符串、列表、元组、集合和字典
#  for和while都可以添加 else子句
# 作用主要是在循环体正常结束的时候 执行该子句
# 循环体异常退出时 不执行
for i in range(10):
    print(i)
else:
    print("over")

# 循环体中断不会执行else语句
for i in range(10):
    if i == 3:
        break
    print(i)
else:
    print("over")

# 循环体中断  不会执行else

for i in range(100, 2):
    print(i * i)
