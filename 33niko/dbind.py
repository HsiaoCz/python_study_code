# python dynamic binding
class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "在吃饭")


stu1 = Stu("张三", 20)
stu2 = Stu("李四", 20)
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


# 类的深拷贝和浅拷贝的问题
# 变量的赋值操作，只是形成两个变量，实际上还是指向同一个对象
# 浅拷贝，python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝
# 因此，源对象与拷贝对象会引用同一个子对象
# 深拷贝 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk) -> None:
        self.cpu = cpu
        self.disk = disk


# 变量的赋值操作
cpu1 = CPU
cpu2 = cpu1
print(id(cpu1))
print(id(cpu2))
# cpu1和cpu2的内存地址是一样的
# 实际上一个对象放到了两个对象中

# 类的浅拷贝
disk = Disk()
computer = Computer(cpu1, disk)

# 浅拷贝
import copy

computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# 深拷贝
# 源对象的子对象都会拷贝一份
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)

# from dbind import Student
