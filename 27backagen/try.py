# try except
# try 内部是可能出现异常的代码
# except 出现异常之后的代码
try:
    n1 = int(input("请输入一个数字:\n"))
    n2 = int(input("请输入另一个数字:\n"))
    result = n1/n2
except ZeroDivisionError:
    print("除数不能为零")
# BaseExeception
except BaseException as e:
    print(e)
else:
    print("结果是:", result)
finally:
    print("程序执行结束")
