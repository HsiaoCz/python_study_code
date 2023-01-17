# 特殊的属性和方法
# 特殊的属性：__dict__ 获得类对象或实例对象所绑定的所有
# 属性和方法的字典
# 特殊方法 __len__() 通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
# __add__()通过重写__add__()方法，可以使用自定义对象具有"+"
# __new__() 用于创建对象
# __init__() 对创建的对象进行初始化
# dir查看一个类所绑定的所有属性和方法
print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

x=C("Bob",12)
print(x.__dict__) #获得类对象或实例对象所绑定的所有属性和方法的字典
print(C.__dict__) 
print(x.__class__) #输出对象所属的类
print(C.__bases__) # 输出父类
print(C.__base__) # 输出父类 第一个
print(C.__mro__) # 类的层次结构
print(A.__subclasses__()) #输出子类的列表

