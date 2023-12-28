# python的容器类型

# 字典 {}
s = {"张三": 108, "lisi": 18}
s1 = dict(name="lisi", age=20)
print(s1)
print(s)

# max返回最后一个元素
# min返回第一个元素
a = "hello"
print(max(a))
print(min(a))
print(len(a))

# 列表[],列表中的元素可以不相同
s = [2, 1, 3, 4]
print(type(s))
# list函数可以创建列表
# 往列表中追加元素
# append追加单个元素
# extend追加多个元素
# 可以使用+=来追加
# insert可以在指定的索引处追加
# 列表中的元素可以重复，但是查询的时候，会返回找到的第一个
# 列表生成式
lis = [i for i in range(1, 10, 2)]

# 集合之间的关系
# 1、集合是否相等，集合元素的内容相同，索引不同也相等
# 2、一个集合是否是另一个元素的子集 issubset
# 3、一个集合是否是另一个集合的超集issuperset
# 4、两个集合是否含有交集isdisjoint() 这个代表是否没有交集

# 集合生成式
s2 = {i for i in range(10)}
print(s2)
