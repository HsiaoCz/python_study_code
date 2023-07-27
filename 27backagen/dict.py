# 使用{}来创建字典
soces = {"张三": 100, "李四": 90}
print(soces)
print(type(soces))

# 第二种创建字典的方式
student = dict(name="lisi", age=24)
print(student)

# 空字典
d = {}
print(type(d))

# 获取字典的方式
# [] 没有键会报错
# get方式不会报错，会输出Noneqkkkj
print(soces["张三"])
print(soces.get("张三"))

# 判断key是否在字典中存在
print("张三" in soces)
print("Lisi" not in soces)
# 删除字典
# 删除单个元素
del soces["张三"]
print(soces)
# 清空字典的元素
soces.clear()
# 新增修改使用key
soces["陈留"] = 100
soces["陈留"] = 200
print(soces)

# 获取所有的键
dit = {"张三": 12, "李四": 14, "王五": 23}
# 获取所有的键
keys = dit.keys()
print(keys)
print(type(keys))
# 将所有key组成的视图转换成列表
print(list(keys))

# 获取所有的value
values = dit.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的键值对
items = dit.items()
print(items)
print(list(items))  # 转换之后的列表元素是由元组组成的

# 字典元素的遍历
for item in dit:
    print(item, dit(item))
# 获取使用dit.get(item) 获取字典的值
# 字典中的key不允许重复
# 字典中的元素无序
# 字典中的key必须是不可变对象
# 字典也可以根据需要动态的伸缩
# 随着使用对象的增加 会增大内存
# 字典会浪费较大的内存，是一种使用空间换时间的数据结构
# 字典的查询速度很快
# 字典生成式 使用内置函数zip()生成字典
# 使用两个列表
itemm = ["张三", "李四", "王五"]
press = [12, 13, 14]
d = {itemm: press for itemm, press in zip(itemm, press)}
print(d)
# 在打包的时候，如果元素个数不相同，会以短的那个为准
