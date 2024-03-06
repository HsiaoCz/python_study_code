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

    def eat(self):
        super().eat()
        print("小猫爱吃鱼")


# 方法的重写 使用super().eat()
# 来继承父类的方法，然后重写此方法
# 不过这里还是会执行之前父类的方法

cat = Cat("大菊", 19)
cat.eat()
cat.say()
