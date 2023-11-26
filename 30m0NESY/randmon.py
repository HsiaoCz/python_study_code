# 随机数
import random

#  随机获取0-1之间的浮点数
print(random.random())

# 获取随机大于等于1，小于等于6之间的整型数字
print(random.randint(1, 6))

# 随机获取大于等于1 小于等于6之间的整型数字
print(random.randrange(1, 6))

# 获得随机参数中的一个数据
print(random.choice([111, 222, 333, 444, 555, 666]))

# 指定元素个数自由组合，随机输出，当指定元素个数为1时，与choice作用相同
print(random.sample([111, 222, 333, 444, 555, 666], 1))
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8], 3))

# 打乱原列表的顺序
list1 = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list1)

# 使用random生成随机验证码


def func(n=6):
    # 获取随机的26个大写英文字母,根据ASC码表
    al_A = chr(random.randint(65, 90))
    # 获取随机的26个小写英文字母，根据ASC码表
    al_a = chr(random.randint(97, 122))
    # 获取随机数字
    num = random.randint(0.9)
    # 生成随机验证码
    res = ""
    for i in range(n):
        res += random.choice([al_a, al_A, str(num)])
    return res
