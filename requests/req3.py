# response header
import requests

# 这里的响应头部 类似于字典
# 可以使用键来获取头部的值
response = requests.get("https://www.bilibili.com")
print(response.headers)

# Content-Type
print(response.headers["Content-Type"])
# 不去分大小写
print(response.headers["content-type"])
