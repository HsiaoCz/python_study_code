# property
# 动态属性
# 一个类里面的方法但凡被property标记
# 我们可以像使用类的属性一样去使用这个方法

from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
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
    user = User("hello", date(year=1987, month=12, day=22))
