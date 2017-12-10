import os,json,struct,socket
ftp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ftp_client.connect(('127.0.0.1',8080))
while True:
    inp = input(">>: ").strip()
    if not inp:continue
    l=inp.split()
    cmd = l[0]
    if not os.path.isfile(l[1]):break
    else:
        filesize = os.path.getsize(l[1])
    head_dic = {'cmd': cmd, 'filename': os.path.basename(l[1]), 'filesize': filesize}
    head_json = json.dumps(head_dic)
    head_bytes = head_json.encode('utf-8')
    head_struct = struct.pack('i',len(head_bytes))
    ftp_client.send(head_struct)
    ftp_client.send(head_bytes)
    send_size = 0
    with open(l[1],'rb') as f:
        for line in f:
            ftp_client.send(line)
            send_size += len(line)
        else:
            print('update successful')




