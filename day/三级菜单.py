menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


# exit_flag = False
# current_layer = menu
#
# layers = [menu]
# # print(current_layer)
#
# while not  exit_flag:
#     for k in current_layer:
#         print(k)
#     choice = input(">>:").strip()
#     if choice == "b":
#         current_layer = layers[-1]
#         #print("change to laster", current_layer)
#         layers.pop()
#     elif choice not  in current_layer:continue
#     else:
#         layers.append(current_layer)
#         current_layer = current_layer[choice]
exit_flag = False
while not exit_flag:
    for item in menu:
        print(item)
    choice = input("城市>>").strip()
    if len(choice) == 0: continue
    if choice == 'q':
        exit_flag = True
        continue
    if choice in menu:
        while not exit_flag:
            lay1 = menu[choice]
            for key1 in lay1:
                print(key1)
            choice2 = input("城市>>").strip()
            if len(choice2) == 0: continue
            if choice2 == 'b': break
            if choice2 == 'q':
                exit_flag = True
                continue
            if choice2 in lay1:
                while not exit_flag:
                    lay2 = lay1[choice2]
                    for key2 in lay2:
                        print(key2)
                    choice3 = input("城市>>").strip()
                    if len(choice3) == 0: continue
                    if choice3 == 'b': break
                    if choice3 == 'q':
                        exit_flag = True
                        continue
                    if choice3 in lay2:
                        while not exit_flag:
                            lay3 = lay2[choice3]
                            for key3 in lay3:
                                print(key3)
                            choice4 = input("城市>>").strip()
                            if choice4 == 'b': break
                            if choice4 == 'q':
                                exit_flag = True
                                continue

