# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성
# stuSave = [[0]*7 for i in range(0)]
# import stu_def          #모듈선언
# import stu_def as stu   #모듈선언후 별칭사용
from stu_def import *
import json

while True:
    choice = 0  #화면출력 선택번호변수
    choice = screen_print()  # 화면출력함수 호출
    
    if choice==1: # 학생성적입력
        
        sCount = stu_input()
    
    elif choice==2: #학생성적수정
        
        stu_modify()
        
    elif choice==3: #학생성적삭제
        stu_delete()
        
            
    elif choice==4: #학생성적전체출력
        stu_print()
        
    elif choice==5: #학생성적검색출력
        stu_Search()
        
    
    elif choice==6: #학생등수처리
        stu_rank() 
        
    elif choice==0:
        print('프로그램을 종료합니다.')
        break