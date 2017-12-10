import time
current_login={'name':None,'login':False}

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)  #my_max(1,2)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

def auth2(auth_type='file'):
    def auth(func):
        # print(auth_type)
        def wrapper(*args,**kwargs):
            if current_login['name'] and current_login['login']:
                res=func(*args,**kwargs)
                return res
            if auth_type == 'file':
                name=input('username: ')
                password=input('password: ')
                if name == 'ke' and password == '123':
                    print('auth successfull')
                    res=func(*args,**kwargs)
                    current_login['name']=name
                    current_login['login']=True
                    return res
                else:
                    print('auth error')
            elif auth_type == 'sql':
                print('还他妈不会玩')
        return wrapper
    return auth

@timmer
@auth2(auth_type='sql') #@auth  #index=auth(index)
def index():
    print('welcome to inex page')

@auth2()
def home():
    print('welcome to home page')



#调用阶段
index()
home()

