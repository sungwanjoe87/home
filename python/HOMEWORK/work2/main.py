from stumanage.studef import *

# 하면 안 되는 거지만 궁금해서 한글로 해봤습니다.
while True:
    #화면출력
    choice = 스크린프린트()

    if choice==1:
        학생성적입력()    # 학생성적입력
        
    elif choice == 2:
        학생전체출력()   # 학생전체출력 
        
    elif choice == 3:
        학생성적검색()   # 학생검색출력    
            
    elif choice ==4: 
        학생성적수정()  #학생검색수정
    
    elif choice ==5:
        학생성적삭제() #학생성적 삭제
    
    elif choice ==6:
        print('학생등수 처리를 선택하셨습니다.')
        학생등수처리() #학생등수 처리
    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
        