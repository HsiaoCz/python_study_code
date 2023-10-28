# json格式数据的序列化和反序列化
import json

# 序列化操作
res = json.dumps([1, 2, 3, 4, 5, True, False])
print("序列化的结果:", res)

# 序列化得到的结果可以存储在文件中

# 反序列化
res1 = json.loads(res)
print("反序列化:", res1)
