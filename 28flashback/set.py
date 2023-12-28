# 集合也是无序的，集合的元素也是经过hash函数
# 来确定集合中元素位置的
# 创建集合 集合中的元素不允许重复
# 集合可以使用{}来创建
s = {2, 3, 4, 5, 6, 5, 4, 3, 2}
print(s)
# 集合中的元素不允许重复
# 也可以使用set()方法来创建集合
s1 = set(range(6))
print(s1)
# 将列表中的元素转成集合中的元素
print(set([1, 2, 3, 4, 5]))
# 将元组转换成集合
print(set((1, 2, 3, 4, 5)))
# 将字符串转换成集合
print(set("python"))
# 定义一个空集合
# 如果直接使用{}定义的是一个字典
ss = {}
print(type(ss))
# 使用set()来定义空集合
sss = set()
print(sss)
print(type(sss))

# 集合中的相关操作
# 集合中的判断操作
print(10 in s)
print(11 not in s)

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
sss.pop()

# 使用clear() 清空集合中的元素
