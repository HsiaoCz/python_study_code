# with 上下文管理器，自动关闭文件
# open()这个对象的实例对象就是上下文管理器
# 上下文管理器 离开上下文管理器 也能保证__exit__方法被执行
with open("2344.txt", "r") as file:
    print(file.readlines())

# 自动将文件释放，优点类似于go的defer
# with 之后 as 语句之前的 被称为上下文表达式
# 结果是一个上下文管理器


class MyContentMgr(object):
    def __enter__(self):
        print("enter 方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ 被执行了")

    def show(self):
        print("show 方法被执行了")

# MyContentMgr实现了特殊方法__enter__(),__exit__()
# 称为该类对象遵守了上下文管理协议，该类的实例对象就是上下文管理器


with open("log.txt", "w") as file_w:
    file_w.writelines("Hello World")
