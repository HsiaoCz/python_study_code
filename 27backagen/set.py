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
