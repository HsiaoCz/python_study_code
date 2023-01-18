# 类的创建
# 类 一类事物的抽象
# 在Python中 数据类型是类
# 例如int
# 对象 类的实例
# 像 1，2 就是int类的实例
# 类的创建语法 class 类名
class Student:
    pass
# 类名首字母大写，其余小写
# 类是类的对象
# 直接写在类的变量称为类属性


class Hello:
    # 属性
    native_pace = "上海"
    # 定义在类中的称为方法  在类外的称为函数
    # 初始化方法

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 使用self 进行修饰的 为实例方法

    def hello(self):
        print("hello")
    # 使用staticmethod 进行修饰的是静态方法

    @staticmethod
    def hi():
        print("静态方法")
    # 使用classmethod 进行修饰的是类方法

    @classmethod
    def cm(cls):
        print("类方法")


# 创建对象
stu1 = Hello("张三", 18)
# 直接输出stu1 输出的是stu1的内存地址
stu1.hello()
print(stu1.name)
print(stu1.age)

# 也可以这样调用hello
Hello.hello(stu1)
# 属性对所有的对象共享
