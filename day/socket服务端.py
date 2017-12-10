import socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
while True:
    conn, addr = phone.accept()
    while True:
        try:
            data = conn.recv(2049)#如果是Linux上，客户端上断开后，这里不会报错会一直收空，然后继续收空进入到死循环了。但是我们可以在下面判断下data是否为空,if not data:break
            print(data)
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()
phone.close()