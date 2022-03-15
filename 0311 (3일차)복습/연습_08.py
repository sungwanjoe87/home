from random import *

my_n = []
lotto = []
C_num = []
l_count = 0
count = 0

for i in range(6):
    a=int(input('{}번째 번호를 입력해 주세요>>'.format(i+1)))
    my_n.append(a)


while True:
    if count <=5:
        temp=randint(1,45)
        if temp not in lotto:
            count +=1
            lotto.append(temp)
    else:
        print("6개의 번호가 추첨되었습니다.")
        break

if i in range(6):
    if my_n[i] in lotto:
        C_num.append(my_n[i])
        l_count += 1

print ('내가 고른 숫자:' , my_n)
print ('이번 로또번호는:', lotto)
print ('내가 맞춘 갯수:', l_count)
print ('내가 맟춘 번호:', C_num)
