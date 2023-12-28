# 序列化和反序列化
import json

res = json.dumps([1, 2, 3, 4, 5, True, False])
print("序列化的结果:", res)

# 反序列化
res1 = json.loads(res)
print("反序列化", res1.type(res1))

# 将文件中的数据反序列化
with open("json.txt", "r", encoding="utf-8") as f:
    json_res = f.read()
    res = json.loads(json_res)
    print(res)
