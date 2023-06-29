# 集合
# 集合也是无序的
# 集合可以看成是没有key的字典

s = {1, 2, 3, 4, 5, 6, 7}
print(s)

# 集合不允许重复
s1 = set(range(12))
print(set([1, 2, 3, 4]))

print(set("hello"))

# 使用set定义一个空集合
s2 = set()
print(type(s2))

# 集合中的新增操作
s2.add(10)
s2.add(11)

s2.update({1, 2, 3, 4, 5})
s2.update([111, 222])
s2.update((11111, 2222))

# 集合中的删除操作
s.remove(1)
s.remove(50)
# remove 删除不存在的会报错
# 使用discard() 没有也不报错
s2.discard(111)

# pop随便删除一个
s2.pop()

# 清空
s2.clear()
