# python中的类型转换
# 隐式转换
a = 1 + True
print(a)

b = 1.0 + 1
print(b)

c = 1.0 + 1 + True

# 隐式类型转换，不同类型之间进行计算发生的值的类型改变
# 显示转换
print(int(False))
print(int(1.0))
print(float(4))
print(bool(1))

# 显式转换需要使用类型函数
