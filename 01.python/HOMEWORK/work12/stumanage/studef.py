from stumanage.Student import Student

#screenPrint (화면 출력), stuInput(1.학생 입력), stuPrint(2.학생출력), stuSerach(3.학생검색출력), , stuModify(4.학생점수수정), stuDelete(5.학생점수삭제) stuRank(6.학생등수처리)

stuSave = []

def screenPrint ():
    print('[학생 성적 프로그램]')
    print('[1.학생 점수 입력]')
    print('[2.학생 점수 출력]')
    print('[3.학생 점수 검색]')
    print('[4.학생 점수 수정]')
    print('[5.학생 점수 삭제]')
    print('[6.학생 등수 처리]')
    print('[0.프로 그램 종료]')
    print() #한칸 띄우기
    choice = int(input('원하는 번호를 입력하세요.>>'))
    
    return choice

def stuInput ():
    while True:
        print('[학생 점수 입력]')
        stuname = input('학생이름을 입력하세요.>>(0.입력종료)')
        if stuname == '0':
            break
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>'))
        math = int(input('수학 점수를 입력하세요.>>'))
        temp = Student(stuname,kor,eng,math)
        stuSave.append(temp)
        print('{}번 {}학생이 입력되었습니다.'.format(temp.stuno,stuname))
        print()

def topTitle():
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
    print('-'*60)
    print()


def stuPrint ():
    print('[학생 점수 출력]')
    topTitle()
    for stu in stuSave:
        print(stu)

def stuSearch ():
    print('[학생 검색 출력]')
    searchname = input('찾으실 학생의 이름을 입력하세요.>>')
    count = 0
    for stu in stuSave:
        if stu == searchname:
            topTitle()
            print(stu)
            count = 1
            break
        
    if count == 0:
        print('찾으시는 {}학생이 없습니다. 다시 입력하세요.'.fomat(searchname))

def stuModify():
    print()
    print('[학생 점수 수정]')
    searchname = input('점수를 수정할 학생의 이름을 입력하세요.>>')
    count = 0
    for stu in stuSave:
        if stu == searchname:
            print('{}학생이 검색 되었습니다.'.format(searchname))
            print('[수정 과목 선택]')
            print('[1. 국어 성적 수정]')
            print('[2. 영어 성적 수정]')
            print('[3. 수학 성적 수정]')
            choicenum =int(input('수정을 원하는 과목의 번호를 입력하세요'))

            if choicenum == 1:
                print('현재국어점수: {} '.format(stu.kor))
                score = int(input('수정하려는 점수를 입력하세요>>'))
                stu.setkor(score)
                print('국어점수가 {}로 수정되었습니다.'.format(score))

            elif choicenum ==2:
                print('현재영어점수: {}'.format(stu.eng))
                score = int(input('수정하려는 점수를 입력하세요>>'))
                stu.seteng(score)
                print('영어점수가 {}로 수정 되었습니다.'.format(score))
            
            elif choicenum ==3:
                print('현재수학점수: {}'.format(stu.math))
                score = int(input('수정하려는 점수를 입력하세요>>'))
                stu.setmath(score)
                print('수학점수가 {}로 수정 되었습니다.'.format(score))
            count = 1
            break

    if count == 0:
        print('찾으시는 {}학생은 없습니다. 다시 입력하세요'.format(searchname))


def stuDelete():
    print('[학생 점수 삭제]')
    count = 0
    searchname = input('삭제하려는 학생의 이름을 입력하세요.>>')
    for i, stu in enumerate(stuSave):
        if stu == searchname:
            print('{}학생이 검색되었습니다.'.format(searchname))
            flag = input('정말 삭제 하시겠습니까? (Y or N)')
            if flag == 'Y':
                del(stuSave[i])
                print('{}학생의 점수가 삭제되었습니다.'.format(searchname))

            elif flag == 'N':
                break

    if count == 0:
        print('{}학생은 없습니다. 다시 검색해 주세요'.format(searchname))

def stuRank():
    print('[학생 등수 처리]')
    for stu1 in stuSave:
        rcount = 1
        for stu2 in stuSave:
            if stu1 < stu2:
                rcount += 1
        stu1.rank = rcount
    print('학생등수처리 완료')
    print()