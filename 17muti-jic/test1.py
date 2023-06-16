# 实现文件拷贝
import multiprocessing
import os


def copy_file(file_name, old_folder_name, new_folder_name):
    # 完成文件的负责
    # 打开要复制的这个文件夹中的文件，读取这里面的内容
    old_f = open("D:\\python项目\\" + old_folder_name + '/' + file_name, "rb")
    content = old_f.read()
    old_f.close()
    # 写入到我们新创建的文件夹下的文件中
    new_f = open(new_folder_name + '/' + file_name, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 获取用户要copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字：")
    # 创建一个新文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取这个文件夹下的所有文件名
    file_names = os.listdir("D:\\python项目" + '/' + old_folder_name)
    print(file_names)
    # 创建 5个进程池
    po = multiprocessing.Pool(5)
    # 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(
            file_name, old_folder_name, new_folder_name))
    # 关闭进程池
    po.close()
    po.join()


if __name__ == '__main__':
    main()
