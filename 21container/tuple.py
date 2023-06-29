# 元组，不可变序列
lst = (1, 2, 3, 4)
# 不可变序列 改变内容后内存地址发生了变化

t = tuple(1, 2, 3)
t2 = 'zhangsa', 'lisi'
tk = ()

for i in t:
    print(i)
