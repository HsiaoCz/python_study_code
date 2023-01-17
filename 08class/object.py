# object类是所有类的父类，因此所有类都有object类的属性和方法
# 内置函数dir()可以查看指定对象所有属性
# Object有一个__str__()方法，用于返回一个对于对象的描述
# __str__()函数经常用于print()方法，帮助我们查看对象的信息
# 所有经常重写此方法
class Student:
     def __init__(self,name,age) -> None:
          self.name=name
          self.age=age
     def __str__(self):
         return "我叫{0},今年{1}".format(self.name,self.age)
stu=Student
print(dir(stu))
# print(stu.__str__())
