#로또번호 맟추기.
from random import *

lotto = []
입력번호 = []
맞는번호 = []
count = 0
맞춘갯수 = 0

for i in range (6):
    a=int(input('{}번째 번호를 입력하세요>>' .format(i+1)))
    입력번호.append(a)

while True:
    
    if count <=5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('6개의 번호가 추출되었습니다.')
        break

for i in range(6):
    if 입력번호[i] in lotto:
        맞춘갯수 += 1
        맞는번호.append(입력번호[i])

print('로또번호:', lotto)
print('입력번호:', 입력번호)
print('맞춘갯수:', 맞춘갯수)
print('맞춘번호:', 맞는번호)