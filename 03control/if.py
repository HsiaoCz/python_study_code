# if 语句
a = 12
b = 13
if a > b:
    print("Hello")

# if-else 条件判断语句
s = int(input("请输入一个数字:\n"))
if s > 60:
    print("真棒")
else:
    print("真垃圾")

# if-elif-else条件判断语句
m = int(input("请输入一个数字:\n"))
if m > 10 and m < 20:
    print("可以")
elif m > 20 and m < 30:
    print("还不错")
elif m > 30 and m < 40:
    print("继续努力")
else:
    print("牛哇")
