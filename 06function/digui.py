# 递归函数
# 递归，在函数内调用函数本省
# 递归调用得有终止条件
# 递归调用的调用过程：
# 每递归调用一次函数，都会在栈内存中分配一个栈帧
# 每执行完一次函数，都会释放相应的空间
# 递归的优点是代码简单，思路清晰
# 缺点 极大的占用内存
def fb(a):
    if a==1 or a==2:
        return 1
    return fb(a-1)+fb(a-2)

result=fb(20)
print(result)

# 计算阶乘
def jieC(a):
    if a==1:
        return 1
    return a*jieC(a-1)

re=jieC(10)
print(re)