
def eater(name):
    print('%s start to eat '%name)
    food_list = []
    while True:
        food = yield food_list
        print('%s get food and eat %s' %(name,food))
        food_list.append(food)
    print('done')
g = eater('kk')

print(next(g))
g.send('包子')
print(g.send('miao'))


#如果在一个函数内部yield的使用方式是表达式形式的话，如x=yield，那么该函数成为协程函数
# def eater(name):
#     print('%s start to eat food' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s get %s ,to start eat' %(name,food))
#         food_list.append(food)
#
#     print('done')
#
#
# e=eater('钢蛋')
# # print(e)
#
# print(next(e))
# print(e.send('包子'))
# print(e.send('韭菜馅包子'))
# print(e.send('大蒜包子'))
#
# #为什么叫协程？
# #协程怎么用？