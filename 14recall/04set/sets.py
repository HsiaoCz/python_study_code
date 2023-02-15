# 集合，无序
# 集合中的元素不允许重复
s = {1, 2, 3, 4, 5}
s1 = set(range(10))
# 使用set可以将列表转成集合，字符串转成集合，元组转成集合
# 定义空集合
# ss={} 这样定义的是一个字典
ss = set()
type(type(ss))
# 新增集合元素
ss.add(10)
ss.add(11)
# add 新增一个 update新增多个
s.remove(1)
# remove移除元素，没有会报错
s.discard(2)
# discard移除元素，没有不报错
s.pop()  # 随机删除，没有参数
ss.clear()  # 清空集合

# 两个集合只要元素相同就相等
# 集合之间的关系
# 一个集合是否是另一个集合的子集 issubset
# 一个集合是否是另一个集合的超集 issuperset()
m = {1, 2, 3, 4, 5}
m1 = {1, 2, 3}
t = m1.issubset(m)
print(t)
t = m.issuperset(m1)
print(t)

# 两个集合是否有交集
# isdisjoint() 判断是否没有交集
t = m1.isdisjoint(m)  # flase代表有交集
print(t)

# 集合的数学操作
s4 = {10, 20, 30, 40}
s5 = {20, 30, 60, 12}
# 交集
print(s4.intersection(s5))
print(s4 & s5)
# 并集
print(s4.union(s5))
print(s4 | s5)
# 差集
print(s4.difference(s5))
print(s5 - s4)
# 对称差集
print(s4.symmetric_difference(s5))

