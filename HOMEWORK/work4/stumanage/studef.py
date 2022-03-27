from stumanage.student import Student #패키지(폴더).파일 import 클래스

stuSave =[]

def screenPrint(): #첫 화면
    print('[학생성적프로그램]')
    print('+'*50)
    print('[1. 학생성적입력]')
    print('[2. 학생성적수정]')
    print('[3. 학생성적삭제]')
    print('[4. 학생성적출력]')
    print('[5. 학생성적검색]')
    print('[6. 학생등수처리]')
    print('+'*50)
    print()
    choice = int(input('원하는 번호를 입력하세요>>'))
    return choice


def stuInput(): #성적입력
    while True:
        print('학생성적입력을 선택하셨습니다.')
        stuname = input('학생이름을 입력하세요>(0.입력종료)')
        if stuname =='0':
            break
        kor = int(input('국어점수를 입력하세요>>'))
        eng = int(input('영어점수를 입력하세요>>'))
        temp = Student(stuname,kor,eng)
        stuSave.append(temp)
        print('{}번 학생이 저장되었습니다.'.format(temp.stuno,stuname))
        print('-'*80)

def stuModify(): #성적수정 함수
    print('성적수정을 선택하셨습니다.')
    sname = input('수정할 학생의 이름을 입력하세요>>')
    count = 0
    for stu in stuSave:
        if stu == sname :
            print('{} 학생이 검색되었습니다.'.format(sname))
            print('[성적수정페이지]')
            print('[1.국어점수 수정]')
            print('[2.영어점수 수정]')
            changescore = input('수정을 원하는 과목의 번호를 입력하세요>>')
            if changescore ==1:
                score = int(input('수정할 점수를 입력하세요>>'))
                stu.setKor(score) #setKor 호출하여 입력값 바꾸기.
                print('국어점수가 {}점으로 변경되었습니다'.format(score))
            elif changescore == 2:
                print('현재 영어 점수: {}'.format(stu.eng))
                score = int(input('변경할 점수를 입력하세요>>'))
                stu.setEng(score) #Student class의 setEng 호출하여 score로 점수 입력
                print('영어점수가 {}으로 변경되었습니다.'.format(score))
                count=1
                break

    if count ==0:
        print('{} 으로 검색된 학생이 없습니다. 다시 입력하세요.'.format(sname))

def topTitle():
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
    print('='*70)

def stuOutput(): #학생성적전체출력함수
    print('성적 전체출력을 선택하셨습니다.')
    topTitle()
    for stu in stuSave: #stuSave안에 있는 stu 모두 출력.
        print(stu)

def stuSearch(): #학생성적 검색함수
    print('학생성적 검색 출력을 선택하셨습니다.')
    searchName = input('검색할 이름을 입력하세요>>')
    count = 0
    for stu in stuSave:
        if stu == searchName:
            topTitle()
            print(stu)
            count = 1
            break
    if count ==0:
        print('해당하는 {} 학생은 없습니다. 다시 입력하세요'.format(searchName))

def stuDelete(): #학생성적삭제함수
    print('학생성적 삭제를 선택하셨습니다.')
    searchN = input('삭제하고자 하는 이름을 입력하세요')
    count = 0
    for i,stu in enumerate(stuSave):
        if stu ==searchN:
            print('{}학생이 검색되었습니다...'.format(searchN))
            flag =input('정말 삭제하시겠습니까? (y or x)')
            if flag =='y' or flag == 'x':
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(searchN))

def stuRank(): #등수 작업 함수
    print('등수 메깁니다.')
    for stu1 in stuSave:
        rcount =1
        for stu2 in stuSave:
            if stu1 < stu2:
                rcount +=1
        stu1.rank = rcount
    print('등수가 메겨젔습니다.')
    