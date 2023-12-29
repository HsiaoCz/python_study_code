# class
# 类的创建
# 在python中一切皆是类
class Student:
    pass


# 类名首字母大写，其余小写
# 类是类的对象
# 直接写在类的变量称为类属性


class Hello:
    # 属性
    native_pace = "上海"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 使用self 进行修饰的 为实例方法

    def hello(self):
        print("hello")

    # 使用staticmethod 进行修饰的是静态方法
    # 静态方法不依赖于类或实例的方法，可以直接通过类名或实例名调用
    # 静态方法没有类似self、cls这样特殊参数，因此无法调用任何属性和类方法
    # 静态方法可以在不创建类实例的情况下调用
    @staticmethod
    def hi():
        print("静态方法")

    # 使用classmethod 进行修饰的是类方法
    # 类方法 cls传递当前类对象
    # 类方法可以调用类的属性，类的方法，实例化对象等
    # classmethod的作用是：可以在class内实例化class
    # 本质上是，可以为一个类创建一些预处理的实例

    @classmethod
    def cm(cls):
        print("类方法")
