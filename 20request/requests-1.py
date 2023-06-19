# requests
# 换个教程，之前那个太垃圾了

import requests

# 常见的HTTP 请求 GET、POST、PUT、PATCH、DELETE
response = requests.get("https://httpbin.org/get")
print(response)

response = requests.post("https://httpbin.org/post")
print(response)

response = requests.put("https://httpbin.org/put")
print(response)

response = requests.patch("https://httpbin.org/patch")
print(response)

response = requests.delete("https://httpbin.org/delete")
print(response)

response = requests.options("https://httpbin.org/get")
print(response)

response = requests.head("https://httpbin.org/get")
print(response)

# 发送一个get请求
response = requests.get("https://httpbin.org/get")
# 查看响应的属性
print(dir(response))
# 查看响应的解释
print(help(response))
# 打印响应的URL
print(response.url)
# 获取响应状态码
print(response.status_code)
# 获取响应头
print(response.headers)
# 获取响应的content-type字段
print(response.headers.get("content-type"))
# 响应的json格式
print(response.json())
# 响应的主体
print(response.text)
# 获取相应的二进制
print(response.content)


# 自定义请求头
headers = {}
requests.get("https://httpbin.org/get", headers=headers)

# 传递参数
payload = {"page": 1, "limit": 20}
response = requests.get("https://httpbin.org/get", params=payload)
print(response.text)

# 请求的主体
payload = {"username": "curder", "password": "test"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# 请求的主体也可以使用json
payload = {"username": "curder", "password": "test"}
r = requests.post("https://httpbin.org/post", json=payload)
print(r.text)

# HTTP 身份验证
r = requests.get("https://httpbin.org/basic-auth/curder/test",
                 auth=("curder", "testx"))
print(r.ok)

# 请求超时时间
try:
    r = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.exceptions.ReadTimeout:
    print('read timeout')

# 响应状态码的获取
r = requests.get('https://httpbin.org/status/442')
print(r.status_code)

# 获取响应头
r = requests.get("https://httpbin.org/get")
print(r.headers.get("content-type"))

# 获取响应的cookies
r = requests.get("https://httpbin.org/cookies", cookies={'username': 'curder'})
print(r.text)

# 另一种方式获取cookies
jar = requests.cookies.RequestsCookieJar()
jar.set('test', 'value', domain="https://httpbin.org", path="/cookies")
jar.set('test1', 'value1', domain="https://httpbin.org", path="/cookies")
r = requests.get("https://httpbin.org/cookies", cookies=jar)

with requests.Session() as session:
    jar = session.cookies
    jar.set("test", "value", domain="httpbin.org", path="/cookies")
    jar.set("test2", "value1", domain="httpbin.org", path="/cookies")
    print(r.text)

# 重定向
# 通过在后面加allow_redirect可以控制是否重定向
r = requests.get('https://httpbin.org/reirect-to',
                 params={'url': 'https://www.baidu.com'})
print(r.url, r.status_code, r.history, sep="\n")

# 请求上下文
with requests.Session() as session:
    login_response = session.post("https://passport.17k.com/ck/user/login",
                                  data={"loginName", "1333333333", "password", "111111"})
    print(login_response)
    r = requests.get(
        "https://user.17k.com/ck/author/shelf?page1&appKey=2406394919")  # 需要登录的接口
print(r.text)
