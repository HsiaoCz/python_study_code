# 线程间通信
import time


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

# 线程通信的方式1：共享变量
# 通过global 全局变量通信
# 共享变量表示线程安全的

# 通过queue的方式进行线程间同步
# 通过消息队列来实现通信
# queue是线程安全的
