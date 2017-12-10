#"1 - 2 * ( (60-30*2+-96) - (-4*3)/ (16-3*2) )"
s='1 - 2 * ( (60-30*2+-96) - (-4*3)/ (16-3*2) )'
import re


r1 = re.search(r'\([^()]+\)',s)
s1=r1.group()
print(s1)
# print(len(s1))
# # k[1:len(k) - 1]
# print(s1[1:len(s1) - 1])
# sum1 = s1.replace('+-','-')
# print(sum1)
#
# #去括号
nokuo = re.sub(r'\(|\)','',sum1)
print(nokuo)
# #乘法计算
#
# chf = re.search(r'\d+\.?\d*\*\d+\.?\d*',nokuo)
# chf_res= chf.group()
# rz1 = re.split(r'\*',chf_res)
# szz1 = int(rz1[0]) * int(rz1[1])
# # print(szz1)
# print(chf_res)


