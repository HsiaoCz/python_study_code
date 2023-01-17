# 方法的重写
class Animal:
    def __init__(self,name) -> None:
        self.name=name
    def eat(self):
        print("吃东西")

class Cat(Animal):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age
    def say(self):
        print("喵喵喵...")
    def eat(self):
        super().eat()
        print("小猫吃小鱼")

#方法重写 使用super().eat()
# 来继承父类的方法，然后可以重写此方法
# 不过这里还是会执行之前父类的方法
cat=Cat("大局",19)
cat.eat()
cat.say() 

        
