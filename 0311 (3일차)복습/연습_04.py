from random import *

my_num = []
lotto = []
ok_num = []
count = 0
l_count = 0

#숫자를 넣기.
for i in range(6):
    a=int(input('{}번째 숫자를 입력하세요>>' .format(i+1)))
    my_num.append(a)


#로또번호 중복 없이 넣기.

while True:

    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print("6개의 숫자가 추출되었습니다.")
        break

#맞춘번호 넣고 숫자 올리기.

for i in range(6):
    if my_num[i] in lotto:
       l_count +=1
       ok_num.append(my_num[i])

print('입력한 번호:', my_num)
print('로또번호:', lotto)
print('맞춘갯수:', l_count)
print('맞춘번호:', ok_num)
