from stumanage.student import Student

stuSave = [] #저장 리스트 선언.

def screen_print (): #화면 출력 함수.
    print('[ 성적 관리 프로그램 ] ')
    print('='*45)
    print('[ 1. 학생 성적 입력란   ]')
    print('[ 2. 학생전체성적출력란 ]')
    print('[ 3. 학생성적검색출력란 ]')
    print('[ 4. 학생 성적 수정란   ]')
    print('[ 5. 학생 성적 삭제란   ]')
    print('[ 6. 학생 등수 처리란   ]')
    print('[ 0. 관리프로그램 종료  ]')
    print('+'*50)
    choice = int(input('원하는 번호를 입력하세요>'))
    return choice


def stu_input(): #1.성적입력 함수
    while True:
        print('학생 성적 입력란 입니다.')
        stuname = input('성적을 작성하려는 학생의 이름을 입력하세요>>(입력종료:0) ')
        if stuname == '0': #입력이 str이기에 반드시 str으로 처리.
            break
        kor = int(input('국어 점수를 입력하세요>>'))
        eng = int(input('영어 점수를 입력하세요>>'))
        temp = Student(stuname,kor,eng) #class
        stuSave.append(temp)
        print('{}번째 {} 학생이 등록되었습니다.'.format(temp.stuno,stuname)) #class에서 stuno가지고 와서 출력.
        print('='*40)

def top_title(): #전체출력, 검색출력에 사용되는 상단 함수.
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)

def stu_output (): #2.성적 전체 출력 함수
    print('학생 성적 전체 출력을 선택하였습니다.')
    print('='*60)
    top_title()
    for stu in stuSave:
        print(stu)

def stu_search(): #3.성적 검색 출력 함수
    print('-'*60)
    print('학생 성적 검색 출력을 선택하셨습니다.')
    search_name = input('검색을 원하시는 학생의 이름을 입력하세요>>')
    count = 0
    for stu in stuSave:
        if stu == search_name:
            top_title()
            print(stu)
            count = 1

    if count ==0:
        print('찾으시는 {} 학생이 없습니다. 다시 입력하세요'.format(search_name))

def stu_modify(): #4.학생 성적 수정 함수.
    print('학생 성적 수정을 선택하셨습니다.')
    search_name = input('찾으려는 학생의 이름을 입력하세요>>')
    count = 0
    for stu in stuSave:
        if stu == search_name:
            print('찾으신 {} 학생이 검색되었습니다.'.format(search_name))
            print('[각 성적 수정란]')
            print('[1. 국어 점수 수정]')
            print('[2. 영어 점수 수정]')
            choice =int(input('원하는 번호를 입력하세요'))

            if choice ==1:
                print('현재 국어점수: {}'.format(stu.kor))
                score = int(input('바꾸시려는 점수를 입력하세요>>'))
                stu.setKor(score) #class 음수제한 함수로 입력.
                print('국어점수가 {}점으로 변경되었습니다.'.format(score))
            elif choice ==2:
                print('현재 영어점수: {}'.format(stu.eng))
                score = int(input('바꾸시려는 점수를 입력하세요>>'))
                stu.setEng(score)
                print('영어점수가 {}점으로 변경되었습니다.'.format(score))
            count =1
            break

    if count ==0:
        print ('입력하신 {} 학생이 존재하지 않습니다. 다시 입력해 주세요.'.format(search_name))


def stu_delete(): #학생성적 삭제함수.
    print('학생성적 삭제를 선택하셨습니다.')
    count =0
    delname = input('삭제하려는 학생의 이름을 입력하세요>>')
    for i,stu in enumerate(stuSave):
        if stu == delname:
            print('{} 학생이 검색 되었습니다.'.format(delname))
            flag = input('정말 삭제하시겠습니까? (y or n)')
            if flag == 'y' or flag == 'n':
                del(stuSave[i])
                print('{} 학생의 성적이 삭제되었습니다.'.format(delname))
                count = 1
                break
        if count ==0:
            print('{}학생이 없습니다.'.format(delname))

def stu_rank(): #학생 등수 처리 함수.
    for stu1 in stuSave:
        rcount = 1
        for stu2 in stuSave:
            if stu1 < stu2:
                rcount += 1
        stu1.rank = rcount
    print('등수가 메겨졌습니다.')
    print('='*60)