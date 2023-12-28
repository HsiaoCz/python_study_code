# 使用queue来实现进程间通信
# 两个进程之前不共享全局变量，那么要如何实现进程之间的通信
# 使用socket进行收发
# 使用文件读取
# queue

import multiprocessing


def download_data(q):
    # 在进程1中创建的数据
    data = [1, 2, 3, 4]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("---数据写入完成----")


def analysts_data(q):
    data_list = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        data_list.append(data)
        # 判断数据是否取完
        if q.empty():
            break
    print(data_list)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建多个线程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p2 = multiprocessing.Process(target=analysts_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()

# 队列是一个先进先出，后进后出的一个数据结构
# queue中有一些方法，知道怎么用就行
# q = multiprocessing.Queue(3) # 初始化一个Queue对象，最多可接收3个数据
# q.put("msg_01")
# q.put("mag_02") # 在q队列中写入数据
# print(q.full()) #False 判断q队列中是否满了
# q.put("msg_03")
# print(q.full()) #True
# q.get()  # msg_01
# q.get()  # msg_02
# q.get()  # msg_03
# q.empty() # true 判断队列是否为空
