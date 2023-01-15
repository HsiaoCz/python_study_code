# 字符串大小写转换的方法
s="hello"
a=s.upper()
print(a)
print(id(s))
print(id(a))
# 字符串是不可变序列 转换之后 产生了一个新的字符串对象
# 即使原来是大写的转换成大写 也会产生一个新的字符串对象
au="HELLO"
print(au.lower())
# swapcase() 讲所有小写转成大写 将大写字母转成小写
# capitalize() 把第一个字符转为大写，把其余字符转为小写
# title() 把每个单词的第一个字符转成大写，把每个单词的剩余字符转换成小写
