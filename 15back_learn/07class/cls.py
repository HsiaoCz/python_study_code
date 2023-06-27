# python的类

# 如果不希望在外部访问一个属性
# 可以在属性前面加上__
# self.__hello="lll"
# 不过还是可以访问到

class Hello:
    def __init__(self, name, age) -> None:
        self.name = name,
        self.age = age,

    def hello(self):
        print(f"hello My man,{self.name},{self.age}")


he = Hello("zhangsan", 12)
he.hello()

# 可以动态的为一个对象绑定属性和方法
# 不过只有当前这个对象访问这些属性和方法

he.gender = "nan"
print(he.name, he.age, he.gender)

# 绑定动他方法


def eat():
    print("eat some thing")


he.eat = eat()
he.eat()

# copy.copy是浅拷贝
# 浅拷贝只拷贝对象的元素，对象包含的子对象不会拷贝
# copy.deepcopy对象包含的子对象也会拷贝

# 多态


class Animal:
    def eat(self):
        print("动物会吃")


class Dog(Animal):
    def eat(self):
        print("狗吃骨头")


class Cat(Animal):
    def eat(self):
        print("猫吃鱼")


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())

# 继承


class Min:
    def __init__(self, name) -> None:
        self.name = name

    def eat():
        print("吃东西")


class Minn(Min):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    def say():
        print("hello")

# 类的静态方法
# 使用staticmethod修饰
# 与对象无关的方法
# 没有this self这样的参数
# 不能调用任何属性和方法

# 类方法
# cls传递当前的对象
# 类方法可以调用类的属性和方法
# 通过classmethod修饰

# 方法重写
# 但是会执行之前父类的方法
# 通过super调用父类的方法和属性

# 一些特殊的方法
# __len__() 可以计算长度
# __add__() 可以使对象获得加操作
# __new__() 构造函数


class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        obj = super.__new__(cls)
        return obj

# 特殊的属性
# __dict__获得类对象或实例对象绑定的所有属性和方法的字典
# __new__() 用于创建对象
# __init__()用于初始化对象
# __class__对象所属的类
# __bases__对象的父类
# __base__ 输出父类，第一个
# __mro__类的层次结构
# __subclasses_()输出子类列表
