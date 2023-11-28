# __new__和__init__的区别


class User:
    # 将类传入进来了
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    # init 传入的是对象
    def __init__(self, name):
        print("in init")
        self.name = name


# new 是用来控制对象的生成过程，在对象生成之前执行
# init 用来完成对象
# 如果new方法不返回对象，则不会调用init函数
if __name__ == "__main__":
    user = User()