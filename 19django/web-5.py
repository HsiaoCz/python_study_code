# 上面那一套拆分一下
# 尽量秉持一个函数做一件事
from wsgiref.simple_server import make_server


def index(request):
    return "<h1>index</h1>"


def login(request):
    return '<h1>login</h1>'


def sign(request):
    return '<h1>sign</h1>'


urlpatterns = [
    ('/', index),
    ('/login', login),
    ('/sign', sign),
]


# 入口函数
def application(request, response):
    response('200 OK', [('Content-Type', 'text/html'), ])
    # 访问的路径
    path = request['PATH_INFO']
    for route in urlpatterns:
        if path == route[0]:
            # 匹配上
            res = route[1](request)
            break
    else:
        res = '<h1>404</h1>'

    return [res.encode('utf8')]


# 启动服务器
httpd = make_server('127.0.0.1', 9000, application)
httpd.serve_forever()
