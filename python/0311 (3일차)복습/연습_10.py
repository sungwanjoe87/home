from random import *

my_n = []
lotto = []
ok_num = []
count = 0
lcount = 0

for i in range(6):
    a=int(input('{}번째 숫자를 입력하세요>>'. format(i+1)))
    my_n.append(a)

while True:
    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count +=1

    else:
        print('{}개의 숫자가 추출되었습니다.'. format(count))
        break

for i in range(6):
    if my_n[i] in lotto:
        ok_num.append(my_n[i])
        lcount += 1


print ('내가 찍은 번호:', my_n)
print ('이번 로또 번호는:', lotto)
print ('내가 맞춘 번호의 갯수는:', lcount)
ok_num.sort()
print ('내가 맞춘 숫자는:', ok_num)
