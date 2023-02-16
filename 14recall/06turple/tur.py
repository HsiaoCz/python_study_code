# 可变序列和不可变序列
# 可变序列 改变内容后地址不变
lis = [1, 2, 3, 4]
print(id(lis))
lis.append(5)
print(id(lis))

# 可变序列 改变内容后地址会发生改变
s = "hello"
print(id(s))
s += "!hi"
print(id(s))

# 集合也是可变序列
m = {1, 2, 3, 4, 5}
print(id(m))
m.add(4)
print(id(m))
