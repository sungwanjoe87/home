class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0

#생성자 함수
    def __init__(self,stuname='',kor=0,eng=0): 
        Student.stuno += 1 #클래스 변수
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        self.rank =0
    def __str__(self):
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint

#객체가 같은지 비교.
    def __eq__(self,stuname):
        return self.stuname == stuname
#객체가 큰지 비교.
    def __lt__(self,other):
        return self.total < other.total
#외부에서 kor에 접근하지 못하게 함.
    def getKor(self):
        return self.__kor
#외부에서 eng에 접근하지 못하게 함.
    def getKor(self):
        return self.__kor        
#kor에 음수가 들어가지 못하게 하는 함수
    def setKor(self,kor):
        if kor>=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')
#eng에 음수가 들어가지 못하게 하는 함수
    def setEng(self,eng):
        if eng>=0:
            self.eng=eng
            self.total=self.kor+eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

