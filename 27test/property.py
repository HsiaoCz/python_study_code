# 属性描述符

import datetime


class User:
    def __init__(self, name, birthday) -> None:
        self.name = name
        self.birthday = birthday
        self.__age = 0

    def get_age(self):
        return datetime.now().year-self.birthday.year

    @property
    def age(self):
        return datetime.now().year-self.birthday.year

    @age.setter
    def age(self, value):
        self.age = value
