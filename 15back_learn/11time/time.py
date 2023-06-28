# python的时间处理

import time

# 获取时间戳
# 1970.1.1 0：00：00到现在经历的秒数
print(time.time())

# 格式化时间字符串，主要用来展示时间
# p表示AM/PM 时分秒可以使用%X表示
time.strftime("%Y-%m-%d %H:%M:%S %p")

# 结构化时间
print(time.localtime())
print(time.gmtime())
