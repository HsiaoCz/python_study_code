# python中的类
class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"在吃饭")


# python动态的绑定数据
# 只有当前的对象可以访问到
stu1 = Student("张三", 14)
stu1.gender = "男"
print(stu1.name, stu1.age, stu1.gender)

# 类的深浅拷贝问题
# 浅拷贝，对象包含的子对象内容不拷贝
# 源对象和子对象会引用同一个子对象
# 深拷贝，使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象
# 源对象和拷贝对象不会引用同一个子对象
# copy.copy() 浅拷贝
# copy.deepcopy() 深拷贝
# 多态：
# 即便不知道一个变量所引用的对象到底是什么类型
# 依然可以通过这个变量调用方法，在运行过程中根据变量所引用的对象类型，动态决定调用哪个对象中的方法


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


fun(Cat())
fun(Dog())
fun(Animal())

# @staticmethod:静态方法
# 静态方法不依赖于类或实例的方法，可以直接通过类名或实例名调用
# 静态方法没有类似self、cls这样的特殊参数，因此无法调用任何属性和类
# 静态方法可以在不创建类实例的情况下调用

# @classmethod:类方法
# 使用cls传递当前对象
# 类方法可以调用类的属性，类的方法，实例对象等
# 作用是可以在class内实例化class
# 本质上，可以为一个创建一些预处理的实例
