from stumanage.studef import *

# 프로그램 시작
while True:
    #화면출력
    choice = screenPrint()

    if choice==1:
        stuInput()    # 학생성적입력
        
    elif choice == 2:
        stuOutput()   # 학생전체출력 
        
    elif choice == 3:
        stuSearch()   # 학생검색출력    
            
    elif choice ==4: 
        stuModify()  #학생검색수정
    
    elif choice ==5:
        stuDelete() #학생성적 삭제
    
    elif choice ==6:
        print('학생등수 처리를 선택하셨습니다.')
        stuRank() #학생등수 처리
    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
        