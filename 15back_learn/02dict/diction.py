# 字典
soces = {"张三": 17, "李四": 29}
print(soces)

# 使用dict创建字典
print(dict(name="张三", age=20))

# 空字典
d = {}
print(d)

# 判断字典中的元素是否存在
print("张三" in soces)
print("张三" not in soces)

# 查找键
print(soces["张三"])
print(soces.get("lisi"))

# 获取键值和键值对
print(soces.keys())
print(soces.values())
print(soces.items())

# 打包字典
item = ["zhangsn", "lisi", "wangwu"]
press = [12, 13, 14]
d = {item: press for item, press in zip(item, press)}
