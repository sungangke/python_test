import socket
client = socket.socket()
client.connect(("60.9.1.128",80))#阻塞

data = b"GET / HTTP/1.1\r\nhost: dig.chouti.com\r\n\r\n"
client.sendall(data)

response = client.recv(8090)#阻塞
print(response)
client.close()