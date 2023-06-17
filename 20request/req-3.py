# 响应头部
import requests

# 这里返回的响应头部，类似于字典
# 可以使用键来获取头部的值
response = requests.get("https://api.github.com")
print(response.headers)

# 查看响应有效负载的类型
print(response.headers["Content-Type"])
# 这里是不区分大小写的
print(response.headers["content-type"])
