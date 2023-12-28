# 元类编程
# 类也是对象
# 什么是元类，元类是创建类的类

# python的类实例化过程，会首先去寻找metaclass，通过metaclass去创建类
# type去创建类对象，实例化

def create_class(name):
    if name == "user":
        class User:
            def __str__(self) -> str:
                return "user"
        return User

    elif name == "copo":
        class Copo:
            def __str__(self) -> str:
                return "copo"
        return Copo


# type获取对象类型的
# 动态创建类
User = type("User", {}, {})


def say(self):
    return "say hello"


class BaseClass():
    def anwser(self):
        return "baseclass"


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        pass


class Hello(metaclass=MetaClass):
    pass


if __name__ == "__main__":
    mycls = create_class("user")
    mycop = mycls()
    User = type("User", (object,), {"name": "user", "say": say})
    he = User()
    print(he.say())
