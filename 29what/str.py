# 字符串的比较操作
# 运算符 >，>=，<，<=
# == 和 is
# == 比较的是value是否相等
# is 比较的是内存地址是否一致
a = "Hello,hello"
# i 查找第一次出现的位置
print(a.index("He"))
print(a.index("lo"))
print(a.find("e"))
# 查找最后出现的位置
print(a.rindex("lo"))
print(a.rfind("e"))
# 使用find() 来查找元素 建议
# 这种方式不会抛异常

# 字符串的替换操作
s = "Hello,python"
print(s.replace("python", "java"))
ss = "python,python,python"
print(ss.replace("python", "java", 1))
# join()用于列表或者元组
ls = ["hello", "java"]
print("".join(ls))
print("|".join(ls))

# 元组的连接
lss = ("hello", "python")
print("|".join(lss))

# 字符串的切片讲产生新的对象
# 因为字符串本身是不可变的类型
print(s[0:6:2])

# 格式化字符串
# python中格式化字符串的方式有几种
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

# 字符串的分割操作
s1 = "hello|hi|world"
print(s1.split(sep="|", maxsplit=1))
print(s1.split(sep="|", maxsplit=2))
