# 字典 字典优点像go的map
# 字典是无序的，大括号创建
source = {"zhangsan": 100, "lisi": 200}
print(source)
print(type(source))

# 使用dict创建字典
# list创建列表,set创建集合,truple创建元组
print(dict(name="zhangsna", age=18))
# 它表示"name":"zhangsan","age":18
d = {}
print(d)
print(type(d))
# 使用键的方式获取字典元素，没有会报错
# 使用get()方式获取，没有不报错
# clear清空字典
# del删除字典中的单个元素
del source["zhangsan"]

# 获取字典所有的键
dit = {"张三": 12, "李四": 14, "王五": 23}
print(dit.keys())
# 获取字典的所有值
print(dit.values())
# 还可以将所有的key或value转换成列表
# 获取所有的键值对
items = dit.items()
print(list(items))
# 字典的生成式和别的还不太一样
ics = ["张三", "李四", "王五"]
pcs = [12, 13, 14]
d = {ics: pcs for ics, pcs in zip(ics, pcs)}
print(d)
# 打包的时候，如果元素个数不相同，会以短的为准