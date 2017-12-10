#IO 多路复用：是用来检测多个socket（IO）对象是否有变化

import socket
import time
client = socket.socket()
client.setblocking(False)#非阻塞，连接不成功就直接往下走了
try:
    client.connect(("60.9.1.128",80))#阻塞
except BlockingIOError as e:
    print(e)
# r,w,e = select.select([sk1,sk2,sk3.....,100],[sk1,sk2,sk3.....,100],[],0.05)
# while True:
#     #w,是谁？【sk2，sk3}连接成功了就是谁
#     for obj in w:
#         obj.send("GET /http/1.0")
#
#     #r,是什么？[sk2,sk3],要收数据
#     for obj in r:
#         res = obj.recv()
#         print(res)