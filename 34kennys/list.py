# 创建列表
s = [1, 2, 3, 4]
print(s)

m = []
print(m)

# 列表中的元素可以是不同的类型
mm = [1, 2, 3, "hello"]
for i in mm:
    print(i)

# 创建只有一个元素的列表
aa = [10]

# 列表的每一个元素后面都跟着一个逗号 经常省略这个逗号

# 通过list()函数创建列表
print(list("hello"))

# 列表追加元素
# append() 追加单个元素
s.append(5)
print(s)

# extend() 追加多个元素
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
lis = [1, 2, 3, 4, 5, 5, 6]

# 获取列表指定元素的索引
# 如果知道列表中存在N个相同的元素
# 只返回相同元素中的第一个
# 还可以在指定的step 和stop之间进行查找

lss = ["Hello", "world", 98, "Hello"]
print(lss.index("Hello"))  # 只返回相同元素中的第一个索引

# 在指定的范围内查找元素
print(lss.index(1, 3))
# 这里不包含 3
# 获取索引为2的元素
print(lss[3])
print(lss[-2])

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

# 列表生成式
list = [i for i in range(1, 10, 2)]
print(list)

# i 这里叫表示列表元素的表达式
# 列表元素是 2 4 6 8 10
l = [i for i in range(2, 11, 2)]
print(l)

a = "Hello"
s = a[1:3]
print(s)
# 步长 隔多少截取
m = a[0:4:2]
print(m)
print(a[1:-1])
# 截取到-1就是截取到倒数第一个，不包含倒数第一个
# 当步长为-1的时候，从左往右获取元素，所以[::-1]的结果是原始序列的倒置
# 切片的结果是列表的拷贝
sliceLss = lss[0:2]
print(sliceLss)

lstt = [2, 3, 4, 5, 6, 7, 8, 9, 12, 13]
print(lstt)
print(id(lstt))
lsttSlice = lstt[1:6:1]
print(lsttSlice)
print(id(lsttSlice))
lsll = lstt[2:7:2]
print(lsll)
print(id(lsll))
# 步长为负数的情况 切片第一个元素是列表的最后一个元素
lslll = lstt[6:0:-1]
# 使用切片对列表进行追加
lstt[4:] = lss
# 意思是切掉的部分用一个新的列表去替换
