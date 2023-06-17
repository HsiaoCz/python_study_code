# 集合
# 集合无序，集合中的元素经过hash之后确定元素的位置
# 集合中的元素不允许重复
s = {1, 2, 3, 4, 5, 6}
print(s)

# 使用set创建集合
print(set(range(1, 10)))
# 定义空集合
ss = set()
# 往集合中增加元素
ss.add(11)
# 使用update可以往集合中添加多个元素
ss.update([12, 13, 14])
print(ss)
# 使用remove删除集合，集合中的元素必须存在，否则报错
# 使用discard()删除集合元素，没有不报错，有就删除
# 使用pop可以删除一个元素，没有参数
# clear()清空集合

# 集合之间的关系
# 1、集合是否相等
# 集合中的元素只要一样，即使位置不同，两个集合也是相等的
# 2、一个集合是否是另一个集合的子集 issubset
# 3、一个集合是否是另一个集合的超集 issuperset
# 4、两个集合是否含有交集isdisjoint()是否没有交集
# 集合的数学操作
# 1、交集intersection &
# 2、并集union |
# 3、差集difference -
# 4、对称差集symmetric_difference ^

# 集合的生成式
s7 = {i for i in range(10)}
print(s7)

