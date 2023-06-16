# 实现进度条的效果
import multiprocessing
import os


def copy_file(q, file_name, old_folder_name, new_folder_name):
    # 完成文件的负责
    # 打开要复制的这个文件夹中的文件，读取这里面的内容
    old_f = open("D:\\python项目\\" + old_folder_name + '/' + file_name, "rb")
    content = old_f.read()
    old_f.close()
    # 写入到我们新创建的文件夹下的文件中
    new_f = open(new_folder_name + '/' + file_name, "wb")
    new_f.write(content)
    new_f.close()
    # 如果文件拷贝完成，就向队列里面写一个消息
    q.put(file_name)


def main():
    # 获取用户要copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字:")
    # 创建一个新文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取这个文件夹下的所有文件名
    file_names = os.listdir("D:\\python项目" + '/' + old_folder_name)
    # print(file_names)
    # 创建一个队列
    q = multiprocessing.Manager().Queue()
    # 创建 5个进程池
    po = multiprocessing.Pool(5)
    # 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(
            q, file_name, old_folder_name, new_folder_name))
    # 关闭进程池
    po.close()
    # po.join()
    # 测一下文件的个数
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print(f'----已经完成copy：{file_name} ----')
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num*100/all_file_num), end='')
        if copy_ok_num >= all_file_num:
            break


if __name__ == '__main__':
    main()
