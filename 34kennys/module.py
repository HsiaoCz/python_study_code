# 模块有三种导入方式
# 1、import <模块名>

from varb import c as mss
from varb import b
import varb

print(varb.x)
# 这种导入方式会导入模块varb的所有代码元素
# 使用某个元素的时候需要在前面加上模块名称

# 2、form <模块名> import <代码元素>

print(b)
# 使用这种方式在访问模块varb 的代码元素时不需要加模块名

# 3、 form <模块名> import <代码元素> as <给代码元素起个别名>

print(mss)
# 使用这种导入主要是导入的模块和当前模块代码元素名称冲突 起个别名避免冲突
