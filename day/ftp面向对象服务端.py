import os,json,struct,socket
class MyFtpServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding='utf-8'
    request_queue_size = 5
    server_dir='C:\\Users\\Tony\\Desktop\\file_upload'
    def __init__(self,server_address,bind_and_activate=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except Exception:
                self.server_closer()

    def server_bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        self.socket.listen(self.request_queue_size)

    def server_closer(self):
        self.socket.close()

    def get_request(self):
        return self.socket.accept()

    def close_request(self,request):
        request.close()

    def run(self):
        while True:
            self.conn,self.client_addr = self.get_request()
            print('from client:',self.client_addr)
            while True:
                try:
                    head_struct = self.conn.recv(4)
                    if not head_struct:
                        break
                    head_len = struct.unpack('i',head_struct)[0]
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)
                    cmd = head_dic['cmd']
                    if hasattr(self,cmd):
                        func = getattr(self,cmd)
                        func(head_dic)
                except Exception:
                    break

    def put(self,args):
        file_path = os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))
        filesize = args['filesize']
        recv_size = 0
        print('----->', file_path)
        with open(file_path, 'wb') as f:
            while recv_size < filesize:
                recv_data = self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size += len(recv_data)
                print('recvsize:%s filesize:%s' % (recv_size, filesize))

tcpserver1 = MyFtpServer(('127.0.0.1', 8080))

tcpserver1.run()