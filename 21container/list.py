l = [1, 2, 3, 4]
print(l)

# 列表中的元素可以是不同的类型

m = [1, 2, 3, "hello"]

for i in m:
    print(i)

# 列表增加元素
m.append(4)
m.append("hi")

for i in m:
    print(i)

# 使用list创建列表
print(list(1, 2))

# 将一个列表追加到另一个列表
ll = [22, 11, 44, 33]
m.extend(ll)

for i in m:
    print(m)


def bianli(m):
    for i in m:
        print(i)


# 使用+=来追加
m += [123, 124, 125]

bianli(m=m)

# 往列表里插入元素

m.insert(1, 221)

# 列表中存在N个相同的元素，只返回相同元素中的第一个
# 查询的元素在列表不存在，会抛出错误

lss = ["hello", "world", 98, "hello"]
print(lss.index("hello"))
print(lss.index(1, 3))

# 列表的生成式
lis = [i for i in range(1, 10, 2)]
print(lis)

# 移除列表中的元素

lll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 移除一个元素
lll.remove(3)
# pop根据索引删除元素
l.pop(1)
l.pop()

# 没有索引则弹出最后一个元素
# lll.clear() 清空列表
# 列表还在，只是没元素了
# del lll 删除列表
# 列表没了
