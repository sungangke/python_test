
# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n-1) + 2
#
# print(age(5))

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
new_data =[]
#num = input('>>>').strip()
def search(num,data):
    print(data)
    if num > data[int(len(data)/2)]:
        data = data[int(len(data)/2):]
        search(num,data)

    elif num < data[int(len(data)/2)]:
        data = data[:int(len(data) / 2)]
        search(num, data)
    else:
        print(data.index(num))
        return
search(17,data)

