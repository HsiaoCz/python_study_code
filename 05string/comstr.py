# 字符串的比较操作
# 运算符 >,>=,<,<=
# 比较规则，首先比较两个字符串的第一个字符，如果相等则继续比较第二个字符
# 依次比较下去，直到两个字符串中的字符不相等时，比较结果就是两个字符串的比较结果
# 字符串后面的字符将不再比较
# 比较的原理：两个字符进行比较时，比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定的字符原始值
# 调用char()指定原始值 可以获得对应的字符
print("apple" > "app")
print("apple" > "banana")
print(ord("a"))
print(ord("b"))
print(chr(98))
print(chr(97))
print(chr(ord("夸")))
# == 和 is
# == 比较的是value是否相等
# is 比较的是内存地址是否一致
