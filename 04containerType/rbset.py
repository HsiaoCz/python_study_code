# 集合之间的关系
# 1.集合是否相等
# 两个集合只要内容一样，元素位置不同没关系，这两个集合就是相等的
s = {1, 2, 3, 4}
s1 = {3, 1, 4, 2}
print(s == s1)
print(s != s1)

# 一个集合是否是另一个集合的子集 issubset
# 如果一个集合的元素在另一个集合里都有 就是另一个集合子集
s2 = {1, 2}
print(s2.issubset(s1))
# 一个集合是否是另一个集合的超级 issuperset
# 包含子集的全部，自己还有多的
s3 = {2, 3}
print(s.issuperset(s3))

# 两个集合是否含有交集 isdisjoint() 是否没有交集
# 所有有交集为false
print(s3.isdisjoint(s3))

# 集合的数学操作
# 交集
s4 = {10, 20, 30, 45}
s5 = {10, 30, 12, 34}
print(s4.intersection(s5))
# 等价于 & 符号
print(s4 & s5)

# 并集操作
print(s4.union(s5))
# 等价于 |
print(s4 | s5)
# 交集和并集之后两个集合都没有发生变化

# 差集操作
print(s4.difference(s5))
# 和相减操作是等价的 -
print(s5-s4)

# 对称差集
print(s4.symmetric_difference(s5))
# 等价于 ^
print(s4 ^ s5)

# 集合生成式
# 生成式没有元组的，元组没有生成式
s7 = {i for i in range(10)}
print(s7)
# 生成的集合是无序的
