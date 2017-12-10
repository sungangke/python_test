import os
def init(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        next(res)
        return res
    return wrapper()



@init
def serarch(target):
    while True:
        dir_name = yield
        g = os.walk(dir_name)
        for i in g:
            for j in i[-1]:
                file_path = '%s\\%s'%(i[0],j)
                target.send(file_path)
@init
def opener(target):
    while True:
        file_path = yield
        with open(file_path) as f:
            target.send((file_path,f))

@init
def cat(target):
    while True:
        file_path,f = yield
        for line in f:
            target.send((file_path,line))

@init
def grep(partten,target):
    while True:
        file_path,line = yield
        if partten in line:
            target.send(file_path)

@init
def printer(target):
    while True:
        file_path = yield
        print(file_path)


g=search(opener(cat(grep('python',printer()))))
g.send('D:\\egon')