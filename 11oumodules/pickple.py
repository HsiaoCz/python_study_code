# pickple的用法和json模块相同，不同点在于它只能用于python
# 可以序列化python独有的数据类型
import pickle

# 序列化
res = pickle.dumps({1, 2, 3})
# 序列化 集合
print(res)

# 反序列化
res1 = pickle.loads(res)
print(res1)
