class Student: #class 선언
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0

    def __init__(self,stuname='',kor=0,eng=0,math=0): #생성자 
        Student.stuno += 1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0

    def __str__(self):  #스트링 호출 함수
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(\
            self.stuno,self.stuname, self.kor, self.eng, self.math,\
            self.total,self.avg,self.rank)
        return stuprint

    def __eq__(self,stuname): #eq 호출 함수
        return self.stuname == stuname

    def __lt__(self,other): #비교 호출 함수
        return self.total < other.total 

    def setkor(self,kor): #국어 입력 함수
        if kor >= 0:
            self.kor = kor
            self.total = kor+self.eng+self.math
            self.avg = self.total/3
        else:
            print("숫자가 잘못 입력 되었습니다.")  
    def seteng(self,eng): #영어 입력 함수
        if eng >= 0:
            self.eng = eng
            self.total = self.kor+eng+self.math
            self.avg = self.total/3
        else:
            print("숫자가 잘못 입력 되었습니다.")  
    def setmath(self,math): #수학 입력 함수
        if math >= 0:
            self.math = math
            self.total = self.kor+self.eng+math
            self.avg = self.total/3
        else:
            print("숫자가 잘못 입력 되었습니다.")  
