# with 上下文管理器
# 将文件自动释放
# 实现了__enter__(),__exit__()方法
# 就是遵守了上下文协议，该类的实例对象就是上下文管理器
with open("hello.txt", "w") as file_w:
    file_w.writelines("hello World")

# 将encoding=utf-8
# 这行写在第一行可以告诉解析器，该文件的编码格式是utf-8
# 避免中文乱码
