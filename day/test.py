import os
g = os.walk('D:\\egon')
for i in g:
    for j in i[-1]:
        file_path = '%s\\%s'%(i[0],j)
        print(file_path)