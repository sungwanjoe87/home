
students = []
count = 1


while True:
    stu_no = count
    print('학생번호:', stu_no)
    stu_name = input('학생이름을 입력하세요:')
    kor = int(input('국어성적을 입력하세요:'))
    math = int(input('수학성적을 입력하세요'))
    eng = int(input('영어점수를 입력하세요:'))
    total = kor+math+eng
    avg = total/3
    rank = 0
    student = [stu_no, stu_name, kor, math, eng, total, avg, rank]
    students.append(student)
    print(students)
    count += 1