# 可变的位置参数
def func(*a):
    print(a)
    
func(10,20,30)

# 可变的关键字参数，结果为字典
def hello(**args):
    print(args)

hello(a=10,b=20,c=30)

# 如果一个函数即有位置参数，又有格式可变的关键字参数
# 位置参数要放在关键字参数之前

def Cegg(*a,**b):
    print(a)
    print(b)
    
# 函数有多个放回值得时候，结果为元组