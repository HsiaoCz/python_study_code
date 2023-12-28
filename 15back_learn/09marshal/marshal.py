# python的序列化与反序列化

import json

# 序列化
res = json.dumps([1, 2, 3, True, False])
print("序列化的结果:", res)

# 将序列化的结果存储到文件中
with open("./2344.txt", "w", encoding="utf-8") as fs:
    fs.write(res)

# 反序列化
res1 = json.loads(res)
print("反序列化:", res1)
