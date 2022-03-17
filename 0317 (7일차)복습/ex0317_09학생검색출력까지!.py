#학생 성적프로그램. 
#1.학생성적입력, 2.힉생성적수정.\
#  3.학생성적삭제, 4.학생성적전체출력, 5.학생검색출력, 6.등수처리 0프로그램종료.
from turtle import st


stuSave = [] #최종 저장 리스트.
sCount = 0
while True:
    print('[학생성적입력프로그램]')
    print('='*30)
    print('1.학생성적입력')
    print('2.학생성적수정')
    print('3.학생성적삭제')
    print('4.학생성적전체출력')
    print('5.학생검색출력')
    print('6.등수처리')
    print('0.프로그램종료')
    print('='*30)
    #숫자만 받고 숫자가 아닐경우 다시 받기.

    choice = input('원하는 번호를 입력하세요.>>')

    if not choice.isdigit():
        print('숫자만 가능합니다.')
        continue
    
    choice=int(choice)
    
    count =0
    if choice == 1:
        print('학생성적입력을 입력하셨습니다.')
        print('--{}번째 학생 등록--'.format(sCount+1))
        sName = input('학생이름을 입력하세요>>')
        kor = int(input('국어점수를 입력하세요>>'))
        eng = int(input('영어점수를 입력하세요>>'))
        math = int(input('수학점수를 입력하세요>>'))
        total = kor+eng+math #합계
        avg = round(total/3,3)  #평균
        rank = 0 #등수
        temp={'stuNo':sCount+1, 'stuName':sName, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank}
        stuSave.append(temp) #딕셔너리 형태로 리스트에 올리기.
        sCount += 1 #n번째 학생으로 번호 올리기
        print('성적이 입력되었습니다.')

    elif choice == 2:
        print('학생성적수정을 입력하셨습니다.')
        searchName = input('수정할 학생의 이름을 입력하세요...')
        count=0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('{}학생이 검색되었습니다.'.format(searchName))
                print('[점수 수정]')
                print('1.국어 점수 수정')
                print('2.영어 점수 수정')
                print('3.수학 점수 수정')
                print('0.상위 메뉴로 이동')
                searchNo = int((input('수정하고자 하는 과목을 입력해 주세요>>')))
                if searchNo ==1:
                    print('현재 국어점수',stu['kor']) #해당 학생의 현재 국어점수 출력.
                    score = int(input('변경할 국어점수를 입력하세요>>'))
                    stu['kor']=score #해당 학생의 현재국어 점수를 입력한 점수로 변경.
                    stu['total']=stu['kor']+stu['eng']+stu['math'] #kor만 변경되기에 연동된 모든 values 업데이트
                    stu['avg']=round(stu['total']/3,3)
                    print('국어 점수가 변경되었습니다.')
                elif searchNo ==2:
                    print('현재 영어점수',stu['eng']) #해당 학생의 현재 영어점수 출력.
                    score = int(input('변경할 영어점수를 입력하세요>>'))
                    stu['eng']=score #해당 학생의 현재영어 점수를 입력한 점수로 변경.
                    stu['total']=stu['kor']+stu['eng']+stu['math'] #eng만 변경되기에 연동된 모든 values 업데이트
                    stu['avg']=round(stu['total']/3,3)
                    print('영어 점수가 변경되었습니다.')
                elif searchNo ==3:
                    print('현재 수학점수',stu['math']) #해당 학생의 현재 수학점수 출력.
                    score = int(input('변경할 수학점수를 입력하세요>>'))
                    stu['math']=score #해당 학생의 현재수학 점수를 입력한 점수로 변경.
                    stu['total']=stu['kor']+stu['eng']+stu['math'] #math만 변경되기에 연동된 모든 values 업데이트
                    stu['avg']=round(stu['total']/3,3)
                    print('수학 점수가 변경되었습니다.')
                elif searchNo ==0:
                    print('상위메뉴로 이동합니다.')
                count=1
                break
        if count ==0:
            print('해당하는 {}학생이 없습니다.'.format(searchName))

    elif choice == 3:
        print('학생성적삭제를 입력하셨습니다.')
        searchName = input('성적을 삭제할 학생의 이름을 입력하세요>>')
        count=0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                del(stuSave[i]) #리스트에서 del로 해당 학생을 삭제한다.
                print('검색한{}학생이 삭제되었습니다.'.format(searchName))
        if count ==0:
            print('해당하는 학생이 없습니다.')
        
    elif choice == 4:
        print('학생성적전체출력을 입력하셨습니다.')
        print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
        print('='*60)
        for stu in stuSave: #stuSave 리스트 안에서 stu에 있는 딕셔너리의 key에 있는 모든 valuse를 출력한다.
            print(stu['stuNo'], stu['stuName'], stu['kor'], stu['eng'], stu['math'], stu['total'], stu['avg'], stu['rank'],sep='\t')        

    elif choice == 5:
        print('학생성적검색출력을 입력하셨습니다.')
        searchName=input('검색할 학생의 이름을 입력하세요>>')
        count =0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('해당하는 학생의 점수가 출력되었습니다.')
                print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
                print(stu['stuNo'], stu['stuName'], stu['kor'], stu['eng'], stu['math'], stu['total'], stu['avg'], stu['rank'],sep='\t')
                print('='*60)
                count+=1
                break
        if count ==0:
            print('검색하신 이름에 해당하는 학생이 없습니다.')    
    elif choice == 6:
        print('등수처리를 입력하셨습니다.')
        pass
    elif choice == 0:
        print('프로그램을 종료합니다...')
        break
