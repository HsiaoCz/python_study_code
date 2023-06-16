# python tcp客户端

import socket

# 选择协议
sock = socket.socket()
# 建立协议
sock.connect(("127.0.0.1", 9091))
# 发送消息
sock.send(b"hello")
# 接收消息
print(sock.recv(1024))
# 关闭连接
sock.close()
