import os,json,struct,socket
ftp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ftp_server.bind(('127.0.0.1',8080))
ftp_server.listen(5)
while True:
    conn, addr = ftp_server.accept()
    while True:
        try:
            head_struct = conn.recv(4)
            if not head_struct:break
            head_len = struct.unpack('i',head_struct)[0]
            head_json = conn.recv(head_len).decode('utf-8')
            head_dic = json.loads(head_json)
            cmd = head_dic['cmd']

            file_path = os.path.normcase(os.path.join(
                'C:\\Users\\Tony\\Desktop\\file_upload',
                head_dic['filename']
            ))
            filesize = head_dic['filesize']
            recv_size = 0
            with open(file_path,'wb') as f:
                while recv_size < filesize:
                    recv_data = conn.recv(8192)
                    f.write(recv_data)
                    recv_size += len(recv_data)
        except Exception:
            raise '错误~~~~~~~~~~~~~~~~'
            break

ftp_server.close()
