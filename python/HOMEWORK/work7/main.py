from stumanage.studef import *


while True:

    choice = screenPrint() #화면 출력

    if choice==1:
        stuInput()    # 학생성적 입력
        
    elif choice == 2:
        stuOutput()   # 학생전체 출력 
        
    elif choice == 3:
        stuSearch()   # 학생검색 출력    
            
    elif choice ==4: 
        stuModify()  # 학생검색 수정
    
    elif choice ==5:
        stuDelete() # 학생성적 삭제
    
    elif choice ==6:
        stuRank() #학생등수 처리
    
    elif choice ==0:
        print('프로그램 종료.')
        break
        