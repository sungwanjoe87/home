from random import *

my_num = []
lotto = []
C_num = []
count = 0
l_count = 0

#1번호 받기.

for i in range(6):
    a=int(input('{}번째 번호를 입력하세요'.format(i+1)))
    my_num.append(a)


while True:

    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('{}개의 숫자가 추출되었습니다'.format(count))
        break

#넣은 숫자가 로또번호와 일치하면 l_count를 반환하고, 맞는 숫자도 나오게

for i in range(6):
    if my_num[i] in lotto:
        C_num.append(my_num[i])
        l_count +=1

print('입력한 번호:', my_num)
print('로또번호:', lotto)
print('맟춘번호:', C_num)
print('맟춘 갯수:', l_count)
