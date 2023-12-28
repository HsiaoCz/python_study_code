# python是一门动态语言
# 在创建对象后，可以动态的绑定属性和方法
# 一个Student类可以创建很多个实例，每个实例对象的属性值不同
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"在吃饭")


stu1 = Student("张三", 20)
stu2 = Student("李四", 20)
stu1.gender = "女"
print(stu1.name, stu1.age, stu1.gender)
# 动态的绑定一个属性，只有当前对象可以访问这个属性
# 动态的绑定方法
stu1.eat()
stu2.eat()

# stu1单独绑定一个show方法


def show():
    print("这是stu1绑定的方法")


stu1.show = show()
stu1.show()
