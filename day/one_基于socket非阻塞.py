import socket
import time
client = socket.socket()
client.setblocking(False)#非阻塞，连接不成功就直接往下走了
try:
    client.connect(("60.9.1.128",80))#阻塞
except BlockingIOError as e:
    print(e)
time.sleep(5)
print('11111111111')
data = b"GET / HTTP/1.1\r\nhost: dig.chouti.com\r\n\r\n"
client.sendall(data)

time.sleep(5)
response = client.recv(8090)#阻塞
print(response)
client.close()