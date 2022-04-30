# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

# stuSave = [[0]*7 for i in range(0)]
from turtle import up, update
from numpy import mat


stuSaves = []
stusave = []
# print(stuSave)
# 학생가입인원 확인count
sCount = 0
while True:
    print('[ 학생성적프로그램 ]')
    print('='*25)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('5. 학생성적검색')
    print('0. 프로그램종료')
    print('='*25)
    choice = int(input('원하는 번호를 입력하세요.>>'))
    
    if choice==1:
        print('-- {}번째 학생등록 -- '.format(sCount+1))
        sName = input('학생이름을 입력하세요.>>')
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>')) 
        math = int(input('수학 성적을 입력하세요.>>'))
        total = kor+eng+math
        avg = total/3
        stuSave =[sCount+1,sName,kor,eng,math,total,avg]
        stuSaves.append(stuSave)
        sCount += 1 #학생인원 count 1증가
        print('학생성적이 저장되었습니다.')
        print(stuSave)
        
        
    elif choice==2:
        print('학생성적 수정을 선택하셨습니다.')
        a = str(input('수정할 학생의 이름을 입력하세요:'))

        if(a in stuSave) == True:
            sName = input('학생이름을 입력하세요')
            kor = input('국어 점수를 입력하세요>>')
            eng = input('영어 점수를 입력하세요>>')
            math = input('수학 점수를 입력하세요>>')
            print('성적 수정이 완료되었습니다.')

            stuSave = [sCount,sName,kor,eng,math,total,avg]
            stuSaves.insert(stuSave)

            continue
        else:
            print('이름의 학생이 없습니다.')
            continue
        


    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
    elif choice==4:
        print('학생성적전체출력을 선택하셨습니다.')
        print(stuSaves)
    elif choice==5:
        print('학생성적검색을 선택하셨습니다.')
    
    elif choice==0:
        print('프로그램을 종료합니다.')
        break