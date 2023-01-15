# 字符串的切片操作
# 字符串本身是不可变类型，不能增删改操作
# 切片将产生新的对象
s="Hello"
print(s,id(s))
print(s[0:2])
s1=s[0:2]
print(s1)
print(s,id(s))
print(s1,id(s1))
