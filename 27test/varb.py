# python中的变量
# python中的变量本质上是一个指针

a = 1
print(a)

# 这里会先去内存申请一块内存空间
# 保存1这个对象
# 然后将a贴到1这个对象上

# is 和 ==的区别
# is 比较的式两个对象的id是否相同
# ==判断值是否相等


# del和垃圾回收
# python中的垃圾回收，采用引用计数
# 所谓的引用计数
# 比如定义一个a=1,b=a,那么1上的引用计数为2，也就是有两个变量指向它
# 当某个对象的引用计数为零就会回收掉，释放内存
# 使用del会使引用计数-1