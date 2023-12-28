# 日志配置
# 日志文件
import os

BASE_DIR = "日志路径"
LOG_PATH = os.path.join(BASE_DIR, 'log')
LOG_UER_PATH = os.path.join(LOG_PATH, 'access.log')

# 定义三种日志输出格式
standard_format = '%(asctime)s - %(threadName)s:%(thread)d - 日志名字:%(name)s - %(filename)s:%(lineno)d -' \
                  '%(levelname)s - %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    # handlers是日志的接收者，不同的handler会将日志输出到不同的位置
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            # 'maxBytes': 1000,
            # 'backupCount': 5,
            # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'filename': LOG_UER_PATH,
            'encoding': 'utf-8',
            'formatter': 'standard',

        },
        # 打印到文件的日志,收集info及以上的日志
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'filename': LOG_UER_PATH,
            'encoding': 'utf-8',
            'formatter': 'test',

        },
    },

    # loggers是日志的产生者，产生的日志会传递给handler然后控制输出
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置，如果我们想要不同logger名的logger对象都共用一段配置，那么肯定不能在loggers子字典中定义n个key ，解决方式就是定义一个空的key,这样我们再取logger对象时logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，但是拿着该名字去loggers里找key名时却发现找不到，于是默认使用key=''的配置
        '': {
            # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'handlers': ['default', ],
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}
