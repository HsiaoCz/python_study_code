# 字典
# 使用{}
soces = {"zhangsan": 100, "lisi": 200}
print(soces)

# 使用dict创建dict
print(dict(name="lisi", age=12))

# 空字典
d = {}
print(soces["lisi"])

print(soces.get("lisi"))

# get没取到不会报错
# 判断字典中是否存在某个key 使用in not in

# 删除字典元素
del soces["lisi"]

# 清空字典
soces.clear()

dit = {"zhang": 1, "lisi": 2}
print(dit.keys())
keys = list(dit.keys())
print(keys)

# 获取所有的键值对
print(dit.items())
# 获取所有的值
print(dit.values())

# 遍历字典
for item in dit:
    print(item, dit(item))
