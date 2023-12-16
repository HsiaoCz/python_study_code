# 进程池
# 当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，
# 但是如果要生成上百上千个目标，手动创建进程的工作量巨大，
# 此时就可以利用multiprocessing模块提供的Pool方法
# 初始化Pool时，可以指定一个最大进程数，当有新的请求提交到这个Pool时中，
# 如果这个进程数还没有满，那么就会创建一个新的进程去执行该请求；
# 如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
# 直到进程池中有进程结束，才会用到之前的进程来执行新的任务

from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s 开始执行,进程号为%d" % (msg, os.getpid))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕,耗时%0.2f" % (t_stop - t_start))


def main():
    # 定义一个进程池，最大进程数为3
    po = Pool(3)
    for i in range(10):
        po.apply_async(worker, (i,))
    print("------start------")
    po.close()
    po.join()
    print("------end------")


if __name__ == "__main__":
    main()
