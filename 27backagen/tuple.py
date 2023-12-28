#  元组是不可变类型
# 改变元素，内存地址发生变化
t = ("python", "world", 98)
print(type(t))

t2 = "张三", "李四", "王武"
print(type(t2))

# 元组中只有一个元素，要加上逗号，不加，默认为元素本身的类型
t1 = tuple("张三", "李四", "hello")
print(type(t1))

for i in t:
    print(i)
