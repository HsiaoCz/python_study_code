# 函数参数的传递
def func(a, b):
    print("a:", a)
    print("b:", b)
    a = 100
    b.append(10)
    print("a:", a)
    print("b:", b)


# 传入的参数是不可变类型时，在函数体内改变参数的值，对函数外的参数没有影响
# 传入可变参数，在函数内修改参数的值，对函数外的参数也会改变
a = 12
b = [12, 13, 14]
print("a:", a)
print("b:", b)
func(a, b)
print("a:", a)
print("b:", b)
