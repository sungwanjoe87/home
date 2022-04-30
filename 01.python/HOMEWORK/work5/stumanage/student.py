class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname='',kor=0,eng=0):
        Student.stuno += 1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        self.rank =0
    
    def __str__(self): #문자열 프린트 함수
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint

    def __eq__(self,stuname): #같은지 비교하는 함수
        return self.stuname == stuname

    def __lt__(self,other): #외부것이 큰지 비교하는 함수
        return self.total < other.total

    def getKor(self): #외부에서 접근하지 못하게 하는 함수
        return self.__kor

    def setKor(self,kor): #kor의 값이 음수이면 kor값 그대로 넣는 함수
        if kor>=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

    def setEng(self,eng): #영어의 값이 음수가 안 들어가게 하는 함수
        if eng>=0:
            self.eng=eng
            self.total=self.kor+eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

