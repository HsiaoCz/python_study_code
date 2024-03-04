# response content

import requests

# GET请求的响应通常再消息体中具有一些有价值的信息，称为有效负载
# 使用Response的属性和方法，可以以各种不同格式查看有效负载

# 要以自己格式查看响应的内容，可以使用.content

response = requests.get("https://www.bilibili.com")
print(response.content)

# 虽然.content允许访问响应有效负载的原始字节，但是通常使用UTF-8等字符编码
# 转换为字符串
# 当访问.text时，response将为你执行此操作

print(response.text)

# 对bytes解码到str需要一个编码格式 所以如果没有指定

response.encoding = "utf-8"
print(response.text)

# 这里输出的时序列化的JSON内容
# 要获取字典内容 可以使用.text获取str并使用json.loads()对其进行反序列化
# 不过完成这个任务有更简单的
print(response.json)

# .json 返回的是字典类型 因此可以使用键值对的方式访问对象的值
