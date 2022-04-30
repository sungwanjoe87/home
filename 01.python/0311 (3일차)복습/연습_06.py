from random import *

my_num = []
lotto = []
ok_num = []
count = 0
l_count = 0


for i in range(6):
    a=int(input('{}번째 숫자를 입력하세요'. format(i+1)))
    my_num.append(a)


while True:
    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            count +=1
    else:
        print('6개의 숫자가 추출되었습니다.')
        break

for i in range(6):
    if my_num[i] in lotto:
        l_count += 1
        ok_num.append(my_num[i])

print('내가 넣은 번호는?>>', my_num)
print('이번 로또 당첨번호는>>', lotto)
print('내가 맞춘 갯수는>>', l_count)
print('맟춘번호는?', ok_num)
