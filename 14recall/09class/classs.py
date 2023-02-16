# class
# 创建类


class student:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "在吃饭")

stu1 = student("zhangsan", 20)
# 动态绑定属性，意思是在声明之后添加的东西
stu1.gender = "女"
print(stu1.name, stu1.age, stu1.gender)
# 这就是动态绑定属性，还可以动态绑定属性
# 还可以动态绑定方法

