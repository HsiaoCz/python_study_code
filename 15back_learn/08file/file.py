# encoding=utf-8
# 将这个写在第一行可以告诉编辑器，该文件的格式
# 避免乱码

print("hello China")

file = open("./2344.txt", "r")

# 读取文件
print(file.readlines())

file.close()

file1 = open("./2344.txt", "w")
file1.write("xiao fan yi")
file1.close()

# 文件打开记得关闭

# os 模块可以操作系统
# os.system
# os.startfile()

# with上下文管理器
with open("./2344.txt", "r") as file3:
    print(file3.readlines())

# 实现了__enter__()和__exit__()方法的
# 这个类就实现了上下文协议，可以成为一个上下文管理器
