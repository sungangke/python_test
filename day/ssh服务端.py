import socket
import subprocess
ssh_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssh_server.bind(('127.0.0.1',8080))
ssh_server.listen(5)
while True:
    conn, addr = ssh_server.accept()
    while True:
        try:
            data = conn.recv(4096)
            if not data: break
            print(data)
            res = subprocess.Popen(str(data,encoding='utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_out = res.stdout.read()

            conn.send(cmd_out)
            res.stdout.close()
            cmd_err_out = res.stderr.read()
            conn.send(cmd_err_out)
            res.stderr.close()
        except Exception:
            break
    conn.close()

ssh_server.close()

