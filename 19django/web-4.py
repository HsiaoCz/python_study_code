# 使用wsgi实现路由分发

from wsgiref.simple_server import make_server


def application(request, response):
    response('200 OK', [('Content-Type', 'text/html'), ])
    # 访问路径
    path = request["PATH_INFO"]
    if path == "/":
        res = '<h1>index</h1>'
    elif path == "/login":
        res = "<h1>login</h1>"
    else:
        res = "<h1>404</h1>"
    return [res.encode("utf-8")]


httpd = make_server("127.0.0.1", 9091, application)
httpd.serve_forever()
