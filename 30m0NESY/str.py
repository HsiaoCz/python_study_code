# 字符串大小写转换的方法
s = "hello"
a = s.upper()

print(a)
print(id(s))
print(id(a))
# 字符串是不可变序列 转换之后 产生了一个新的字符串对象
# 即使原来是大写的转换成大写 也会产生一个新的字符串对象
au = "HELLO"
print(au.lower())
# swapcase() 讲所有小写转成大写 将大写字母转成小写
# capitalize() 把第一个字符转为大写，把其余字符转为小写
# title() 把每个单词的第一个字符转成大写，把每个单词的剩余字符转换成小写

# 不同的变量指向相同的字符串 指向的是相同内存地址相同
# 所谓驻留机制 是对相同的字符串只保留一个
# 不同的字符串被放在字符串的驻留池中
# 驻留机制的几种情况
# 1.字符串的长度为0或者1时
# 2.符合标识符的字符串
# 3.字符串只在编译时进行驻留，而非运行时
# 4.[-5,256]之间的整数数字
# sys中的intern方法强制两个字符串指向同i个对象

aa = "abc"
bb = "ab" + "c"
print(aa is bb)
cc = "".join(["ab", "c"])
print(aa is cc)

# 这时候就不是了 因为+操作 在运行之前已经连接完成了
# 但是join操作在运行时才进行连接操作
# 字符串驻留机制可以提高效率
# 字符串拼接 建议使用join方法

# 字符串的分割操作
# split() 从字符串的左边开始分割，默认的分割符是空格
# 返回值是一个列表
# 可以指定分割符和最大分割次数
# rsplit() 从字符串右边开始分割

sa = "Hello world python"
print(sa.split())
s1 = "Hello|Hi|world"
print(s1.split(sep="|", maxsplit=1))
# rsplit() 从右边开始分割
print(s1.rsplit(sep="|", maxsplit=2))

# 字符串的切片操作
# 字符串本身是不可变类型，不能增删改操作
# 切片将产生新的对象
s = "Hello"

# 步长 两个元素之间的索引间隔为2
print(s[::2])
# 步长为负，索引从后往前
print(s[::-1])
# 格式化字符串
# 格式化字符串的两种方式
# 1.使用%作为占位符
# 2.使用{}作为占位符
name = "张三"
print("hello:%s" % name)
age = 12
print("hello:%s,%d" % (name, age))

# 使用{}进行占位
print("hello:{0},{1}".format(name, age))

# 使用f进行格式化
print(f"Hello{name},{age}")

# 表示精度和宽度的格式化字符串
print("%d" % 99)
# %10d表示宽度
print("%10d", 99)
print("%.3f", 3.121314)
# 还可以同时表示宽度和精度

# 字符串替换
# replace() 第一个参数指定要被替换的子串，第二个参数指定替换子串的字符串
# 方法返回替换后的字符串，替换前的字符串不发生变化，该方法可以通过第三个参数指定最大替换次数
# join() 将列表或元组中的字符串合并成一个字符串
s = "Hello,python"
print(s.replace("python", "java"))
ss = "python,python,python"
print(ss.replace("python", "java", 1))
# join()用于列表或者元组
ls = ["hello", "java"]
print("".join(ls))
print("|".join(ls))

# 元组的连接
lss = ("hello", "python")
print("|".join(lss))

# 字符串查找
# index() 查找子串第一次出现的位置，如果子串不存在时，抛出valueError
# rindex() 查找子串最后一次出现的位置，如果子串不存在，则抛出valueError
# find() 查找子串第一次出现的位置，如果子串不存在，则返回-1
# rfind() 查找子串最后一次出现的位置，如果查找的子串不存在时，则返回-1

kk = "Hello,hello"
print(kk.index("He"))
print(kk.index("lo"))

# 字符串内容对齐的操作方法
# center() 居中对齐，第一个参数指定宽度
# 第二个参数指定填充符，此参数可选，默认为空格
# 如果设置的宽度小于字符串宽度，返回原字符串
# ljust() 左对齐，第一个参数指定宽度，第二个参数指定填充符
# 第二份参数可选，默认空格，设置宽度小于字符原本宽度，返回原字符串
# rjust() 右对齐
# zfill() 右对齐，左边用零填充

# == 和 is
# == 比较的是value是否相等
# is 比较的是内存地址是否一致

# 编码和解码
# 编码：将字符串转换为二进制数据(bytes)
# 解码：将bytes类型的数据转换成字符串类型
s = "天涯共此时"
print(s.encode(encoding="GBK"))
print(s.encode(encoding="UTF-8"))
# 不同的编码格式占用的字节数是不同的

# 解码
byte = s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))
# 编码和解码的格式需要相同
