# 创建列表
s = [2, 1, 3, 4]
print(s)
m = []
print(m)
# 列表中的元素可以是不同的类型的
mm = [1, 2, 3, "Hello"]
for i in mm:
    print(i)
# 创建只有一个元素的列表
aa = [10]
print(aa)

# 列表的每一个元素后面都跟着一个逗号，但经常省略这个逗号

# 通过list()函数创建列表
print(list("Hello"))

# 列表追加元素
# append()追加单个元素
s.append(5)
print(s)
# extend()追加多个元素
t = [6, 7, 8]
s.extend(t)
print(s)
# 可以使用+=来追加多个元素
s += [12, 13, 14]

# 往列表中插入元素
s.insert(2, 19)
print(s)

# 对列表元素进行替换
s[5] = 23
print(s)

# 列表可以存储重复的数据
lis = [1, 2, 3, 4, 4, 4]

# 获取列表指定元素的索引
# 如果知道列表中存在N个相同的元素，只返回相同元素中的第一个
# 如果查询的元素在列表中不存在，会抛出错误
# 还可以在指定的step 和stop之间进行查找

lss = ["Hello", "world", 98, "Hello"]
print(lss.index("Hello"))  # 只返回相同元素中的第一个索引

# 在指定的范围内查找元素
print(lss.index(1, 3))
# 这里不包含 3
# 获取索引为2的元素
print(lss[3])
print(lss[-2])

# 列表生成式
lists = [i for i in range(10)]
print(lists)

# 移除元素
lll = [1, 2, 3, 4, 5, 6, 7]
lll.remove(3)
# pop 可以删除指定index的元素，不指定index会删除最后一个元素
lll.pop()

# clear会清空列表，但是列表还在
# del 删除列表，列表会没

# 列表排序
l = [23, 12, 3, 24, 17, 25, 13]
print(l)
l.sort()
print(l)
# sort()
# 默认按照升序排列
# 排序是在原列表中进行的
# 使用reverse=true 按照降序排序
l.sort(reverse=True)
# 当reverse=falue时就是升序排序
l.sort(reverse=False)

# 使用内置函数sorted()对列表排序 将产生一个新序列
newl = sorted(l, reverse=True)
print(newl)
newl1 = sorted(l, reverse=False)
print(newl1)
