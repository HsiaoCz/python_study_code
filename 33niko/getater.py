# __getattr__,__getattribute__
# __getattr__,就是在查找不到属性的时候调用

from datetime import date
from typing import Any


class User:
    def __init__(self, name, birthday, info={}) -> None:
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    # 无条件的进入这个函数，查找的时候
    # 把持所有访问的入口
    # 这个最好不要写
    def __getattribute__(self, __name: str) -> Any:
        pass


if __name__ == "__main__":
    user = User("hello", date(year=1982, month=12, day=21), info={"hihi": "lisi"})
    print(user.hihi)
