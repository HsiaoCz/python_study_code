# 属性描述符和属性查找过程
from datetime import datetime
import numbers

# 属性的查找过程

# 实现这三个方法就是一个属性描述符的对象
# 属性描述符控制属性


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Intergral):
            raise ValueError("int value need")
        self.value = value

    def __delete__(self, instance):
        pass


# 非数据属性描述符


class NonDataIntField:
    def __get__(self, instance, owner):
        return self.value


class Person:
    age = IntField()


class User:
    def __init__(self, name, birthday) -> None:
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self.age = value


if __name__ == "__main__":
    # user = User("hello", date(year=1987, month=12, day=22))
    person = Person()
    person.age = 30
    print(person.age)
