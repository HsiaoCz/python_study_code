# socket

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("127.0.0.1", 8081)
server.listen()
sock, addr = server.accept()


# 获取从客户端发送的数据
# 一次获取1k的数据
data = server.recv(1024)
print(data.decode("utf8"))

sock.send("hi".encode("utf8"))
server.close()
sock.close()
