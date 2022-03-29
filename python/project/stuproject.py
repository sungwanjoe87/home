from stu_def import *


while True:
    choice =0

    choice = screen_print()

    if choice ==1: #학생성적입력
        sCount = stu_input()
    elif choice ==2: #학생성적 수정
        stu_motify()
    elif choice ==3: #학생성적 삭제
        stu_delete()
    elif choice ==4: #학생성적 전체 출력
        stu_print()
    elif choice ==5: #학생성적 검색 출력
        stu_search()
    elif choice ==6: #학생등수 처리
        stu_rank()
    elif choice ==0:
        print('프로그램을 종료합니다.')
        break
