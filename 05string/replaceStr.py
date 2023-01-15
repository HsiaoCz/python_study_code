# 字符串的替换操作
# replace() 第一个参数指定要被替换的子串，第二个参数指定替换子串的字符串
# 方法返回替换后的字符串，替换前的字符串不发生变化，该方法可以通过第三个参数指定最大替换次数
# join() 将列表或元组中的字符串合并成一个字符串
s="Hello,python"
print(s.replace("python","java"))
ss="python,python,python"
print(ss.replace("python","java",1))
# join()用于列表或者元组
ls=["hello","java"]
print("".join(ls))
print("|".join(ls))

# 元组的连接
lss=("hello","python")
print("|".join(lss))