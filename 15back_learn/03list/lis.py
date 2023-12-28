# 列表
l = [1, 2, 3, 4, 5, "hello"]
for item in l:
    print(item)

# 使用list函数可以创建列表
print(list("hello"))

# 往列表追加元素
l.append(9)
l.append("张三")
t = [12, 13, 14]
l.extend(t)

m = [23, 24, 25]
l = l+m

# 插入单个元素
l.insert(1, "hi")

# 查找列表范围内的元素
print(l.index(1, 5))
print(l.index("hello"))

# 列表的生成式
ll = [i for i in range(1, 20, 3)]
print(ll)

# 移除列表中的一个元素，如果有重复只移除一个
ll.remove(3)
# 移除不存在的元素会报错
ll.remove(2)
# pop根据指定索引删除列表
# 使用切片，原来的列表没变，产生了一个新的列表
# clear清空列表，列表还在
# del删除列表，列表没了

# 列表的排序操作
ll.sort()
print(ll)
# 按降序排列
ll.sort(reverse=False)

# 使用内置函数sorted()对列表进行排序，将产生一个新的序列
newl = sorted(ll, reverse=False)
print(newl)
