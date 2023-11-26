# 序列化和反序列化
import json

res = json.dumps([1, 2, 3, 4, 5, 6, 7])
print("序列化的结果:", res)

# 序列化得到的结果可以存储在文件中
with open("json.txt", "w", encoding="utf-8") as fs:
    fs.write(res)

# 反序列化
res1 = json.loads(res)
print("反序列化", res1.type(res1))

with open("json.txt", "r", encoding="utf-8") as f:
    json_res = f.read()
    res = json.loads(json_res)
    print(res)
