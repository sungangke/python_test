import socket
ssh_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssh_client.connect(('127.0.0.1',8080))
while True:
    cmd = input('pls input your cmd:').strip()
    if not cmd:continue
    # ssh_client.send(cmd.encode('utf-8'))
    ssh_client.send(bytes(cmd,encoding='utf-8'))
    data = ssh_client.recv(4096)
    print(data.decode('gbk'))
    # print(data)

ssh_client.close()