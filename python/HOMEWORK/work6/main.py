
from stumanage.studef import *

while True:
    
    choice = screenPrint() #화면출력

    if choice==1:
        print('학생 성적을 입력합니다.')
        stuInput()    # 학생성적입력
        
    elif choice == 2:
        print('학생성적 전체 출력을 선택 하셨습니다.')
        stuoutput()   # 학생전체출력 
        
    elif choice == 3:
        print('학생검색 및 출력을 선택 하셨습니다.')
        stusearch()   # 학생검색출력    
            
    elif choice ==4: 
        print('학생검색 및 수정을 선택 하셨습니다.')
        stuModify()  #학생검색수정
    
    elif choice ==5:
        print('학생성적 삭제를 선택하셨습니다.')
        stuDelete() #학생성적삭제
    
    elif choice ==6:
        print('학생등수 처리를 선택하셨습니다.')
        sturank() #학생등수처리
    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
        