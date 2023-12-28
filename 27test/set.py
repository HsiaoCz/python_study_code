# 集合
s = {1, 2, 3, 4, 5, 6}
print(s)

ss = set(range(6))
print(ss)

# 集合元素的新增操作
s.add(80)
ss.add(10)
# 使用update一次至少添加一个元素
ss.update({1, 2, 3, 4, 5})
# update 还可以放元组，列表
ss.update([1, 2, 3, 4])
ss.update((12, 13))
print(ss)

# 集合元素的删除操作
s.remove(1)
s.remove(50)  # remove方法移除元素 集合元素必须要存在 否则抛出异常
# 使用discard()方法 没有的元素也不报错 有就删了
s.discard(100)
# 使用s.pop()随便删除一个 没有参数
ss.pop()
