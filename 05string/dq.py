# 字符串的对齐操作
s = "hello,python"
print(s.center(20, "*"))
print(s.ljust(20, "*"))
# 字符串内容对齐的操作方法
# center() 居中对齐，第一个参数指定宽度
# 第二个参数指定填充符，此参数可选，默认为空格
# 如果设置的宽度小于字符串宽度，返回原字符串
# ljust() 左对齐，第一个参数指定宽度，第二个参数指定填充符
# 第二份参数可选，默认空格，设置宽度小于字符原本宽度，返回原字符串
# rjust() 右对齐
# zfill() 右对齐，左边用零填充
