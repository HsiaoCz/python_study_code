# 字符串的切片操作
# 字符串本身是不可变类型，不能增删改操作
s = "hello"
print(s, id(s))
print(s[0:2])

# 格式化字符串的方法
name = "李四"
print("hello:%s" % name)
print("hello:{0}".format(name))
print(f"hello:{name}")

# 字符串替换操作
# replace()第一个参数指定要被替换的子串
ss = "Hello,python"
print(ss.replace("python", "java"))
# 当有多个相同的子串的时候，指定替换哪一个

ls = ["hello", "world"]
print(" ".join(ls))

# 元组的连接
lss = ("hello", "python")
print("|".join(lss))

sss = "海内存知己"
print(sss.encode(encoding="GBK"))
byte = sss.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))
