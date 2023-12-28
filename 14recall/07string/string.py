# 字符串是不可变序列
# 字符串的编解码
s = "天涯共此时"
print(s.encode(encoding="GBK"))
ty = s.encode(encoding="GBK")
print(ty.decode(encoding="GBK"))
# ord()获取字符串的原始值
# char()指定原始值 获取对应的字符
# 这里需要注意的是==比较的是值是否相等
# is比较的是内存地址是否相等
