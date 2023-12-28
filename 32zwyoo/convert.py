# 类型转换
# 隐式转换
a = 1 + True
print(a)
b = 1.0 + 1
print(b)
c = 1.0 + 1 + True
print(c)

# 隐式转换，不同类型之间计算发生的值类型改变
# 显示转换
print(int(False))
print(int(1.0))
print(float(5))
print(bool(1))
