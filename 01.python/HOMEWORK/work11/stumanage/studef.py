from stumanage.Student import Student
import cx_Oracle

stuSave=[]


#화면 출력 함수
def screenPrint ():
    print('[학생프로그램]')
    print('-'*40)
    print('[1.학생성적입력]')
    print('[2.학생성적출력]')
    print('[3.학생검색출력]')
    print('[4.학생성적수정]')
    print('[5.학생성적삭제]')
    print('[6.학생등수처리]')
    print('[0.프로그램종료]')
    print()
    choice = int(input('원하는 번호를 입력하세요.>>'))

    return choice

def stuInput(): #학생성적입력
    while True:
        print ('[학생성적입력]')
        stuname = input('학생이름을 입력하세요 (0.종료)>>')
        if stuname =='0':
            break
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        math = int(input('수학점수를 입력하세요.>>'))
        
        #oracleDB의 경우
        #conn = cx_Oracle.connect("ora_user/1234@192.168.0.17:1521/xe")
        #cs = conn.cursor()
        #sql = "insert into studata values(stu_seq.naxtval,\
        # :1,:2,:3,:4,:5,:6,:7)"
        #cs.execute(sql,(stuname,kor,eng,math,kor+eng+math,\
        # (kor+eng+math)/3,1))
        #print("insert : ",cs.rowcoint)
        temp = Student(stuname,kor,eng,math)
        stuSave.append(temp)
        print('{}번. {}학생이 저장되었습니다.'.format(temp.stuno,stuname))
        #print('{}학생이 저장되었습니다.'.format(stuname))
        #cs.close()
        #conn.commit()
        #conn.close()
        print()


def topTitle(): #상단 타이틀 출력
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
    print('-'*60)
    print()

def stuOutput(): #학생성적 출력
    print()
    print('[학생성적출력]')
    topTitle()
    for stu in stuSave:
        print(stu)

def stuSearch(): #학생검색출력
    print()
    print('[학생검색출력')
    sname = input('학생이름을 입력하세요.>>')
    count = 0
    for stu in stuSave:
        if stu == sname:
            topTitle()
            print(stu)
            count=1
            break

    if count == 0:
        print('{}학생은 없습니다. 다른 이름을 입력하세요.'.format(sname))


def stuModify(): #성적수정출력
    print()
    print('[학생성적수정]')
    sname = input('학생이름을 입력하세요.>>')
    count = 0
    for stu in stuSave:
        if stu == sname:
            print('{} 학생이 검색되었습니다.' .format(sname))
            print('[성적 수정]')
            print('1.국어 점수')
            print('2.영어 점수')
            print('3.수학 점수')
            cnum = int(input('수정할 과목의 번호를 입력하세요.>>'))
            if cnum == 1:
                print('현재국어 점수 : {}' .format(stu.kor))
                score = int(input('수정할 점수를 입력하세요>>'))
                stu.setkor(score)
                print('국어점수가 {}로 수정되었습니다' .format(score))
            elif cnum == 2:
                print('현재수학 점수 : {}' .format(stu.eng))
                score = int(input('수정할 점수를 입력하세요>>'))
                stu.seteng(score)
                print('영어점수가 {}로 수정되었습니다' .format(score))
            elif cnum == 3:
                print('현재국어 점수 : {}' .format(stu.math))
                score = int(input('수정할 점수를 입력하세요>>'))
                stu.setmath(score)
                print('수학점수가 {}로 수정되었습니다' .format(score))
            count = 1
            break
    
        if count ==0:
            print('검색된 학생이 없습니다. 다시 입력해 주세요.')
    

def stuDelete (): #검색 삭제 함수.
    print()
    print('[학생성적삭제]')
    count = 0
    sname = input('삭제할 이름을 입력하세요>>')
    for i, stu in enumerate(stuSave):
        if stu == sname:
            print ('{} 학생이 검색되었습니다.' .format(sname))
            flag = input('정말 삭제 하시겠습니까? (Y or N)')
            if flag == 'Y':
                del(stuSave[i])
                print('{}학생이 삭제 되었습니다.' .format(sname))
                count = 1
                break           
            elif flag == 'N':
                break
        elif count == 0:
            print('{}학생이 없습니다.' .format(sname))

def stuRank():
    print('[학생등수처리]')
    for stu1 in stuSave:
        rcount = 1
        for stu2 in stuSave:
            if stu1 < stu2:
                rcount +=1
        stu1.rank = rcount
    print('학생등수처리 완료.')
    print()