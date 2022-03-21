def order():
    print('주문하실 음료를 알려주세요')
    drink = input('주문하실 음료를 입력하세요>>')
    a =print('{} 주문하셨습니다.'.format(drink))
    return a
count =0

temp = order()


def mul(a1,a2,a3=1):
    temp = []
    result1 = a1+a2+a3
    temp.append(result1)
    result2 = a1-a2-a3
    temp.append(result2)
    result3 = a1*a2*a3
    temp.append(result3)
    result4 = a1/a2/a3
    temp.append(result4)
    return temp


a= mul(2,4,8)
b= mul(4,12)

print(a[0], a[1], a[2], a[3])
print(b[0], b[1], b[2], b[3])



# def korean_age():
#     import datetime
#     myage = 0
#     myage = int(input('태어난 년도를 입력하세요'))
#     age = datetime.today.year() - myage
#     return myage

# temp = korean_age()


def my_friend(friendName):
    print("{}는 나의 친구 입니다.".format(friendName))

my_friend("철수")
my_friend("오징어")


def my_calc(x,y):
    z = x*y
    return z

temp = my_calc(3,4)
print(temp)
