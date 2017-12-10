import selectors,socket
sock = socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)
sock.setblocking(False)
sel = selectors.DefaultSelector()

def read(conn,mask):
    try:
        data=conn.recv(1024)
        print(data)
        send_data = input(">>>>--:").strip()
        conn.send(send_data.encode('utf-8'))
    except Exception:
        sel.unregister(conn)

def accept(sock,mask):
    conn,addr = sock.accept()
    print(conn)
    sel.register(conn,selectors.EVENT_READ,read)

sel.register(sock,selectors.EVENT_READ,accept)

while 1:
    print('waiting......')
    events = sel.select()
    for key,mask in events:
        func = key.data
        obj = key.fileobj
        func(obj,mask)