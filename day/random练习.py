
import random
# def valia():
#     s =''
#     for i in range(5):
#         rnum = random.randint(0,9)
#         rstr = chr(random.randint(65,122))
#         res = random.choice([rnum,rstr])
#         s = ''.join(str(s) + str(res))
#
#
#     return s
#
# print(valia())

def ma():
    code = ''
    for i in range(5):
        rnum = random.randint(0,9)
        ralp = chr(random.randint(65,122))
        rres = random.choice([rnum,ralp])

        code = ''.join([str(code),str(rres),'wang'])

    return code
print(ma())

