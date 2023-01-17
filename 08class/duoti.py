# 面向对象之多态
# 多态就是具有多种形态，它是指，即便不知道一个变量所引用的对象到底是什么类型
# 仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
class Animal:
    def eat(self):
        print("动物会吃")

class Dog(Animal):
    def eat(self):
        print("狗吃骨头")

class Cat(Animal):
    def eat(self):
        print("猫吃小鱼")
        
# 定义一个函数
def fun(obj):
    obj.eat()
    
# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
# 多态 在go语言里 使用interface来实现
# 鸭子类型
class Persion:
    def eat(self):
        print("人吃牛排")

fun(Persion())
