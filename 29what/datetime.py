import datetime

print(datetime.datetime.now()) # 输出格式化时间
print(datetime.datetime.now()+datetime.timedelta(3))  # 当前时间加3天
print(datetime.datetime.now()+datetime.timedelta(-3))  # 当前时间减三天
print(datetime.datetime.now()+datetime.timedelta(hours=3))  # 当前时间加3个小时
print(datetime.datetime.now()+datetime.timedelta(minutes=30))  # 当前时间加30分钟

