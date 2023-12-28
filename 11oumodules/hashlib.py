# hash是一类算法，通过接收传入的内容，经过运算后得到一串hash值，hash值有以下特点
# 1.只要传入的内容一样，得到的hash值必然一样
# 2.不能由hash值返解成内容
# 3.不管传入的内容有多大，只要使用hash算法不变，得到的hash值长度一定
import hashlib

m = hashlib.md5()  # 相当于建造了一个工厂，用来接收需要加密的数据
m.update('hello'.encode('utf-8'))  # 接收加密的数据
m.update('world'.encode('utf-8'))  # 可以多次接收加密的数据
res = m.hexdigest()  # 对需要加密的数据进行处理 得到加密的结果
print(res)

# md5 虽然不能反解，但是可以通过撞库进行比较
# 常用hash加盐的方式 增加撞库的成本
ms = hashlib.md5()
ms.update("天王".encode('utf-8'))
ms.update("hello".encode("utf-8"))
ms.update("盖地虎".encode("utf-8"))
ms.update("world".encode("utf-8"))
print(ms.hexdigest())
