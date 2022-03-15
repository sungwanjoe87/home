from random import *

my_num = []
lotto = []
ok_num = []
count = 0
l_count = 0

for i in range(6):
    a=int(input('{}번째 숫자를 입력해 주세요>>' .format(i+1)))
    my_num.append(a)


while True:

    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('{}개의 숫자가 뽑혔습니다.' .format((i+1)))
        break

for i in range(6):
    if my_num[i] in lotto:
        ok_num.append(my_num[i])
        l_count += 1


print('내가 넣은 번호:', my_num)
print('이번 로또 번호:', lotto)
print('내가 맞춘 갯수:', l_count)
print('내가 맞춘번호:', ok_num)

