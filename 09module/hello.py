# 在这个模块中引入main
from calc import add
import calc

print(calc.add(100, 200))
# 这时候打印输出 会输出30，将calc这个模块的输出内容也输出了
# 如果不想输出，有这样两种办法
# 1.只引入add()函数
print(add(100, 200))
# 还有一种办法，修改calc的代码
# 加上__name__=__main__
