# Process类调用

from multiprocessing import Process
import time
def f(name):

    print('hello', name,time.ctime())
    time.sleep(1)

if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = Process(target=f, args=('alvin:%s'%i,))
        p_list.append(p)
        p.start()
    for i in p_list:
        p.join()
    print('end')

# 继承Process类调用
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        # self.name = name

    def run(self):

        print ('hello', self.name,time.ctime())
        time.sleep(1)


if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')