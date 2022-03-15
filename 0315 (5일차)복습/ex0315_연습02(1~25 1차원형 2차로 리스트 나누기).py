# #1.리스트 변수 선언 randNum =[]
# from random import *
# randNum = []
# #2.1,25 리스트에 넣기
# for i in range(25):
#     randNum.append(i+1)
# #3. 랜덤 섞기(500번)
# for i in range(500):
#     rno = randint(0,24)
#     randNum[0], randNum[rno] = randNum[rno], randNum[0]
# #4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
# arrs = []

# for i in range (0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)

# from random import*

# randNum = []

# for i in range(25):
#     randNum.appen(i+1)

# for i in range(500):
#     rno = randint(0,24)
#     randNum[0], randNum[rno] = randNum[rno], randNum[0]

# arrs = []

# for i in range(0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)


from random import *

randNum = []

for i in range(25):
    randNum.append(i+1)

for i in range(500):
    rno=randint(0,24)
    randNum[0], randNum[rno] = randNum[rno], randNum[0]

arrs = []
 #4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
for i in range(0,5):
    arr2 = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2) 


while True:
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end='   ')
        print()

    input1 = int(input('1~25번호 사이에 X로 변경할 숫자를 입력하세요>>'))

    for i,arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)]='X'