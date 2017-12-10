import socketserver
class MyFtpserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        while True:#接收循环
            data = self.request.recv(1024)
            print(data)
            self.request.send(data.upper())
if __name__ == '__main__':
    obj = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyFtpserver)
    obj.serve_forever()#链接循环