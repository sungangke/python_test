# m = input("输入你要查询的域名:")
# list = []
# flag = False
# with open('haproxy.conf',encoding='utf-8') as f:
#     for line in f:
#         if line.startswith('backend') and m in line:
#             flag = True
#             continue
#         if line.startswith('backend') and flag:
#             break
#         if flag:
#             list.append(line.strip())
#     for i in list:
#         print(i)

def foo():
    print("a")
    bar()


def bar():
    print("bar")

def xx():
    dfaf()

foo()