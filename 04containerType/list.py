# 创建列表
s=[2,1,3,4]
print(s)
m=[]
print(m)
# 列表中的元素可以是不同的类型的
mm=[1,2,3,"Hello"]
for i in mm :
    print(i)
# 创建只有一个元素的列表
aa=[10]
print(aa)

# 列表的每一个元素后面都跟着一个逗号，但经常省略这个逗号

# 通过list()函数创建列表
print(list("Hello"))

# 列表追加元素
# append()追加单个元素
s.append(5)
print(s)
# extend()追加多个元素
t=[6,7,8]
s.extend(t)
print(s)
# 可以使用+=来追加多个元素
s+=[12,13,14]

# 往列表中插入元素
s.insert(2,19)
print(s)

# 对列表元素进行替换
s[5]=23
print(s)