import re
with open('1.txt','rb') as f:
    # pattern =re.compile(u"[\u4e00-\u9fa5]+")
    # for line in f:
    #     line=line.decode('utf8')
    #     result=re.findall(pattern,line)
    #     for w in result:
    #         print(w)
    for line in f.readlines():
        line=line.strip().decode('utf8')
        res=re.sub(u"[\u4e00-\u9fa5]+",'',line)
        l=[]
        if res != '':
            l.append(res)
        for i in l:
            print(i)

