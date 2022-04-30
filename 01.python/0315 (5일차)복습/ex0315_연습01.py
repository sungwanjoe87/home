# from random import *
# #1.리스트 생성
# randNum = []
# #2. randNum리스트에 25까지 데이터 넣기.
# for i in range(25):
#     randNum.append(i+1)
# #3. 랜덤 섞기.
# for i in range(500):
#     rno=randint(0,24)
#     randNum[0],randNum[rno] = randNum[rno], randNum[0]

# print (randNum)
# print ('='*188)
# #4. randNum에 있는 데이터를 arrs리스트를 만들어 5개의 1차원 리스트에 추가.
# arrs =[]
# for i in range(0,5):
#     arr2 =[randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)

# print(arrs)

# #5. 무한반복으로 2차원 리스트에 숫자를 넣기
# while True:
#     for arr in arrs:
#         for a in arr:
#             print('{:2s}'.format(str(a)), end='   ')
#         print()

#     #input1에 1~25사이의 원하는 숫자를 받기.
#     input1 = int(input('1~25의 숫자를 입력하세요>>'))

#     for i,arr in enumerate(arrs):
#         if input1 in arr:
#             arrs[i][arr.index(input1)]='X'


# from random import *

# #1.리스트 선언
# randNum = []
# #2. 리스트에 1-25 (i+1 로 0-24가 1-25로 바뀜) 숫자 할당

# for i in range(25):
#     randNum.append(i+1)
# print(randNum)

# #3.랜덤 섞기.
# for i in range(500):
#     rno=randint(0,24)
#     randNum[0],randNum[rno] = randNum[rno], randNum[0]
# print(randNum)


# arrs = []
# #4. arrs로 선언한 리스트에 5자리씩 i,j를 총 5개의 1차원 리스트에 담기
# for i in range(0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)
# print(arrs)

# while True:
#     for arr in arrs:
#         for a in arr:
#             print ('{:2s}' .format(str(a)),end='   ')
#         print()

#     input1 = int(input('1~25중에 X로 바꿀 숫자를 입력하세요'))

#     for i,arr in enumerate(arrs):
#         if input1 in arr:
#             arrs[i][arr.index(input1)]='X'


# #1.리스트 변수 선언 randNum =[]
# from random import *
# randNum = []

# #2.1,25 리스트에 넣기
# for i in range(25):
#     randNum.append(i+1)

# #3. 랜덤 섞기
# for i in range(500):
#     rno=randint(0,24)
#     randNum[0],randNum[rno] = randNum[rno], randNum[0]

# arrs = []
# #4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
# for i in range(0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)
# print(arrs)

# while True:
#     for arr in arrs:
#         for a in arr:
#             print('{:2s}'.format(str(a)),end='   ')
#         print()

#     input1 = int(input('1~25중 X로 바꿀 수를 입력하세요>>'))

#     for i,arr in enumerate(arrs):
#         if input1 in arr:
#             arrs[i][arr.index(input1)]='X'

# #1.리스트 변수 선언 randNum =[]
# from random import *
# randNum = []
# #2.1,25 리스트에 넣기
# for i in range(25):
#     randNum.append(i+1)
# #3. 랜덤 섞기
# for i in range(500):
#     rno=randint(0,24)
#     randNum[0], randNum[rno] = randNum[rno], randNum[0]    
# #4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
# arrs = []
# for i in range(0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)

# while True:
#     for arr in arrs:
#         for a in arr:
#             print('{:2s}'.format(str(a)),end='   ')
#         print()

#     input1=int(input('1부터 25중 X로 바꿀 번호를 입력하세요'))

#     for i,arr in enumerate(arrs):
#         if input1 in arr:
#             arrs[i][arr.index(input1)]='X'
#1.리스트 변수 선언 randNum =[]
# from random import *
# randNum = []
# #2.1,25 리스트에 넣기
# for i in range(25):
#     randNum.append(i+1)
# #3. 랜덤 섞기(500번)
# for i in range(500):
#     rno=randint(0,24)
#     randNum[0], randNum[rno] = randNum[rno], randNum[0]

# #4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
# arrs = []

# for i in range(0,5):
#     arr2 = [randNum[5*i+j] for j in range(0,5)]
#     arrs.append(arr2)

# #5.무한 반복으로 arr는 5X5형태로 바꾸고, input1에 1~25 받아서 X 변경.


# while True:
#     for arr in arrs:
#         for a in arr:
#             print('{:2s}'.format(str(a)),end='  ')
#         print()

#     input1 = int(input('1~25중에 x로 바꿀 번호를 입력하세요>>'))

#     for i,arr in enumerate(arrs):
#         if input1 in arr:
#             arrs[i][arr.index(input1)]='X'

#1.리스트 변수 선언 randNum =[]
from random import *
randNum = []
#2.1,25 리스트에 넣기
for i in range(25):
    randNum.append(i+1)
#3. 랜덤 섞기(500번)
for i in range(500):
    rno = randint(0,24)
    randNum[0], randNum[rno] = randNum[rno], randNum[0]
#4. arrs로 선언한 리스트에 arr2 5자리씩 i,j를 총 5개의 1차원 리스트에 담기.
arrs = []

for i in range (0,5):
    arr2 = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2)

#5.무한 반복으로 arr는 5X5형태로 바꾸고, input1에 1~25 받아서 X 변경.

while True:

    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end='   ')
        print()

    input1=int(input('1~25중 X로 바꿀 번호를 입력하세요>>'))

    for i,arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)]='X'