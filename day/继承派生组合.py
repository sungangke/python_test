# class Hero:
#     def __init__(self,nickname,aggres,life_value):
#         self.nick = nickname
#         self.aggres = aggres
#         self.life = life_value
#
#     def attack(self,emery):
#         print('hero attack')
#         # emary_life -= self.aggres
#
# class Green(Hero):
#
#     def __init__(self,nickname,aggres,life_value,script):
#         Hero.__init__(self,nickname,aggres,life_value)
#         self.script = script
#
#     def attack(self,emery):
#         Hero.attack(self,emery)
#         print('green attack')
#
# g1 = Green('garen',18,200,'干干干')
# print(g1.script)
# g1.attack('g1')



##组合

class Teacher(object):
    def __init__(self,name,sex,course):
        self.name = name
        self.sex = sex
        self.course = course

class Student(object):
    def __init__(self,name,sex,course):
        self.name = name
        self.sex  = sex
        self.course = course

class Course(object):
    def __init__(self,name,price,priod):
        self.name = name
        self.price = price
        self.priod = priod

class Birth(object):
    def __init__(self,name,sex,dates):
        self.name = name
        self.sex = sex
        self.dates =dates


Student_obj = Student('wang','man','python')
Python_obj = Course('python',15900,'7m')
Teacher_obj = Teacher('alex','female',Python_obj)

Birth_obj = Birth(Teacher_obj.name,Teacher_obj.sex,'2017-01-01')
print(Teacher_obj.course.name)