# 集合可以看成没有key的字典
s = {1, 2, 3, 4, 5, 6}
print(type(s))

s1 = set(range(10))
# 可以将列表中的元素转成集合
# 可以将tuple中的元素转成集合
# 可以将字符串转成集合
# 使用set定义一个空集合
s2 = set()
print(type(s2))

# 集合的相关操作
# 集合新增操作
s.add(12)
# 一次添加多个元素

s.update(12, 13, 14, 15)

# 集合的删除操作
s.remove(1)
s.remove(12)

# discard() 删除元素，没有也不报错
s.discard(122)
# 随便删除一个元素，没有参数
s.pop()

# 使用clear() 清空集合中的元素
ss = {1, 12, 13, 4, 9, 7, 8}
# 使用reverse进行排序
# reverse=true 按照降序排序
ss.sort(reverse=True)
ss.sort(reverse=False)

# 使用内置函数sorted()对列表排序，将产生一个新序列
new1 = sorted(ss, reverse=True)
print(new1)
new22 = sorted(ss, reverse=False)
print(new22)
