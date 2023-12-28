# python的tcp和udp
# 服务端
import socket

# 建立TCP连接
sock = socket.socket()
# 绑定ip和端口
sock.bind("127.0.0.1", 9091)
# 最多5个人排队
sock.listen(5)
print("服务器运行再127.0.0.1:9091")

while True:
    print("等待客户端连接...")
    server, addr = sock.accept()
    print(addr, "客户端连接成功,等待接收消息...")
    data = server.recv(1024).decode("utf-8")
    print(addr, f":{data}")
    # 向服务端发送消息
    server.send(b"hello")
    # 关闭与客户端的连接
    server.close()
