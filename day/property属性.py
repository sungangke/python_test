
class Peopel:
    def __init__(self,name,SEX):
        self.name = name
        self.sex = SEX
        # self.__sex = SEX
    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self,value):
        if not isinstance(value,str):
            raise TypeError
        self.__sex = value

    @sex.deleter
    def sex(self):
        del self.__sex
p1 = Peopel('kk','sssss')
# print(p1.sex())
# print(p1.sex)

del p1.sex
print(p1.sex)
