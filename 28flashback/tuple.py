# 不可变序列与可变序列
# 可变序列 列表，字典
lst = [10, 20, 45]
print(id(lst))
lst.append(300)
print(id(lst))
# 不可变序列 字符串，元组
s = "hello"
print(id(s))
s += "world"
print(id(s))
# 不可变序列 改变内容后内存地址发生了改变
# 元组的创建方式
# 第一种创建方式，使用()
t = ('Python', 'world', 98)
print(type(t))
print(t)
# 也可以省略小括号
t2 = 'zhangsan', 'lisi', 100
print(type(t2))
print(t2)

# 元组中只有一个元素 要加上逗号
# 不加上逗号，会默认为它本省的类型
t4 = ("张三",)

# 第二种创建方式，使用内置函数tuple()
t1 = tuple(('张三', "李四", "王五"))
print(type(t1))
print(t1)

# 空元组
tk = ()
print(tk)
# 元组的遍历
# 第一种遍历方式
print(t[1])
print(t[2])
# 也可以使用for 来遍历
for i in t:
    print(i)
