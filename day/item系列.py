
class Foo:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        # self.__dict__[key] = value
        print('setitem')
    def __getitem__(self, item):
        self.__dict__[item]

    def __delitem__(self, key):
        self.__dict__.pop(key)

f = Foo('egon')
print(f.name)

f.sex = 'mail'
f['sss'] = 19  #当类里面有item方法的时候，以字典方式赋值的时候就会调用__setitem方法
# print(f.age)
print(f.__dict__)