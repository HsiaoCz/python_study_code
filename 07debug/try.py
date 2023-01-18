# 异常处理
# 使用try except
# try 内部是可能出现异常的代码
# except 出现异常之后执行的代码
try:
    n1 = int(input("请输入一个数字:\n"))
    n2 = int(input("请输入另一个数字:\n"))
    result = n1/n2
except ZeroDivisionError:
    print("被除数不能为0")
# 对所有可能出现的异常情况都捕获
# BaseExecption 起个别名 e
except BaseException as e:
    print(e)
else:
    print("结果是:", result)
finally:
    print("程序执行结束")

# 使用多个except来处理多个异常情况
# 使用else 没有出现错误时执行的语句
# finally 后面跟的语句 无论程序是否出错都会执行的代码
