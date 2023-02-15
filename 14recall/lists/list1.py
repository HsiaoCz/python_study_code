# 创建列表的方式
s = [1, 2, 3, 4, "hello"]
for item in s:
    print(item)

s1 = [i for i in range(1, 100, 10)]
print(s1)

s2 = [i * (i + 1) for i in range(1, 10, 2)]
print(s2)
