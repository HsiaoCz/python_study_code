# 类的创建
# python中一切都是类
# 数据类型也是类
# int是类,1,2都是int类的实例


class Student:
    pass


# 类的首字母大写,其余小写
# 属性写在类的内部


class Hello:
    # 属性
    native_pace = "上海"

    # 定义在类中的方法,类外的称为函数
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # 使用self进行修饰的 是实例方法

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


# 面向对象之封装
# 将数据（属性）和行为（方法）包装到类对象中。在方法内部
# 对属性进行操作，在类对象外部调用
# python中没有专门的修饰符用于属性的私有
# 如果不希望在类对象外部被访问，前面可以加两个"_


# 使用不希望被外部访问的属性
class Student:
    def __init__(self, name, age) -> None:
        self.name = (name,)
        self.__age = age  # 不希望在类的外部进行使用

    def show(self):
        print(self.name, self.__age)


stu = Student("张三", 19)
stu.show()
# 在类的外部使用
print(stu.name)
print(stu.__age)  # 在这里运行会报错
# 可以通过类名来访问
print(stu._Stuent.__age)


# 多态
# 多态就是具有多种形态，它是指，即便不知道一个变量所引用的对象到底是什么类型
# 仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法


class Animal:
    def eat(self):
        print("动物会吃")


class Dog(Animal):
    def eat(self):
        print("狗吃骨头")


class Cat(Animal):
    def eat(self):
        print("猫吃小鱼")


# 定义一个函数


def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
# 多态 在go语言里 使用interface来实现
# 鸭子类型

# 继承 继承的语法格式
# class 子类类名(父类1，父类2):
# 如果一个类没有继承任何类，则默认继承object
# python 支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造方法

# 使用super().__init__(name)调用父类的属性

# object类是所有类的父类，因此所有类都有object类的属性和方法
# 内置函数dir()可以查看指定对象所有属性
# Object有一个__str__()方法，用于返回一个对于对象的描述
# __str__()函数经常用于print()方法，帮助我们查看对象的信息
# 所有经常重写此方法