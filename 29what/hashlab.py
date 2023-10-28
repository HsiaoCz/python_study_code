import hashlib

m = hashlib.md5()  # 相当于建造的一个工厂
m.update('hello'.encode('utf-8'))  # 接收加密的数据
m.update('world'.encode('utf-8'))
res = m.hexdigest()  # 对需要加密的数据进行处理，得到加密之后的结果
print(res)


