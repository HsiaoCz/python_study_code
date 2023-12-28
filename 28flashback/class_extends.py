# 继承
# class 子类类名(父类1，父类2):
# 如果一个类没有继承任何类，则默认继承object
# python 支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造方法
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print("吃东西")


class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    def say(self):
        print("喵喵喵...")


# 使用super().__init__(name)调用父类的属性
cat = Cat("大菊", 18)
cat.eat()
cat.say()

# python支持多继承，也就是类名后面可以写多个类名
# 一个类继承自多个类

