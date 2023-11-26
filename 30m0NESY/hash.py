import hashlib

m = hashlib.md5()  # 相当于建造一个工厂
m.update("hello".encode("utf-8"))  # 接收加密的数据

res = m.hexdigest()

print(res)

# md5 虽然不能反解，但是可以通过撞库进行比较
# 常用hash加盐的方式 增加撞库的成本
ms = hashlib.md5()
ms.update("天王".encode("utf-8"))
ms.update("hello".encode("utf-8"))
ms.update("盖地虎".encode("utf-8"))
ms.update("world".encode("utf-8"))
print(ms.hexdigest())
