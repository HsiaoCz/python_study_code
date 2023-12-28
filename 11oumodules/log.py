# logging 模块可以用来记录程序运行的日志
import logging

# 数字大小代表不同的等级
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

logging.debug("调试debug")
logging.info("消息info")
logging.warning("警告warn")
logging.error("错误error")
logging.critical("严重critical")

logging.basicConfig(filename='test.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

# 上述参数及其他未用到的参数介绍如下：
# filename：用指定的文件名创建FiledHandler，用来打印到文件中
# datefmt：指定日期时间格式。
# level：根据数字设置的日志级别

# format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

# logging 模块在使用过程中，需要用到formatter,Handler,Logger,Filter对象
# Logger：产生日志对象
# filter: 过滤日志对象，不常用
# Handler:接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端
# Formatter 对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式
