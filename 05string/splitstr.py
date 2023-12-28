# 字符串的分割
# split() 从字符串的左边开始分割，默认的分割符是空格
# 返回值是一个列表
# 可以指定分隔符和最大分割次数
# rsplit() 从字符串的右边开始分割
s = "Hello world python"
print(s.split())
s1 = "Hello|Hi|world"
print(s1.split(sep="|", maxsplit=1))
# rsplit() 从右边开始分割
print(s1.rsplit(sep="|", maxsplit=2))
