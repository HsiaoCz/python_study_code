# socket client

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9091))
client.send("hello".encode("utf8"))

data = client.recv(1024)

print(data.decode("utf8"))
client.close()
