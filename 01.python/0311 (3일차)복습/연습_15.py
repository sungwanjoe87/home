from random import *


my_n =  []
lotto = []
ok_n =  []
count = 0
ok_c  = 0


for i in range(6):
    a=int(input('{}번째 번호를 입력하세요'.format(i+1)))
    my_n.append(a)


while True:
    if count <= 5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('{}개의 로또번호가 추첨되었습니다.' .format(count))
        break

for i in range(6):
    if my_n[i] in lotto:
        ok_n.append(my_n[i])
        ok_c += 1

print ('내가 응모한 번호' , my_n)
print ('로또 번호:', lotto)
print ('내가 맞춘 숫자 갯수:', ok_c)
print ('내가 맞춘 번호:', ok_n)
