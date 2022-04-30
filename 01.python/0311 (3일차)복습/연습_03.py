from random import *

my_num = []
lotto = []
맞춘번호 = []
count = 0
l_count = 0

for i in range(6):
    a=int(input('{}번째 번호를 입력해 주세요>>' .format(i+1)))
    my_num.append(a)


while True:

    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('{}개의 번호가 추출되었습니다.' .format(count))
        break

for i in range(6):
    if my_num[i] in lotto:
        l_count += 1
        맞춘번호.append(my_num[i])


print('입력번호:', my_num)
print('로또번호', lotto)
print('맞춘번호:', 맞춘번호)
print('맞은갯수:', l_count)