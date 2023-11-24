# 使用{}来创建字典
socres = {"张三": 100, "李四": 90}
print(socres)
print(type(socres))

# 第二种创建字典的方式
student = dict(name="张三", age=20)
print(student)

# 空字典
d = {}

print(d)

# 获取字典的元素
# 使用第一种方式:[]
# 如果查找的键不存在 []的形式会报错
# get()的方式不会报错 会输出一个Noneqkkkj
print(socres["张三"])
# 使用get()方法也能获取字典
print(socres.get("张三"))

# 判断key在字典中是否存在
print("张三" in socres)
print("李四" not in socres)

# 删除字典
# 删除单个元素
del socres["张三"]
print(socres)
# 清空字典的元素
socres.clear()
# 新增修改使用key
socres["陈留"] = 100
socres["陈留"] = 200
print(socres)

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
