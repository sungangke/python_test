import socket
import select


class Request(object):
    def __init__(self,sock,info):
        self.sock = sock
        self.info = info

    def fileno(self):
        return self.sock.fileno()

class QinBing(object):
    def __init__(self):
        self.sock_list = []
        self.conns = []

    def add_request(self,req_info):
        """
        创建请求
        :return:
        """
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((req_info['host'], req_info['port']))
        except BlockingIOError as e:
            pass
        obj = Request(sock,req_info)
        self.sock_list.append(obj)
        self.conns.append(obj)

    def run(self):
        """
        开始事件循环
        :return:
        """
        while True:
            r,w,e = select.select(self.sock_list,self.conns,[],0.05)
            for obj in w:
                data = "GET %s http/1.1\r\nhost: %s\r\n" %(obj.info['path'],obj.info['host'])
                obj.sock.send(data.encode('utf-8'))
                self.conns.remove(obj)

            for obj in r:
                response = obj.sock.recv(8096)
                print(response)
                self.sock_list.remove(obj)

            if not self.sock_list:
                break

url_list= [
    {'host':'www.baidu.com','port':80,'path':'/'},
    {'host':'www.cnblogs.com','port':80,'path':'/index.html'},
    {'host':'www.bing.com','port':80,'path':'/'},

]
qinbing = QinBing()
for item in url_list:
    qinbing.add_request(item)
qinbing.run()