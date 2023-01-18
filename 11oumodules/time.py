# time/datetime时间处理模块
import time
# 获取时间戳，表示从1970.1.1 0:00:00到现在经过的秒数，属于浮点类型
print(time.time())

# 格式化时间字符串，主要用来展示时间
# p表示 AM/PM 时分秒可以使用%X表示
time.strftime("%Y-%m-%d %H:%M:%S %p")

# 结构化时间
print(time.localtime())  # 获取本地时区的struct_time
print(time.gmtime())   # 获取UTC时区的结构化时间

# 上述的三种时间格式，计算机只能识别时间戳，而人类能看懂的时间是格式化的时间字符串或者结构化时间
# 因此三者有转化关系
# 1、时间戳-->结构化时间内-->格式化时间
time1 = time.time()  # 获取时间戳
res = time.localtime(time1)  # 将时间戳转为结构化时间
print(res)

# 结构化时间---格式化时间
res = time.localtime()  # 获取结构化时间
time1 = time.strftime("%Y-%m-%d %X", res)
print(time1)

# 2、格式化时间--->结构化时间---->时间戳
# 格式化时间---结构化时间
res = time.strftime('%Y-%m-%d %X', res)  # 获取格式化时间
print(res)

time1 = time.strptime(res, '%Y-%m-%d %X')  # 格式化时间转成结构化时间
print(time1)

# 结构化时间转成时间戳
res = time.localtime()  # 获取结构化时间
time1 = time.mktime(res)
print(time1)
