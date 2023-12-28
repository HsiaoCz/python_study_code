# datetime模块可以用来加减时间
import datetime

print(datetime.datetime.now())  # 格式化输出时间
print(datetime.datetime.now()+datetime.timedelta(3))  # 当前时间加3天
print(datetime.datetime.now()+datetime.timedelta(-3))  # 当前时间减三天
print(datetime.datetime.now()+datetime.timedelta(hours=3))  # 当前时间加3个小时
print(datetime.datetime.now()+datetime.timedelta(minutes=30))  # 当前时间加30分钟
