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
