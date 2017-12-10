product_list=[
	['apple',2300],
	['Xiaomi',1300],
	['Huawei',300],
	['旮沓',100],
	['docker',10]
]

sclary=int(input('输入你的工资：'))
shoping_car={}

while True:
    index = 0
    for product in product_list:
        print(index,product)
        index += 1
    choice = input("请输入你的选择》》").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice <= len(product_list):
            product = product_list[choice]
            if sclary >= product[1]:
                if product[0] in shoping_car:
                    product[0][1] += 1
                else:
                    shoping_car[product[0]] = [product[1], 1]

                sclary = sclary - product[1]
                print('购买的商品：'+product[0]+'剩余的钱：'+str(sclary))
            else:
                print("穷逼")

        else:
            print('商品不存在')

    elif choice == "q":

        print("------------购买的商品为------------")
        for i in shoping_car:
            print(i)

        print("当前余额为：",sclary)
        print("------------end------------")
        break
    else:
        print('没有此选项')
