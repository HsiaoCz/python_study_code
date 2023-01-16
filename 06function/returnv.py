# 函数的返回值，当函数返回多个值的时候，结果为元组
def fun(num):
    odd=[] # 存奇数
    even=[] # 存偶数
    for i in num:
        if i%2: # 每个对象都有一个布尔值，当i%2 为True，否则为True
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,20,30,40,13,15,17,21]))
# 函数由多个返回值的时候，结果为元组
# 每个对象都有一个布尔值
# 0的布尔值为False 非零的布尔值为True
# 如果函数没有返回值，函数执行完毕之后，不需要给调用处提供数据
# return可以不写
# 函数只有一个返回值，返回类型
# 函数有多个返回值的时候，返回的结果是一个元组

    