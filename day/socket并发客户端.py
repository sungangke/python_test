import socket

Ftpclinet=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Ftpclinet.connect(('127.0.0.1',8080))
while True:
    msg = input('>>: ').strip()
    Ftpclinet.send(msg.encode('utf-8'))
    data = Ftpclinet.recv(1024)
    print(data)
Ftpclinet.close()