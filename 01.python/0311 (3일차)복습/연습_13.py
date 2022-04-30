from random import *

my_num = []
lotto = []
ok_num = []
okcount = 0
count = 0


for i in range(6):
    a = int(input('{}번째 숫자를 찍어보삼:' .format(i+1)))
    my_num.append(a)


while True:
    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('{}개의 숫자가 로또번호로 뽑혔습니다.', count)
        break

for i in range(6):
    if my_num[i] in  lotto:
        ok_num.append(my_num[i])
        okcount += 1

print ('내가 뽑은 번호', my_num)
lotto.sort()
print ('로또번호', lotto)
print ('내가 맞춘 갯수:', okcount)
print ('내가 맞춘 번호:', ok_num)
