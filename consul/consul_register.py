import requests

headers = {
    "contentType": "application/json"
}

# 这里的四个参数分别是:
# name 服务的名称 id 服务的id(服务的标识) address 服务的ip地址 port 服务暴露的端口
# url 这里要填的是consul 注册服务的Url地址 需要启动consul
# http://172.20.115.6:8500 consul启动的ip地址
# /v1/agent/service/register 注册的地址 v1需要注意 这个在consul的接口文档中没有 需要加上
# 将服务注册到注册中心 使用可以发送HTTP请求的就行 这里需要注意的是 注册的请求 得是PUT请求
# 这里headers用于指定请求的格式 使用json格式
# Tags 指定 服务的Tag

# 我们添加健康检查
# 添加check字段
# 设置Timeout和DeregisterCriticalServiceAfter
# 可以在检查没获取到的时候，过一分钟会删除掉服务


def register(name, id, address, port):
    url = "http://172.21.17.5:8500/v1/agent/service/register"
    rsp = requests.put(url, headers=headers, json={
        "Name": name,
        "ID": id,
        "Tags": ["hello", "hi"],
        "Address": address,
        "Port": port,
        "Check": {
            # consul 健康检查的地址
            "HTTP": f"http://{address}:{port}/health",
            # 超时时间设置
            "Timeout": "5s",
            # 5s检查一次
            "Interval": "5s",
            # 没检查到抹除掉
            "DeregisterCriticalServiceAfter": "15s"
        }
    })
    if rsp.status_code == 200:
        print("注册成功")
    else:
        print(f"注册失败:{rsp.status_code}")


# 之前这种注册 是个假的健康检查
# 如果需要真健康检查 需要设置一下
# 如何注销服务
# 注销和注册的url有点不一样
# 注销的是deregister 注册时register
# 另外注销url最后需要跟上 服务的id

def deregister(id):
    url = f"http://172.21.17.5:8500/v1/agent/service/deregister/{id}"
    rsp = requests.put(url, headers=headers)
    if rsp.status_code == 200:
        print("注销成功")
    else:
        print(f"注销失败:{rsp.status_code}")
if __name__ == "__main__":
    # 需要注意的是，在实现服务注册的时候，ip地址要是可用的
    # 怎么判断可用呢，ping以下ip地址就知道了
    register("hello", "hi", "172.21.17.5", 3002)

# 这里使用报错，不知道为啥
# 搞了半天，没写端口号，我去
