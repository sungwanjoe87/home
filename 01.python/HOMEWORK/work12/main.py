from stumanage.studef import *

#프로그램 시작

while True:
    #화면출력
    choice = screenPrint()

    if choice == 1:
        stuInput()  #학생 성적 입력.

    elif choice == 2:
        stuPrint()  #학생 성적 출력.

    elif choice == 3:
        stuSearch() #학생 검색 출력.

    elif choice == 4:
        stuModify() #학생 점수 수정.

    elif choice == 5:
        stuDelete() #학생 점수 삭제.

    elif choice ==6:
        stuRank() #학생 등수 처리.

    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
    
    