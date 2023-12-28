# 创建列表
s = [1, 2, 3, 4]
print(s)

# python列表中的元素可以是不同的类型
# 列表中的每个元素后面都跟着一个逗号，但是经常省略
# 可以使用list函数创建列表
print(list(1, 2, 3, 4, 5))

# appand 追加元素
s.append(5)
s.append(6)

m = ["hello", 12, 31, 24, 25]

# extend追加多个元素
s.extend(m)
# +=也可以追加元素
# 使用insert可以插入元素
s.insert(222, 223)

# index可以获取列表中指定元素的索引
# 如果列表中存在N个相同的元素，只返回相同的元素的第一个
print(s.index("hello"))


# 移除一个元素
# 如果有重复的，只移除第一个
s.remove(1)
s.remove(2)

# pop 根据索引删除元素
# 索引不存在，将抛异常
s.pop()
s.pop(5)

# 对列表进行切片
sm = s[0:6]
print(sm)

# clear 清空列表
# del 删除列表
# 列表生成式
ll = [i for i in range(1, 100, 1)]
