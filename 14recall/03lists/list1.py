# 创建列表的方式
s = [1, 2, 3, 4, "hello"]
for item in s:
    print(item)

s1 = [i for i in range(1, 100, 10)]
print(s1)

s2 = [i * (i + 1) for i in range(1, 10, 2)]
print(s2)

# 使用ist()也可以创建列表
print(list("Hello"))
# append() 追加元素
s.append(10)
m = [11, 12, 13]
s.extend(m)
s += [14, 15, 16]
# insert()插入元素 index获取索引

# 移除列表元素
s.remove(11)
s.remove(12)

# 列表排序
s.sort()
print(s)
s.sort(reverse=True)
# sort()对原来的列表进行排序
# sorted对列表排序，并且产生一个新的列表
news = sorted(s, reverse=True)

# max返回最后一个元素
# min返回第一个元素
print(max(s))
print(min(s))
