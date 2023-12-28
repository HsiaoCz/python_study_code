# for

for item in "hello":
    print(item)

num = [1, 2, 3, 4, 5]
for e in num:
    print(e)

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
