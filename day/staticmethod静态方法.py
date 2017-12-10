import  time

class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month =month
        self.day = day
    @staticmethod
    def now():
        obj = time.localtime()
        return Date(obj.tm_year,obj.tm_mon,obj.tm_mday)

# d1 = Date()
# d1.now()
date_now = Date.now()
print(date_now.year)