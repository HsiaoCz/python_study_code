# slice 将序列截取下来一部分
from list import lss

a = "Hello"
s = a[1:3]

# 步长 隔多少截取
m = a[0:4:2]
print(m)
print(a[1:-1])

# 截取到-1就是截取到倒数第一个，不包含倒数第一个
# 当步长为-1的时候，从左往右获取元素，所以[::-1]的结果是原始序列的倒置
# 切片的结果是列表的拷贝

sliceLss = lss[0:2]
print(sliceLss)

lstt = [2, 3, 4, 5, 6, 7, 8, 9, 12, 13]
print(lstt)
print(id(lstt))
lsttSlice = lstt[1:6:1]
print(lsttSlice)
print(id(lsttSlice))
lsll = lstt[2:7:2]
print(lsll)
print(id(lsll))
# 步长为负数的情况 切片第一个元素是列表的最后一个元素
lslll = lstt[6:0:-1]
# 使用切片对列表进行追加
lstt[4:] = lss
# 意思是切掉的部分用一个新的列表去替换
