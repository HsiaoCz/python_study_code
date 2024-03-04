# 查询字符串参数
# 自定义GET请求的一种常用方法是通过URL中的查询字符串参数传递值
# 使用get执行这个操作 需要将数据传递给params

import requests

response = requests.get(
    "https://www.baidu.com", params={"q", "requests+;anguage:python"}
)

json_response = response.json()
repository = json_response["item"][0]

print(f"Repository name:{repository['name']}")
print(f'Repository description: {repository["description"]}')

# 通过将字典 {'q'：'requests + language：python'}
# 传递给 .get() 的 params 参数，你可以修改从Search API返回的结果
# 还可以像刚才那样以字典的形式或以元组列表形式将 params 传递给 get():
# requests.get(
#     'https://api.github.com/search/repositories',
#      params=[('q', 'requests+language:python')],
# )

# 还可以传 bytes 作为值
# requests.get(
#  'https://api.github.com/search/repositories',
#  params=b'q=requests+language:python',
# )
