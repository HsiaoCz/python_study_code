# 字典
# 字典是hash结构
sorce = {"张三": 12, "李四": 15}
print(sorce)

# 使用dict创建字典
stu = dict(name="张三", age="李四")
d = {}

# 获取字典元素
print(sorce["张三"])
print(sorce.get("李四"))

# 判断key是否在字典中存在
print("张三" in sorce)
print("李四" not in sorce)

# clear清空字典
# del 删除字典
# dict.keys()可以获取字典的键
# dict.values可以获取字典的值
# dict.items()可以获取字典的键值对

# 遍历字典
for item in stu:
    print(item, stu(item))

# 打包生成字典
itemm = ["张三", "李四", "王五"]
press = [12, 13, 14]
d = {itemm: press for itemm, press in zip(itemm, press)}
print(d)
# 在打包的时候，如果元素个数不相同，会以短的那个为准
