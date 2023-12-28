# 类的深浅拷贝问题
# 变量的赋值操作，只是形成两个变量，实际上还是指向同一个对象
# 浅拷贝，python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝
# 因此，源对象与拷贝对象会引用同一个子对象
# 深拷贝 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk) -> None:
        self.cpu=cpu
        self.disk=disk

# 变量的赋值操作
cpu1=CPU
cpu2=cpu1
print(id(cpu1))
print(id(cpu2))
# cpu1和cpu2的内存地址是一样的
# 实际上一个对象放到了两个对象中

# 类的浅拷贝
disk=Disk()
computer=Computer(cpu1,disk)

# 浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

# 深拷贝
# 源对象的子对象都会拷贝一份
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)

