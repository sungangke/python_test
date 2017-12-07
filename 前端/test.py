# list_num = []
# import numpy as np
# t1,t2,t3='','',''
# with open('1.txt','r') as f:
#     for line in f:
#         (t1,t2,t3) = line.split(',',3)
#         print(t2)


# with open('1.txt',encoding='utf8') as f:
#     data_1 = f.readline().strip().split(',')
#     # print(data_1)
#     dic = {}
#     for line in f:
#         data_2 = line.strip().split(',')
#         # print(data_2)
#         val_list=[]
#         # for i in data_1:
#         #     # print("i",i)
#         #     ind = data_1.index(i)
#         #     dic[i]=data_2[ind]
#         # print(dic)

filename=r'1.txt'
l=[]
v=[""]*len(open('1.txt').readlines())

with open(filename,'r') as f:
	for line in f:
		line=line.replace("\n","").split(",")
		l.append(line)
for i in range(0,3):
    # print(i)
	v[i]=dict(zip(l[0],l[i]))
print(l)
print(v)
print(l[0])
print(l[1])
print(dict(zip(l[0],l[1])))
#
# for j in v:
#     print(j)
