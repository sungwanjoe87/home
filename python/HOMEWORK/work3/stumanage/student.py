class Student:
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    total = 0
    avg = 0
    rank = 0

#손가락 아파서 수학 뺌.
    def __init__(self,stuname='',kor=0,eng=0):
        Student.stuno +=1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor +eng
        self.avg = self.total/2
        self.rank =0

    def __str__(self): #문자열로 반환해줌.
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint

    def __eq__(self,stuname): #메소드가 같은지 비교
        return self.stuname == stuname

    def __lt__(self,other): #class에서 작동할때에는 이렇게 비교해야 함.
        return self.total < other.total

    def setKor(self,kor): #kor에 입력되는 값이 음수일 경우 원래 kor값으로 입력
        if kor>=0:
            self.kor=kor
            self.total =kor + self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다')

    def setEng(self,eng): #eng에 입력되는 값이 음수일 경우 원래 eng값으로 입력
        if eng>=0:
            self.eng=eng
            self.total = self.kor + eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')
