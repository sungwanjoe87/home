import os
import json

stuSave =[]
sCount = 0
count = 0


def jsonRead (): #파일 열기 함수
    if 'stuSaveData.json' in os.listdir():
        stuSave = json.load(open('stuSaveData.json','r'))
    else:
        stuSave = []

def jsonSave (): #파일 저장 함수
    if 'stuSaveData.json' in os.listdir():
        json.dump(stuSave,open('stuSaveData.json','w'))
    else:
        json.dump(stuSave,open('stuSaveData.json','w'))


def stusCount ():
    global sCount
    
    if len(stuSave) ==0:
        sCount = 1
    else:
        sCount = stuSave[-1]['stuno']+1
    return sCount


#화면출력함수

def screen_print ():
    jsonRead()
    stusCount()
    print('[학생성적관리프로그램]')
    print('[1.학생성적입력]')
    print('[2.학생성적수정]')
    print('[3.학생성적삭제]')
    print('[4.학생성적전체출력]')    
    print('[5.학생성적검색출력]')
    print('[6.등수처리]')
    print('[0.프로그램 종료]')
    print('='*25)
    choice = input('원하는 번호를 입력하세요>>')
    if not choice.isdigit():
        print('숫자만 입력하세요!!')

    return int(choice)

#성적입력함수

def stu_input():
    global sCount
    print('---{}번째 학생 등록--'.format(sCount))
    stuname = input('학생이름을 입력하세요>>')
    kor = int(input('국어점수를 입력하세요>>'))
    eng = int(input('영어점수를 입력하세요>>'))
    temp = {'stuno':sCount,'stuname':stuname,'kor':kor,\
        'eng':eng,'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
    stuSave.append(temp)
    jsonSave()
    sCount +=1
    print('학생성적이 입력되었습니다.')
    return sCount


#학생성적 수정 함수
def stu_motify():
    count = 0
    jsonRead ()
    print('[학생성적 수정 페이지]')
    print('='*50)
    searchName = (input('수정할 이름을 입력하세요>>'))
    for i,stu in enumerate(stuSave):
        if searchName in stu.values():
            print('{}학생이 검색되었습니다.'.format(searchName))
            print('[점수수정페이지]')
            print('[1.국어점수 수정]')
            print('[2.영어점수 수정]')
            print('[0. 상위메뉴로 이동]')
            searchNo = int(input('원하는 번호를 입력하세요>>'))

            if searchNo ==1:
                print('현재 국어 점수:' ,stu['kor'])
                score =int(input('수정할 국어 점수를 입력하세요>>'))
                stu['kor']=score
                stu['total'] = stu['kor']+stu['eng']
                stu['avg'] = stu['total']/2
                jsonSave()
                print('국어점수가 수정되었습니다.')
            elif searchNo ==2:
                print('현재 영어 점수:',stu['eng'])
                score = int(input('수정할 영어 점수를 입력하세요>>'))
                stu['eng']=score
                stu['total'] = stu['kor']+stu['eng']
                stu['avg'] = stu['total']/2
                jsonSave()
                print('영어점수가 수정되었습니다.')

            elif searchNo ==0:
                print('상위메뉴로 이동합니다...')
            count =1
            break
    if count ==0:
        print('{}학생이 저장되어 있지 않습니다.'.format(searchName))

#학생삭제함수                
def stu_delete ():
    jsonRead
    searchName = input('삭제할 학생을 입력하세요>>')
    count = 0
    for i,stu in enumerate(stuSave):
        if searchName in stu.values():
            del(stuSave[i])
            print('{}학생이 삭제되었습니다.'.format(searchName))
            count =1
            jsonSave
            break
    if count ==0:
        print('{}학생이 없습니다'.format(searchName))

#학생성적 전체 출력 함수
def stu_print():
    jsonRead()
    print('번호','이름','국어','수학','합계','평균','등수',sep='\t')
    print('='*80)
    for stu in stuSave:

        print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],stu['total'],\
            stu['avg'],stu['rank'],sep='\t')


#학생검색 출력함수

def stu_search():
    jsonRead()
    searchName = input('출력할 학생이름을 입력하세요>>')
    count = 0
    for i,stu in enumerate(stuSave):
        if searchName in stu.values():
            print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
            print('='*60)
            print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],\
            stu['total'],stu['avg'],stu['rank'],sep='\t')
            count =1
            break
    if count ==0:
        print('{}학생이 등록되어 있지 않습니다'.format(searchName))

#학생등수 처리 함수

def stu_rank():
    jsonRead()
    for stu in stuSave:
        rcount =1
        for stu2 in stuSave:
            if stu['total'] < stu2['total']:
                rcount +=1
        stu['rank'] =rcount
    jsonSave()
    print('등수처리가 완료되었습니다.')