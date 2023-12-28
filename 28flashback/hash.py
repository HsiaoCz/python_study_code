# hash 是一类算法，通过接收传入的内容，经过运算得到一串hash值
# 传入相同的内容，hash值相同
# hash值不能反解成内容
# hash算法不变，hash值长度不变

import hashlib

m = hashlib.md5()
m.update('hello'.encode('utf-8'))
res = m.hexdigest()
print(res)

ms = hashlib.md5()
ms.update("天王".encode('utf-8'))
ms.update("hello".encode("utf-8"))
ms.update("盖地虎".encode("utf-8"))
ms.update("world".encode("utf-8"))
print(ms.hexdigest())

