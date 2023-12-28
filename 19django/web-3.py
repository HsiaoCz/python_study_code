# wsgiref简单使用
# wsgi将繁杂的数据处理部分抽离出来，使得开发者可以专注于逻辑的处理
from wsgiref.simple_server import make_server

# 入口函数


def application(request, response):
    response("200 OK", [{"Content-Type", "text/html"}])
    # 访问路径
    path = request["PATH_INFO"]
    print(path)

    return [b"<h1>hello world</h1>"]


# 启动服务器
httpd = make_server("127.0.0.1", 9091, application)
httpd.serve_forever()
