# python 迭代器
# 可迭代对象：在python中凡是可以跟在for循环后面的，都是可迭代对象
# 常见的可迭代对象
# 字符串，列表，元组，字典，集合
# 可迭代对象的接口 __iter__,对应的调用方法就是内置函数iter()
# 使用iter()函数最后会生成可迭代对象
# 迭代器有两个接口:__iter__和__next__

# 迭代的三个关键步骤：
# 1、调用iter(iterable)来构建迭代器
# 2、调用next(iterator)来获取值
# 最后捕获StopIteration异常来判断迭代结束

# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标访问的方式不一样，迭代器是不能返回的
# 迭代器提供了一种惰性访问数据的方式
# 以下标访问 本质上是__getitem__

# 所有的迭代器本身都要求时可迭代的
# 也就是说，迭代器也是可迭代对象

# 可迭代对象iterable 只要实现了__iter__就是可迭代对象
# iterator 迭代器继承自Iterable
# 迭代器需要实现__next__() 获取下一个元素
# __iter__(self) 用来返回可迭代对象
# 真正拿到迭代器 使用的是__next__()

from typing import Iterator


class MyIterator(Iterator):
    def __init__(self, employee) -> None:
        super().__init__()
        self.iter_list = employee
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
