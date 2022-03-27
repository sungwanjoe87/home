class Student:
    stuno=0   #변수
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname='',kor = 0,eng = 0): #생성자
        Student.stuno += 1 
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        self.rank = 0
    def __str__(self):
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint

#객체가 같은지 비교
    def __eq__(self,stuname):
        return self.stuname == stuname
#객체
    def __lt__(self,other):
        return self.total < other.total

    def getKor(self): #내부에서만 접근가능하도록 __(변수)
        return self.__kor

    def setKor(self,kor): #음수가 들어오면 원래 kor 값을 넣는 함수
        if kor>=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

    def setEng(self,eng): #음수가 들어오면 원래 eng 값을 넣는 함수
        if eng>=0:
            self.eng=eng
            self.total=self.kor+eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

