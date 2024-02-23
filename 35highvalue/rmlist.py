# 移除一个元素，remove
# 从列表中移除一个元素，如果有重复元素只移除第一个元素
l = [1, 2, 3, 4, 4, 5, 5, 6, 6]
l.remove(3)
print(l)
l.remove(4)
# 移除不存在的元素会报错
# pop根据索引删除元素
l.pop(1)
l.pop(2)
# 指定索引位置不存在，将抛异常
l.pop()
# 不指定参数，将删除最后一个元素
# 使用切片 原来的列表没变，产生了一个新的列表
# 不产生新的列表对象，而是删除原列表的内容
l[0:2] = []
ls = [1, 2, 3, 4, 5, 6]
ls.clear()
print(ls)
# clear 清空了列表的元素
# del删除列表
lsls = [1, 2, 3, 4, 5]
del lsls
print(lsls)