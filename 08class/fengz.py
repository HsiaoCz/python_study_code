# 面向对象特征之：封装
# 封装：提高程序的安全性
# 将数据（属性）和行为（方法）包装到类对象中。在方法内部
# 对属性进行操作，在类对象外部调用
# python中没有专门的修饰符用于属性的私有
# 如果不希望在类对象外部被访问，前面可以加两个"_
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("汽车已经启动")


car = Car("雪佛兰")
car.start()


# 使用不希望被外部访问的属性
class Student:
    def __init__(self, name, age) -> None:
        self.name = name,
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
