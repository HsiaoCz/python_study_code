# while 语句 先判断循环条件 再执行循环
# while 后面可以跟 else
i = 0
while i * i < 1000 :
    i += 1

print(i)

# 这里要注意 while直到循环
# while 后面可以加else
while i * i < 10 :
    i += 1
    print(i)
else :
    print("over")

# 可以使用break 终止循环
while i < 20 :
    i += 1
    if i == 5:
        break
    print(i)
else :
    print("over")
   
 