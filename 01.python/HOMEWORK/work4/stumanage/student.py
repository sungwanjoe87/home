class Student :
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    total = 0
    avg = 0
    rank = 0


    def __init__(self,stuname='',kor=0,eng=0):
        Student.stuno += 1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor + eng
        self.avg = self.total/2
        rank = 0 #있다 처리할거임.

     #str문자열 불러오기용.
    def __str__(self):
        sprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,\
            self.kor,self.eng,self.total,self.avg,self.rank)
        return sprint

    def __eq__(self,stuname): #비교할 것 가지고 오기 (이름 비교용)
        return self.stuname == stuname

    def __lt__(self,other): #밖에서 오는 것과 비교.
        return self.total < other.total

    def setKor(self,kor): #국어점수 체크용
        if kor >=0:
            self.kor = kor
            self.total = kor +self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못 되었습니다.')

    def setEng(self,eng): #영어점수 체크용
        if eng >=0:
            self.eng = eng
            self.total = self.kor + eng
            self.avg = self.total/2
        else:
            print('입력이 잘 못되었습니다.')

    