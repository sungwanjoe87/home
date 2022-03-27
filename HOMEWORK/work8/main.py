from stumanage.studef import *

# 프로그램 시작
while True:
    #화면출력
    choice = screen_print()

    if choice==1:
        stu_input()    # 학생성적입력
        
    elif choice == 2:
        stu_output()   # 학생전체출력 
        
    elif choice == 3:
        stu_search()   # 학생검색출력    
            
    elif choice ==4: 
        stu_modify()  #학생검색수정
    
    elif choice ==5:
        stu_delete() #학생성적 삭제
    
    elif choice ==6:
        stu_rank() #학생등수 처리
        
    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
        