# 列表排序
l = [23, 12, 3, 24, 17, 25, 13]
print(l)
l.sort()
print(l)
# sort()
# 默认按照升序排列
# 排序是在原列表中进行的
# 使用reverse=true 按照降序排序
l.sort(reverse=True)
# 当reverse=falue时就是升序排序
l.sort(reverse=False)

# 使用内置函数sorted()对列表排序 将产生一个新序列
newl = sorted(l, reverse=True)
print(newl)
newl1 = sorted(l, reverse=False)
print(newl1)
