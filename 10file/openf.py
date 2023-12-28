# 打开文件
file = open("./2344.txt", "r")
# 读取文件
# readlines()一行一行的读
print(file.readlines())
# 记得关闭文件
file.close()

# 以只写模式打开文件
file1 = open("./2345.txt", "w")
file1.write("Hello,World")
file1.close()
