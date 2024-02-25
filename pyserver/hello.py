import socket

# socket.socket() 方法用来创建一个 socket 对象。
# 同时我们给它传递了两个参数：socket.AF_INET 表示使用IPv4 协议，
# socket.SOCK_STREAM 表示这是一个基于 TCP 的 socket 对象。
# 这两个参数也是默认参数，都可以不传。
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 允许端点复用
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# 绑定IP 和端口
sock.bind(("127.0.0.1", 8000))

# 开始监听
# 等待连接的最大请求数 5
sock.listen(5)

#  sock.accept() 会阻塞程序，等待客户端的连接，一旦有客户端连接上来，它会分别返回客户端连接对象和客户端的地址
client, addr = sock.accept()

data = b""

# 接收客户端请求数据需要调用客户端连接对象的 recv 方法，
# 参数为每一次接收的数据长度。socket 通讯过程中的数据都为 Python 的 bytes 类型。这里每次接收 1024 个字节，等待数据全部接收完成退出循环。
while True:
    chunk = client.recv(1024)
    data += chunk
    if len(chunk) < 1024:
        break

# 打印从客户端接收的数据
print(f"data: {data}")
# 给客户端发送响应数据
client.sendall(
    b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World</h1>"
)

# 关闭客户端连接对象
client.close()
# 关闭socket 对象
sock.close()
