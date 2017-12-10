current_login={'name':None,'login':False}

def authself(auth_type):
    def auth(func):
        def wrapper(*args, **kwargs):
            # if current_login['name'] and current_login['login']:
            #     res = func(*args, **kwargs)
            #     return res
            # else:
            #     print('用户没有登陆，请输入用户名和密码登陆')
            #     # name = input('username:').strip()
            #     # pwd = input('password:').strip()
            #     # if name == 'kesungang' and pwd == '123':
            #     #     current_login['name'] = name
            #     #     current_login['login'] = True
            #     #     print('登陆成功')
            #     #     res = func(*args,**kwargs)
            #     #     return res
            if auth_type == 'file':
                name = input('username:').strip()
                pwd = input('password:').strip()
                with open('key.txt', 'a') as f:
                    dbname = f.read()
                    if name == eval('dbname')['name'] and eval('dbname')['login'] == 'True':
                        res = func(*args, **kwargs)
                        return res
                    else:
                        print('key文件里面还没有这个用户')
                        f.write(current_login+'\n')
            elif auth_type == 'sql':
                print('没有写sql认证那')

        return wrapper
    return auth
# @auth #index=authself(index)
# def index():
#     print('Welcome to index page')
#
# index()

# @authself(auth_type='file')
@authself(auth_type='file')
# @auth
def home():
    print('Welcome to the home page')
home()

# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print('run time is %s ' %(stop-start))
#     return wrapper
#
#
# @timmer
# def index():
#     print('welcome to oldboy')
#
# index()