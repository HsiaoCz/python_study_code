l = [1, 2, 3, 4]
print(l)

# 列表
# 创建列表
s = [1, 2, 3, 4, 5]
print(s)

for i in s:
    print(i)

# 通过list来创建列表
print(list("hello"))

# 往列表中追加元素
s.append(12)
# 往列表中追加多个元素
a = [22, 23, 24]
s.extend(a)

# 还可以使用+=来进行追加
# 往列表中插入元素
s.insert(1, 22)
# 获取列表的索引
print(s.index(2))

# 列表的生成式
list = [i for i in range(1, 20, 2)]
print(list)

# 删除元素 这种删除如果元素不存在会报错
s.remove(5)

# pop 可以根据索引删除元素
s.pop(1)
# clear清除元素
# del 删除列表

