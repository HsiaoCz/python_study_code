# 查询字符串的方法
# index() 查找子串第一次出现的位置，如果子串不存在时，抛出valueError
# rindex() 查找子串最后一次出现的位置，如果子串不存在，则抛出valueError
# find() 查找子串第一次出现的位置，如果子串不存在，则返回-1
# rfind() 查找子串最后一次出现的位置，如果查找的子串不存在时，则返回-1
a = "Hello,hello"
# 查找第一次出现的位置
print(a.index("He"))
print(a.index("lo"))
print(a.find("e"))
# 查找最后出现的位置
print(a.rindex("lo"))
print(a.rfind("e"))
# 使用find() 来查找元素 建议
# 这种方式不会抛异常
