# 序列化与反序列化
# json模块和pickle模块是用来序列化和反序列化数据的模块
# 将内存中的数据序列化成一种特定的内容，该格式用于传输给其他平台
# 反序列化 将一种特点的格式转换成python能够认识的数据格式

import json

# 序列化操作
res = json.dumps([1, 2, 3, 4, 5, True, False])
print("序列化的结果:", res)

# 序列化得到的结果可以存储在文件中
with open("json.txt", "w", encoding="utf-8") as fs:
    fs.write(res)

# 反序列化
res1 = json.loads(res)
print("反序列化", res1.type(res1))

# 将文件中的数据反序列化
with open("json.txt", "r", encoding="utf-8") as f:
    json_res = f.read()
    res = json.loads(json_res)
    print(res)
