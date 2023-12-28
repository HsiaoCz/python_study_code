# python的迭代协议
# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标访问的方式不一样，迭代器是不能返回的
# 迭代器提供了一种惰性访问数据的方式
# 以下标访问 本质上是__getitem__

# 迭代协议
# __iter__

# 可迭代对象iterable 只要实现了__iter__就是可迭代对象
# iterator 迭代器继承自Iterable
# 迭代器需要实现__next__() 获取下一个元素
# __iter__(self) 用来返回可迭代对象
# 真正拿到迭代器 使用的是__next__()

# 迭代器和可迭代对象的区别

from typing import Iterator


class MyIterator(Iterator):
    def __init__(self, employee_list) -> None:
        super().__init__()
        self.iter_list = employee_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 真正返回迭代值是在这里面
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
