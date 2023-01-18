# 字符串的切片操作
# 字符串本身是不可变类型，不能增删改操作
# 切片将产生新的对象
s = "Hello"
print(s, id(s))
print(s[0:2])
s1 = s[0:2]
print(s1)
print(s, id(s))
print(s1, id(s1))
# 步长 两个元素之间的索引间隔为2
print(s[::2])
# 步长为负，索引从后往前
print(s[::-1])
# 格式化字符串
# 格式化字符串的两种方式
# 1.使用%作为占位符
# 2.使用{}作为占位符
name = "张三"
print("hello:%s" % name)
age = 12
print("hello:%s,%d" % (name, age))

# 使用{}进行占位
print("hello:{0},{1}".format(name, age))

# 使用f进行格式化
print(f"Hello{name},{age}")

# 表示精度和宽度的格式化字符串
print("%d" % 99)
# %10d表示宽度
print("%10d", 99)
print("%.3f", 3.121314)
# 还可以同时表示宽度和精度
