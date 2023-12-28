# 打开文件
file = open("./hello.txt", "r")

# 读取文件
# readlines()一行一行读取
print(file.readlines())

# 关闭文件
file.close()

# 以写模式打开文件
file1 = open("./hello.txt", "w")
file1.write("hi world")
file1.close()
