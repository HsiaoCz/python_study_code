# list 列表
s = [1, 2, 3, 4]
print(s)

m = []
print(type(m))

# 列表中的元素可以是不同的类型
mm = [1, 2, 3, "hello"]

for i in mm:
    print(i)

# 创建一个只有一个元素的列表
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

# 移除列表中的元素 remove
# 从列表中移除一个元素，如果有重复元素只移除第一个元素
l = [1, 2, 3, 4, 5, 6, 7]
l.remove(3)

print(l)
l.remove(4)

# 移除不存在的元素会报错
# pop根据索引删除元素
l.pop(1)
l.pop(2)
# 指定索引位置不存在，将抛异常
l.pop()
# 不指定参数，将删除最后一个元素
# 使用切片 原来的列表没变，产生了一个新的列表
# 不产生新的列表对象，而是删除原列表的内容
l[0:2] = []
ls = [1, 2, 3, 4, 5, 6]
ls.clear()
print(ls)
# clear 清空了列表的元素
# del删除列表
lsls = [1, 2, 3, 4, 5]
del lsls
print(lsls)

# 列表生成式
liss = [i for i in range(1, 20, 2)]
print(liss)

# 列表排序
lll = [23, 12, 3, 24, 17, 25, 13]
print(lll)
lll.sort()

print(lll)
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
