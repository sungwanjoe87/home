
from random import *

my_num = []
lotto = []
L_num = []
count = 0
L_count = 0

for i in range(6):
    a=int(input('{}번째 숫자를 입력하세요'.format(i+1)))
    my_num.append(a)

while True:

    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count +=1
    else:
        print('{}개의 번호가 뽑혔습니다!'.format (count))
        break

for i in range(6):
    if my_num[i] in lotto:
        L_count += 1
        L_num.append(my_num[i])

print('내가 뽑은 숫자:', my_num)
lotto.sort()
print('로또 번호는:', lotto)
print('내가 맞춘 갯수:', L_count)
print('내가 맞춘 번호는:', L_num)


