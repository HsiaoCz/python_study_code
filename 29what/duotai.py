# 面向对象之多态
# 多态就是具有多种形态，它是指，即便不知道一个变量所引用的对象到底是什么类型
# 仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法

class Animal:
    def eat(self):
        print("eeee")


class Duck(Animal):
    def eat(slef):
        print("aaaa")


class Cat(Animal):
    def eat(self):
        print("ssss")


# 定义一个函数

def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Animal())
fun(Duck())
