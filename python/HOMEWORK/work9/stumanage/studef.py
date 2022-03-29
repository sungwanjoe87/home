from stumanage.student import Student

stuSave = [] #학생성적이 저장될 전역 리스트 선언.

# 화면출력
def screenPrint():
    print('[학생성적프로그램]')
    print('='*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print()
    choice =int(input('원하는 번호를 입력하세요>>'))

    return choice

#학생성적입력
def stuInput():
    while True:
        print('[학생성적입력 선택]')
        stuname = input('학생이름을 입력하세요.(0.입력:종료)>>')
        if stuname =='0':
            break
        kor = int(input('국어성적 입력>>'))
        eng = int(input('영어성적 입력>>'))
        temp = Student(stuname,kor,eng) #class student에서 total,avg 계산됨.
        stuSave.append(temp)
        print('{}번. {}학생이 저장되었습니다.'.format(temp.stuno,stuname))
        print() #한칸 띄우기.

#출력에 사용되는 연속된 상단 타이틀
def topTitle():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
    print('='*70)

#학생전체출력 ->__str__ 자동 호출
def stuOutput():
    topTitle() #타이틀 출력함수
    for stu in stuSave:
        print(stu)

# 학생검색출력 -> __eq__자동 호출
def stuSearch():
    print()
    print('[ 학생검색출력 ]')
    searchName = input('학생이름을 입력하세요.>>')
    count=0
    for stu in stuSave:
        if stu == searchName:
            topTitle()
            print(stu)
            count=1
            break
    
    if count == 0:
        print('{}학생은 없습니다. 다른 이름을 검색하세요!!'.format(searchName))


#학생성적수정
def stuModify():
    print()
    print('[학생성적수정 선택')
    searchName = input('검색할 학생의 이름을 입력하세요')
    count = 0 #검색 카운트 변수 초기화
    for stu in stuSave:
        if stu ==searchName:
            print('{} 학생이 검색되었습니다.'.format(searchName))
            print('[성적수정]')
            print('[1.국어점수]')
            print('[2.영어점수]')
            changeNum = int(input('수정할 과목 번호를 입력하세요>>'))
            if changeNum ==1:
                print('현재 국어 점수: {}'.format(stu.kor))
                score = int(input('변경할 점수를 입력하세요>>'))
                stu.setKor(score) #Student class의 setKor 호출하여 score로 점수 입력
                print('국어점수가 {}으로 변경되었습니다.'.format(score))
            elif changeNum == 2:
                print('현재 영어 점수: {}'.format(stu.eng))
                score = int(input('변경할 점수를 입력하세요>>'))
                stu.setEng(score) #Student class의 setEng 호출하여 score로 점수 입력
                print('영어점수가 {}으로 변경되었습니다.'.format(score))
            count=1
            break

    if count ==0:
        print('{}으로 검색된 학생이름이 없습니다! 다시 입력하세요.'.format(searchName))


#학생성적 삭제
def stuDelete():
    print('학생삭제를 선택하셨습니다.')
    count =0
    searchName = input('삭제할 이름을 입력하세요>>')
    for i,stu in enumerate(stuSave):
        if stu ==searchName:
            print('{} 학생이 검색되었습니다.'.format(searchName))
            flag = input('정말 삭제하시겠습니까? (y or n)')
            if flag =='y' or flag =='n':
                del(stuSave[i])
                print('{}학생이 삭제 되었습니다.'.format(searchName))
                count=1
                break
        elif count ==0:
            print('{} 학생이 없습니다. 다시 입력하세요'.format(searchName))

#학생등수처리
def stuRank ():
    for stu1 in stuSave: 
        rcount =1 
        for stu2 in stuSave:
            if stu1 < stu2: 
                rcount += 1 #클래스 __lt__자동호출
        stu1.rank = rcount 
    print('등수처리가 완료되었습니다.')
    print()