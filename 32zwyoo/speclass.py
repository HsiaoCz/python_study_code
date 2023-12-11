# 特殊的方法
# __len__()
a = 20
b = 100
c = a+b
print(c)
d = a.__add__(b)
print(d)


class Student:
    def __init__(self, name) -> None:
        self.name = name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("张三")
stu2 = Student("李四")
s = stu1+stu2  # 重写__add__使得对象获得+操作
print(s)
s = stu1.__add__(stu2)
print(s)

# len()计算列表的长度
list = [1, 2, 3, 4, 5]
print(len(list))
print(list.__len__())
print(stu1.__len__())


class Persion(object):
    def __init__(self, name, age) -> None:
        self.mname = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__被调用执行了,cls的id值为{0".format(id(cls)))
        obj = super().__new__(cls)
        print("创建的对象的id:{0}".format(id(obj)))
        return obj


print("object这个类对象p的id:{0}".format(id(object)))
print("Persion这个类对象的id:{0}".format(id(Persion)))
# 创建类的实例对象
p = Persion("张三", 12)
print("Person创建的对象p的id:{0}".format(id(p)))
