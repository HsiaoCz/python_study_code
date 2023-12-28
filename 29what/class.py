# python是一门动态语言
# python的对象创建后，可以动态的绑定属性和方法
# 一个student类可以创建很多个实例，每个实例对象的属性值不同

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"在吃饭")


stu1 = Student("张三", 16)
stu2 = Student("lisi", 23)

stu1.gender = "男"
print(stu1.name, stu1.age, stu1.gender)

# 动态的绑定一个属性，只有当前对象可以访问这个属性
# 动态绑定方法
stu1.eat()
stu2.eat()

# 动态绑定一个方法


def show():
    print("这是stu2绑定的方法")


stu2.show = show()
stu2.show()
