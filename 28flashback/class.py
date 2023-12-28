# 动态绑定属性和方法
class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"吃饭")


stu1 = Student("张三", 20)
stu1.gender = "女"

print(stu1.name, stu1.age, stu1.gender)

# 动态绑定一个属性，但是只有当前对象可以访问这个属性


def show():
    print("这是stu1绑定的方法")


stu1.show = show()
stu1.show()
