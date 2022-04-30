class Student:
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0

    def __init__(self,stuname='',kor=0,eng=0,math=0):
        Student.stuno += 1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        rank = 0

    def __str__(self): #자동 str 함수
        stuprint = ('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(\
            self.stuno,self.stuname,self.kor,self.eng,self.math,self.total,self.avg,self.rank))
        return stuprint

    def __eq__(self,stuname): # 같은지 비교 eq
        return self.stuname == stuname

    def __lt__(self,other): #다른 지 비교 lt
        return self.total < other.total 

    def setkor(self,kor): #국어 점수 입력 함수
        if kor >= 0:
            self.kor = kor
            self.total = kor + self.eng + self.math
            self.avg = self.total/3
        else:
            print('잘못된 입력입니다. 다시 입력하세요.')
    def seteng(self,eng): #영어 점수 입력 함수
        if eng >= 0:
            self.eng = eng
            self.total = self.kor + eng + self.math
            self.avg = self.total/3
        else:
            print('잘못된 입력입니다. 다시 입력하세요.')
    def setmath(self,math): #수학 점수 입력 함수
        if math >= 0:
            self.math = math
            self.total = self.kor + self.eng + math
            self.avg = self.total/3
        else:
            print('잘못된 입력입니다. 다시 입력하세요.')